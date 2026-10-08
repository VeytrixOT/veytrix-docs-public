# Platform overview

Veytrix is an OT Asset & Security Intelligence platform in development. The intended product will use passive observations to build explainable asset identity and show relationships and security context. No discovery or asset platform is currently deployed.

## Product family

- **Veytrix Sensor** is planned to process site-local mirrored traffic passively; protocol coverage and device support are not yet validated.
- **Veytrix Central** is planned to coordinate asset data and sensor health.
- **Veytrix Intelligence** describes the planned evidence and identity workflow, not a currently available service.
- **Veytrix Integrations** are later planned work for selected logs and external inventory sources.

## Why evidence matters

One device can have several interfaces, changing IP addresses, and conflicting source descriptions. The design aims to explain identity claims with their evidence and preserve ambiguity rather than treating an address as identity. Matching rules and device coverage require implementation and real-data validation.

Kibana is the intended SOC event-search experience; Veytrix is planned to focus on asset identity and relationships. See the [delivery roadmap](roadmap.md) for the planned sequence and validation gates.
