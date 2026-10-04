#!/usr/bin/env python3
"""Optional public-metadata tools. Standard library only; no manuscript mutation.

Selected workflows adapted from system-paper-skill (MIT).
See NOTICE.md and references/repository-migration.md.
"""
import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

USER_AGENT = 'systems-paper-writing/1.0 (public-reference-metadata)'
MAX_BYTES = 2_000_000


def normalize_doi(value):
    value = str(value or '').strip()
    value = re.sub(r'^(?:https?://(?:dx\.)?doi\.org/|doi\s*:\s*)', '', value, flags=re.I)
    if not re.fullmatch(r'10\.\d{4,9}/[^\s]+', value):
        raise ValueError('Expected a DOI such as 10.1145/945445.945450')
    return value.lower()


def fetch(url, accept='application/json'):
    req = Request(url, headers={'User-Agent': USER_AGENT, 'Accept': accept})
    with urlopen(req, timeout=20) as response:
        raw = response.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError('Metadata response exceeded 2 MB')
    return raw.decode('utf-8')


def text(value):
    return value[0] if isinstance(value, list) and value else value if isinstance(value, str) else ''


def record(item):
    authors = []
    for author in item.get('author', []):
        authors.append(author.get('name') or ' '.join(x for x in [author.get('given'), author.get('family')] if x))
    date = item.get('issued', {}).get('date-parts', [[]])
    return {'doi': item.get('DOI', ''), 'title': text(item.get('title')),
            'authors': authors, 'venue': text(item.get('container-title')),
            'year': date[0][0] if date and date[0] else None,
            'type': item.get('type'), 'url': item.get('URL', ''), 'source': 'crossref'}


def lookup(doi):
    doi = normalize_doi(doi)
    data = json.loads(fetch('https://api.crossref.org/works/' + quote(doi, safe='')))
    return record(data['message'])


def search(query, limit=5):
    if not 1 <= limit <= 20:
        raise ValueError('limit must be between 1 and 20')
    params = urlencode({'query.bibliographic': query, 'rows': limit})
    data = json.loads(fetch('https://api.crossref.org/works?' + params))
    return {'query': query, 'status': 'candidates',
            'papers': [record(x) for x in data['message'].get('items', [])]}


def search_links(topic, venues=()):
    def urls(query):
        return {'query': query,
                'dblp': 'https://dblp.org/search?' + urlencode({'q': query}),
                'google_scholar': 'https://scholar.google.com/scholar?' + urlencode({'q': query}),
                'semantic_scholar': 'https://www.semanticscholar.org/search?' + urlencode({'q': query}),
                'openalex': 'https://openalex.org/works?' + urlencode({'search': query})}
    return {'global': urls(topic), 'per_venue': [urls(topic + ' ' + v) for v in venues]}


def bibtex(doi):
    doi = normalize_doi(doi)
    urls = ['https://doi.org/' + quote(doi, safe='/'),
            'https://api.crossref.org/works/' + quote(doi, safe='') + '/transform/application/x-bibtex']
    for url in urls:
        try:
            result = fetch(url, 'application/x-bibtex').strip()
            if not re.match(r'^@(?:article|inproceedings|proceedings|book|incollection|misc|techreport|phdthesis|mastersthesis|dataset|software|unpublished|inbook|manual|booklet)\s*[{(]', result, re.I):
                raise ValueError('Metadata endpoint did not return a recognized BibTeX entry')
            return {'doi': doi, 'bibtex': result, 'bibtex_source': url,
                    'status': 'retrieved', 'next_step': 'Check the version, author order, fields, citation key and project bibliography style.'}
        except (OSError, ValueError):
            if url == urls[-1]:
                raise


def normalized(value):
    value = unicodedata.normalize('NFKC', str(value or '')).casefold()
    return ' '.join(re.sub(r'[^\w\s]', ' ', value).split())


def author_name(value):
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        return value.get('name') or value.get('display_name') or ' '.join(x for x in [value.get('given'), value.get('family')] if x)
    raise ValueError('authors must contain names or metadata objects')


def compare(claimed, observed):
    checks = {}
    for field in ['doi', 'title', 'year', 'venue', 'authors']:
        a, b = claimed.get(field), observed.get(field)
        if a is None or a == '' or a == []:
            checks[field] = 'not_supplied'
        elif b is None or b == '' or b == []:
            checks[field] = 'missing_in_source'
        elif field == 'doi':
            checks[field] = 'match' if normalize_doi(a) == normalize_doi(b) else 'review'
        elif field == 'authors':
            if not isinstance(a,list) or not isinstance(b,list):
                raise ValueError('authors must be an ordered list')
            checks[field] = 'match' if [normalized(author_name(x)) for x in a] == [normalized(author_name(x)) for x in b] else 'review'
        else:
            checks[field] = 'match' if normalized(a) == normalized(b) else 'review'
    status = 'needs_review' if 'review' in checks.values() else 'metadata_match' if all(v == 'match' for v in checks.values()) else 'metadata_partial'
    return {'status': status, 'checks': checks, 'matched_record': observed,
            'claim_support': 'requires_reading',
            'interpretation': 'Compare name variants, online/issue dates and venue aliases before editing; preserve supplied metadata.'}


def verify(paper):
    if not isinstance(paper,dict):
        raise ValueError('Each paper must be an object')
    try:
        if not paper.get('doi'):
            return {'status': 'needs_identifier', 'candidates': search(paper['title'])['papers'] if paper.get('title') else [], 'claim_support': 'requires_reading'}
        return compare(paper, lookup(paper['doi']))
    except (OSError, ValueError, KeyError) as exc:
        return {'status': 'unresolved', 'error': str(exc), 'claim_support': 'requires_reading'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest='command', required=True)
    links = subs.add_parser('links', help='Generate search links without network access')
    links.add_argument('--topic', required=True)
    links.add_argument('--venue', action='append', default=[])
    query = subs.add_parser('search', help='Retrieve candidate metadata from Crossref')
    query.add_argument('--query', required=True)
    query.add_argument('--limit', type=int, default=5)
    for cmd in ['lookup', 'bibtex']:
        sub = subs.add_parser(cmd)
        sub.add_argument('--doi', required=True)
    check = subs.add_parser('verify', help='Compare supplied JSON fields with DOI metadata')
    check.add_argument('--input', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == 'links':
            result = search_links(args.topic, args.venue)
        elif args.command == 'search':
            result = search(args.query, args.limit)
        elif args.command == 'lookup':
            result = lookup(args.doi)
        elif args.command == 'bibtex':
            result = bibtex(args.doi)
        else:
            data = json.loads(args.input.read_text())
            papers = data.get('papers') if isinstance(data,dict) else data
            if not isinstance(papers,list) or len(papers)>100 or any(not isinstance(p,dict) for p in papers):
                raise ValueError('Expected up to 100 paper objects or an object with a papers list')
            result = [{'input':p, 'verification':verify(p)} for p in papers]
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({'status':'error','error':str(exc)}),file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
