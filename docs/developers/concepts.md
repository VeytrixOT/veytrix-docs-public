# Data and plugin concepts

The planned data model separates four concepts; implementation and released interfaces may change these descriptions:

| Concept | Meaning |
| --- | --- |
| Observation | A versioned statement of what a parser or source saw, with time and site. |
| Evidence | An interpreted claim, tied to its observations, source, method, and confidence. |
| Canonical asset | A reconciled identity whose selected fields can be explained by evidence. |
| Relationship | A time-aware link between assets, interfaces, addresses, networks, or protocols. |

In the intended workflow, sources produce observations, interpretation adds evidence, and reconciliation would select or flag asset identity. These are design concepts, not currently available parsers, plugins, reconciliation services, or graph views.

Shared contract validation foundations exist, but no wire format has been released and no public product or service is available. These descriptions are conceptual and may change as the work progresses. Consult each implementation repository's README for its current status and setup.
