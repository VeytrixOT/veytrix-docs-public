# Repository map

Veytrix uses separate repositories so the site software, platform, contracts, integrations, and deployment tooling can evolve on their own schedules.

| Repository | Purpose |
| --- | --- |
| [veytrix-schemas](https://github.com/VeytrixOT/veytrix-schemas) | Versioned event, evidence, asset, job, and API contracts. |
| [veytrix-plugin-sdk](https://github.com/VeytrixOT/veytrix-plugin-sdk) | Shared plugin interfaces and validation. |
| [veytrix-sensor](https://github.com/VeytrixOT/veytrix-sensor) | Site-local collection, processing, and outbound delivery. |
| [veytrix-plugins-passive](https://github.com/VeytrixOT/veytrix-plugins-passive) | Passive fingerprinting and protocol interpretation. |
| [veytrix-plugins-active](https://github.com/VeytrixOT/veytrix-plugins-active) | Controlled device identity capabilities (future phase). |
| [veytrix-central](https://github.com/VeytrixOT/veytrix-central) | Central APIs, policy, jobs, and asset management. |
| [veytrix-web](https://github.com/VeytrixOT/veytrix-web) | Asset, topology, and fleet UI. |
| [veytrix-integrations](https://github.com/VeytrixOT/veytrix-integrations) | Source-specific external adapters. |
| [veytrix-infrastructure](https://github.com/VeytrixOT/veytrix-infrastructure) | Local and deployment automation. |
| `veytrix-docs` | Private design and engineering documentation. |
| [veytrix-docs-public](https://github.com/VeytrixOT/veytrix-docs-public) | This public site. |

Most implementation repositories are private during early development. Repository links do not imply that a capability is released or publicly accessible.
