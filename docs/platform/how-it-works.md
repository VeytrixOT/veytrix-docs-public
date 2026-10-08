# How Veytrix is designed to work

The following describes the intended workflow; these components and capabilities are still in development and are not available as a deployed platform.

1. **Observe at the site (planned).** A site sensor is intended to process mirrored traffic passively. Which records and device signals are useful must be determined from real lab data; vendor coverage is not yet validated.
2. **Preserve evidence (planned).** Observations and identity claims are intended to retain their sources and uncertainty. An IP address alone is not enough to establish an asset identity.
3. **Correlate centrally (planned).** Site-originated observations are intended to support explainable asset identity and relationships. Handling interruptions and offline retention still require implementation and validation.
4. **Add context later (planned).** Existing logs and external integrations are later work, not prerequisites for the initial passive milestone.

## Controlled operations

An active identity capability may be considered only after passive acceptance and offline-safety checks, with separate authorization and lab validation. No active capability is available today.

## Future integrations

External tools may contribute records through selected adapters in a later phase. Integrations are not part of the current foundation work.
