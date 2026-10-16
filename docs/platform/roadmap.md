# Delivery roadmap

Veytrix is in development. This sequence is a **plan**, not a feature availability statement. Foundation work comes first; real lab data and validation follow only when the software is ready for that checkpoint.

| Stage | Focus |
| --- | --- |
| Foundation (software acceptance complete) | Versioned contracts, a passive plugin SDK, Web foundations, and a disposable software integration path are implemented and locally tested. Actual target-host validation remains pending; this is not a released or deployed product. |
| Passive product milestone (planned) | Complete the capture-to-ingest path, then use real lab records and fresh traffic to develop and validate passive inventory and observed communications. Do not treat an empty inventory response as discovery. Examples and tests are not proof of device support or product availability. |
| Controlled active lab milestone (planned) | After passive acceptance and offline-safety checks, consider one specifically authorized, read-only lab capability. This is not permission for production OT queries. |
| Later work (planned) | Add selected log context, external integrations, and evidence-backed intelligence after prerequisites and separate scope reviews. |

The current foundations are locally tested development work, not a released or deployed product. They do not establish device support, deployed inventory, 72-hour retention, target operating-system compatibility, or production readiness. Real PCAP validation belongs to a later readiness checkpoint after required target-host validation and separate authorization; no live-device testing is implied.
