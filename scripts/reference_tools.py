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

USER_AGENT = 'systems-paper-writing/1.3.0 (public-reference-metadata)'
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


class StructureError(ValueError):
    """Invalid caller or provider data, not an internal programming failure."""


def text(value):
    if value is None or value == []:
        return ''
    if isinstance(value, list):
        if not all(isinstance(x, str) for x in value):
            raise StructureError('Text arrays must contain strings')
        return value[0]
    if not isinstance(value, str):
        raise StructureError('Expected text or a text array')
    return value


def author_name(value):
    if isinstance(value, str) and value.strip():
        return value
    if isinstance(value, dict):
        for key in ('name', 'display_name', 'given', 'family'):
            if key in value and not isinstance(value[key], str):
                raise StructureError('Author name components must be strings')
        name = value.get('name') or value.get('display_name') or ' '.join(
            value[k] for k in ('given', 'family') if value.get(k))
        if name:
            return name
    raise StructureError('Authors must contain nonempty names or name objects')


def validate_paper(item):
    if not isinstance(item, dict):
        raise StructureError('Each paper must be an object')
    for field in ('doi', 'title', 'venue'):
        if field in item and item[field] is not None and not isinstance(item[field], str):
            raise StructureError(field + ' must be a string')
    if item.get('year') is not None and (isinstance(item['year'], bool) or
            not isinstance(item['year'], (str, int))):
        raise StructureError('year must be a string or integer')
    if 'authors' in item:
        if not isinstance(item['authors'], list):
            raise StructureError('authors must be an ordered list')
        for author in item['authors']:
            author_name(author)


def record(item):
    if not isinstance(item, dict):
        raise StructureError('Crossref record must be an object')
    if not item or not any(k in item for k in ('DOI', 'title', 'author')):
        raise StructureError('Crossref record lacks identifying metadata')
    authors = item.get('author', [])
    if not isinstance(authors, list):
        raise StructureError('Crossref author must be an ordered array')
    issued = item.get('issued', {})
    if not isinstance(issued, dict):
        raise StructureError('issued must be an object')
    date = issued.get('date-parts', [[]])
    if not isinstance(date, list) or not all(isinstance(x, list) for x in date):
        raise StructureError('date-parts must be an array of arrays')
    result = {'doi': item.get('DOI', ''), 'title': text(item.get('title')),
              'authors': [author_name(x) for x in authors],
              'venue': text(item.get('container-title')),
              'year': date[0][0] if date and date[0] else None,
              'type': item.get('type'), 'url': item.get('URL', ''), 'source': 'crossref',
              'raw_record': item}
    validate_paper(result)
    if not any(result[k] for k in ('doi', 'title', 'authors')):
        raise StructureError('Crossref record contains no identifying metadata values')
    return result


def message(data):
    if not isinstance(data, dict) or not isinstance(data.get('message'), dict):
        raise StructureError('Expected a Crossref message object')
    return data['message']


def lookup(doi):
    doi = normalize_doi(doi)
    data = json.loads(fetch('https://api.crossref.org/works/' + quote(doi, safe='')))
    return record(message(data))


def unresolved(exc):
    return {'status': 'unresolved', 'error_type': type(exc).__name__,
            'error': str(exc), 'claim_support': 'requires_reading'}


def search(query, limit=5):
    if not isinstance(query, str) or not query.strip():
        raise StructureError('query must be nonempty text')
    if not 1 <= limit <= 20:
        raise ValueError('limit must be between 1 and 20')
    params = urlencode({'query.bibliographic': query, 'rows': limit})
    items = message(json.loads(fetch('https://api.crossref.org/works?' + params))).get('items')
    if not isinstance(items, list):
        raise StructureError('Crossref items must be an array')
    papers, errors = [], []
    for index, item in enumerate(items):
        try:
            papers.append(record(item))
        except StructureError as exc:
            errors.append({'index': index, 'raw_record': item, **unresolved(exc)})
    return {'query': query, 'status': 'partial_candidates' if errors else 'candidates',
            'papers': papers, 'errors': errors}


def search_links(topic, venues=()):
    def urls(query):
        return {'query': query,
                'dblp': 'https://dblp.org/search?' + urlencode({'q': query}),
                'google_scholar': 'https://scholar.google.com/scholar?' + urlencode({'q': query}),
                'semantic_scholar': 'https://www.semanticscholar.org/search?' + urlencode({'q': query}),
                'openalex': 'https://openalex.org/works?' + urlencode({'search': query})}
    return {'global': urls(topic), 'per_venue': [urls(topic + ' ' + v) for v in venues]}


