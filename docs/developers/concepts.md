# Data and plugin concepts

The planned data model separates four concepts; implementation and released interfaces may change these descriptions. Contract, passive plugin SDK, Web foundations, and a disposable software integration path have been implemented and locally tested. Target-host validation and deployment remain in progress. These foundations are not a released service and do not provide device discovery or reconciliation:

| Concept | Meaning |
| --- | --- |
| Observation | A versioned statement of what a parser or source saw, with time and site. |
| Evidence | An interpreted claim, tied to its observations, source, method, and confidence. |
| Canonical asset | A reconciled identity whose selected fields can be explained by evidence. |
| Relationship | A time-aware link between assets, interfaces, addresses, networks, or protocols. |

In the intended workflow, sources produce observations, interpretation adds evidence, and reconciliation would select or flag asset identity. The plugin SDK foundation does not establish support for any vendor device. Parsers, device-specific plugins, reconciliation and graph views remain planned; an empty UI or inventory response does not prove discovery has occurred.

Shared contracts, passive plugin SDK, Web foundations and software integration have been locally tested. Phase 2 was approved and merged; Phase 3 software acceptance is complete, while actual target-host validation remains pending. These foundations are not released, deployed, or publicly available as a product. Real-PCAP validation follows target-host checks and separate readiness authorization. These descriptions are conceptual and may change as the work progresses. Consult each implementation repository's README for its current status and setup.
