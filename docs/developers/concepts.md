# Data and plugin concepts

The core workflow separates four concepts:

| Concept | Meaning |
| --- | --- |
| Observation | A versioned statement of what a parser or source saw, with time and site. |
| Evidence | An interpreted claim, tied to its observations, source, method, and confidence. |
| Canonical asset | A reconciled identity whose selected fields can be explained by evidence. |
| Relationship | A time-aware link between assets, interfaces, addresses, networks, or protocols. |

Parsers produce observations. Passive fingerprint plugins produce candidate evidence. Reconciliation selects or flags asset identity; plugins do not directly overwrite canonical records. The graph is a projection of durable asset relationships, while detailed event history stays in search-oriented storage.

`veytrix-schemas` is the future source of released wire formats; the descriptions here are conceptual and may change as contracts are validated. For implementation-specific setup, consult each repository's README when its code is available.
