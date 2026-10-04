# Finding and checking references

Use this optional workflow when drafting related work, locating support for a claim, or importing reference metadata. It consolidates selected functions from the retired `system-paper-skill` repository; see [migration](repository-migration.md).

## Identify the evidence needed

State the technical question and the comparison dimension before searching. Search relevant mechanisms and assumptions, not only system names. Prioritize original papers, publisher records, author artifacts, and official documentation. A venue preference narrows a search; it does not establish correctness or justify excluding relevant prior work.

The helper uses Python 3 and the standard library:

```bash
python3 scripts/reference_tools.py links --topic "GPU preemption" --venue OSDI --venue SOSP
python3 scripts/reference_tools.py search --query "GPU preemption scheduling" --limit 5
python3 scripts/reference_tools.py lookup --doi 10.1145/945445.945450
python3 scripts/reference_tools.py bibtex --doi 10.1145/945445.945450
python3 scripts/reference_tools.py verify --input papers.json
```

`links` runs offline and produces DBLP, Google Scholar, Semantic Scholar, and OpenAlex URLs. `search` queries Crossref and returns candidate records; venue text in a query is not an exact venue filter. Check candidates against publication pages. `lookup` uses Crossref's DOI record. `bibtex` uses DOI content negotiation and returns the retrieved entry with its source.

Network commands send the supplied bibliographic query or DOI to public metadata services. Pass bibliographic information, not private manuscript text. Each request has a 20-second timeout and a 2 MB response cap. The helper prints JSON and does not modify the manuscript or bibliography.

## Supply structured metadata

`verify` accepts a list of paper objects or `{"papers": [...]}`:

```json
[
  {
    "doi": "10.1234/example",
    "title": "Example title",
    "authors": ["Alice Lin", "Bo Wu"],
    "year": 2024,
    "venue": "Example Conference"
  }
]
```

This JSON illustrates the schema; the example identifier is not a reference. Authors must be an ordered list of strings or metadata objects. Extract BibTeX into these fields using the project's existing parser if needed; the helper does not parse arbitrary BibTeX syntax.

## Interpret the result

| Status | Meaning and action |
| --- | --- |
| `metadata_match` | All five supplied fields match the returned metadata under normalization; read the paper to check claim support. |
| `metadata_partial` | Available fields agree, but input or source fields are missing; complete the comparison from evidence. |
| `needs_review` | At least one supplied field differs; inspect version, author order, initials, venue aliases, and online versus issue dates. |
| `needs_identifier` | No DOI was supplied; title search produces candidates for manual identification. |
| `unresolved` | The record could not be checked, for example because of a timeout or invalid identifier; preserve the entry and resolve the specific issue. |

A DOI resolving successfully cannot override a conflicting title. Missing records, outages, and lack of a Crossref registration do not prove fabrication. Full author order and organizational authors matter. Name-format differences can require manual review even when they identify the same person.

Fetching BibTeX does not trigger heuristic fallback generation. If retrieval fails, obtain an authoritative record or preserve a clearly identified missing field. Avoid merging a preprint's evidence with a journal version's metadata without checking the versions.

## Integrate with the manuscript

Read the relevant passage, figure, or theorem and record its location and supporting scope. Distinguish bibliographic existence, metadata agreement, and actual support for the cited statement.

Use the manuscript's bibliography backend and venue style. Preserve complete author metadata; let the style handle display truncation. Renaming keys requires a mapping and updates to all affected references. Software, datasets, and websites need their own version, creator, identifier, URL, and access information as applicable. Submission-specific formatting follows current official requirements.

The source workflow's fixed venue-ranking database and generic citation-style formatter were not carried over: the writing skill uses task-specific source selection and the project's actual bibliography style.

BibTeX retrieval tries the DOI resolver and then the official Crossref transform endpoint once if retrieval fails. It preserves the returned entry and records the successful endpoint. See [Crossref content negotiation](https://www.crossref.org/documentation/retrieve-metadata/content-negotiation/).
