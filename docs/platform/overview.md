# Platform overview

Veytrix is an OT Asset & Security Intelligence platform in development. It is designed to discover assets passively, explain the evidence behind their identity, and show how they relate to networks, sites, protocols, and security context.

## Product family

- **Veytrix Sensor** observes site-local mirrored traffic and interprets industrial protocols. Planned active identity reads are controlled at the site.
- **Veytrix Central** coordinates fleet inventory, policy, and sensor health.
- **Veytrix Intelligence** reconciles observations into evidence-backed assets and relationships.
- **Veytrix Integrations** connects approved log and external inventory sources over time.

## Why evidence matters

One device can have several interfaces, changing IP addresses, and conflicting source descriptions. Veytrix's design treats a source observation as evidence rather than automatically promoting it to a fact. Identity matching prefers stable identifiers in site context, records confidence and source, and surfaces ambiguous cases for review.

Kibana continues to serve SOC event search and investigation. The Veytrix experience focuses on asset identity, topology, and provenance. The [delivery roadmap](roadmap.md) distinguishes the first product milestones from later integration and active-identification work.
