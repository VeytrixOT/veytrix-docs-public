# How Veytrix is designed to work

1. **Observe at the site.** A sensor receives SPAN/TAP traffic. Zeek and industrial parsers turn sessions into normalized observations; passive plugins interpret protocol identifiers and behavior.
2. **Preserve evidence.** Each identity claim retains its source, method, time, and confidence. A device's IP address is supporting evidence, never sufficient identity by itself.
3. **Correlate centrally.** Central receives site-originated data over an outbound authenticated connection, reconciles asset identities, and projects condensed relationships. The sensor queues important evidence when Central is unavailable.
4. **Add context.** Selected Cribl-routed logs in Elastic can contribute time-aware context. Kibana remains the SOC search and alert interface; Veytrix provides the asset and relationship view.

## Controlled operations

Future active identification is designed around named, narrow capabilities such as reading a device identity. Central may request one, but site-local policy and runtime limits must authorize and enforce it. Generic remote shell and unrestricted scanning are outside the product's initial scope.

## Future integrations

External tools can contribute records and claims through source-specific adapters. Matching and reconciliation happen before those claims alter a canonical asset. The first product milestones do not depend on those connectors being available.
