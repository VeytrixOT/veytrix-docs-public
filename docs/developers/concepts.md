# Data and plugin concepts

The planned data model separates four concepts; implementation and released interfaces may change these descriptions. Locally tested Central service foundations now provide protected ingestion and reads, but do not yet perform discovery or reconciliation:

| Concept | Meaning |
| --- | --- |
| Observation | A versioned statement of what a parser or source saw, with time and site. |
| Evidence | An interpreted claim, tied to its observations, source, method, and confidence. |
| Canonical asset | A reconciled identity whose selected fields can be explained by evidence. |
| Relationship | A time-aware link between assets, interfaces, addresses, networks, or protocols. |

In the intended workflow, sources produce observations, interpretation adds evidence, and reconciliation would select or flag asset identity. Parsers, plugins, reconciliation and graph views remain planned; current reads can return a valid empty inventory because no discovery or reconciliation populates canonical assets yet.

Shared evidence and contract foundations exist, and Central service code has been locally tested. Phase 2 acceptance review is pending; these foundations are not a deployed or publicly available service. No wire format has been publicly released. These descriptions are conceptual and may change as the work progresses. Consult each implementation repository's README for its current status and setup.