def bibtex_fields(body):
    """Read simple top-level fields; reject unsupported concatenation/macros safely."""
    fields = []
    pos = 0
    while body[pos:].strip():
        match = re.match(r'\s*([A-Za-z][A-Za-z0-9_-]*)\s*=\s*', body[pos:])
        if not match:
            return None
        name = match[1].lower()
        pos += match.end()
        if pos >= len(body):
            return None
        opener = body[pos]
        if opener in '{"':
            pos += 1
            start, depth, escaped = pos, 1, False
            while pos < len(body):
                char = body[pos]
                if escaped:
                    escaped = False
                elif char == '\\':
                    escaped = True
                elif opener == '{' and char == '{':
                    depth += 1
                elif (opener == '{' and char == '}') or (opener == '"' and char == '"'):
                    depth -= 1
                    if depth == 0:
                        break
                pos += 1
            if depth:
                return None
            value = body[start:pos]
            pos += 1
        else:
            number = re.match(r'\d+', body[pos:])
            if not number:
                return None
            value = number[0]
            pos += number.end()
        fields.append((name, value))
        while pos < len(body) and body[pos].isspace():
            pos += 1
        if pos < len(body):
            if body[pos] != ',':
                return None
            pos += 1
    return fields


def bibtex_checks(raw, doi):
    """Conservative single-entry envelope check, not a complete BibTeX parser."""
    start = re.match(r'\s*@(?:article|inproceedings|proceedings|book|incollection|misc|techreport|phdthesis|mastersthesis|dataset|software|unpublished|inbook|manual|booklet)\s*([{(])', raw, re.I)
    balanced = False
    if start:
        # Balance delimiters outside quoted strings, retaining nested field braces.
        stack, quoted, escaped, end = [start[1]], False, False, None
        for index in range(start.end(), len(raw)):
            char = raw[index]
            if escaped:
                escaped = False
                continue
            if char == '\\':
                escaped = True
                continue
            if char == '"' and len(stack) == 1:
                quoted = not quoted
            if quoted:
                continue
            if char == '{':
                stack.append(char)
            elif char in '})':
                if char == ')' and stack[-1] == '{':
                    continue
                if (stack[-1], char) not in (('{', '}'), ('(', ')')):
                    break
                stack.pop()
                if not stack:
                    end = index
                    break
        balanced = end is not None and not raw[end + 1:].strip() and not quoted
    key = re.match(r'\s*[^,{}()\s]+\s*,', raw[start.end():]) if start else None
    fields = bibtex_fields(raw[start.end() + key.end():end]) if balanced and key else None
    syntax = 'basic_pass' if fields else 'invalid_or_unsupported'
    doi_fields = [value for name, value in (fields or []) if name == 'doi']
    identity = 'not_checked' if syntax != 'basic_pass' else 'missing'
    if doi_fields:
        try:
            identifiers = [normalize_doi(value) for value in doi_fields]
            identity = 'match' if all(x == doi for x in identifiers) else 'conflict'
        except ValueError:
            identity = 'unresolved'
    return {'syntax': syntax, 'identifier': identity,
            'fields_present': sorted(set(name for name, _ in (fields or []))),
            'claim_support': 'requires_reading'}


def bibtex(doi):
    doi = normalize_doi(doi)
    urls = ['https://doi.org/' + quote(doi, safe='/'),
            'https://api.crossref.org/works/' + quote(doi, safe='') + '/transform/application/x-bibtex']
    attempts = []
    for url in urls:
        try:
            raw = fetch(url, 'application/x-bibtex')
        except (OSError, ValueError) as exc:
            attempts.append({'source': url, **unresolved(exc)})
            continue
        checks = bibtex_checks(raw, doi)
        attempt = {'source': url, 'raw': raw, **checks}
        attempts.append(attempt)
        if checks['syntax'] == 'basic_pass':
            return {'doi': doi, 'bibtex': raw, 'bibtex_source': url,
                    'status': 'retrieved', 'validation': checks, 'attempts': attempts,
                    'next_step': 'Review metadata, version, author order and source passages.'}
    return {'doi': doi, 'status': 'unresolved', 'attempts': attempts,
            'claim_support': 'requires_reading'}


def normalized(value):
    # Preserve punctuation and operators: C++, C#, < and > carry meaning.
    return ' '.join(unicodedata.normalize('NFC', str(value)).casefold().split())


def field_value(field, value):
    if field == 'year':
        return str(value).strip()
    return normalized(value)


def compare(claimed, observed):
    validate_paper(claimed)
    validate_paper(observed)
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
            checks[field] = 'match' if field_value(field, a) == field_value(field, b) else 'review'
    status = 'needs_review' if 'review' in checks.values() else 'metadata_match' if all(v == 'match' for v in checks.values()) else 'metadata_partial'
    return {'status': status, 'checks': checks, 'matched_record': observed,
            'claim_support': 'requires_reading',
            'interpretation': 'Compare name variants, online/issue dates and venue aliases before editing; preserve supplied metadata.'}


def verify(paper):
    try:
        validate_paper(paper)
        if not paper.get('doi'):
            candidates = search(paper['title']) if paper.get('title') else {'papers': []}
            return {'status': 'needs_identifier', 'candidates': candidates['papers'],
                    'candidate_errors': candidates.get('errors', []),
                    'claim_support': 'requires_reading'}
        return compare(paper, lookup(paper['doi']))
    except (OSError, ValueError) as exc:
        return unresolved(exc)


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
            if not isinstance(papers,list) or len(papers)>100:
                raise ValueError('Expected a list of up to 100 entries or an object with a papers list')
            result = [{'input':p, 'verification':verify(p)} for p in papers]
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError) as exc:
        print(json.dumps({'status':'error','error':str(exc)}),file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
