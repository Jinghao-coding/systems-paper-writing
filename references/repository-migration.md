# Repository consolidation

Date: 2026-10-05. Source: `Jinghao-coding/system-paper-skill`, commit `39fdb764f0fca8108fe3ef67cbdd1e088505554d` (MIT).

The predecessor focused on paper discovery and venue routing. This repository focuses on systems-paper writing and includes the reference functions that support that workflow.

| Predecessor capability | Decision in this repository |
| --- | --- |
| Topic and venue search URLs | Retained as offline `reference_tools.py links`, with explicit user-selected venue strings. |
| Candidate paper retrieval | Reduced to transparent Crossref candidate search and direct links to other search services. |
| DOI metadata retrieval | Retained as `lookup`; preserves ordered and organizational authors. |
| BibTeX retrieval | Retained as DOI content negotiation with source information; no guessed fallback entries. |
| Metadata verification | Reworked to distinguish agreement, conflicts, missing fields, and lookup failures; claim support requires reading. |
| Fixed A/B venue rankings and keyword scoring | Omitted; select literature for the actual research problem and verify current venue requirements. |
| Generic IEEE/APA string formatter | Omitted; use the manuscript's actual bibliography backend and style. |
| Shell wrapper and process-chain orchestration | Replaced by a single Python CLI with explicit subcommands. |
| Bytecode caches and old smoke-test outputs | Omitted; deterministic tests live in `tests/`. |

The new metadata checker does not equate DOI existence with complete correctness, silently accept a title mismatch, reorder authors, or generate a paper record from missing facts. Title searches produce candidates rather than automatic matches.

The predecessor's exact MIT license is preserved under [licenses](../licenses/system-paper-skill-MIT.txt). This document records the migration boundary and does not make the writing skill depend on the old repository.
