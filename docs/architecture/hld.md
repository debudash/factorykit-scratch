# High-level design

## Context
`factorykit-scratch` is a small standard-library Python project. `src/calc.py` computes Order totals. From spec #6, Partners are told when a total is computed.

## Components and responsibilities
| Component | Responsibility |
|---|---|
| `calc` | Computes Order totals; calls the webhook API after each. |
| `webhook.api` | Public entry point `notify_order_totalled`; holds the Partner list; creates Events and enqueues them. Never blocks on the network. |
| `webhook.queue` | Event queue and Dead-letter list. |
| `webhook.worker` | Delivery worker: sends Events, applies retry and Backoff rules, dead-letters failures. |

## Data flows
`calc` -> `webhook.api` -> Event queue -> Delivery worker -> Partner endpoint (HTTP POST, JSON). Failures end in the Dead-letter list. Detail: [LLD for spec #6](lld/6-order-totalled-webhook.md).

## Deployment
Single process. The Delivery worker is a daemon thread started by the caller of `webhook.worker.start_worker`. No external services.

## Non-functional requirements
- **Reliability**: at-least-once delivery per Partner, up to 3 Attempts; nothing silently lost within a process lifetime. Events do not survive restarts (out of scope).
- **Security**: payloads are not signed (out of scope). Partner URLs are trusted configuration.
- **Performance**: `notify_order_totalled` is O(partners) and does no I/O. Attempt timeout is 5s.
