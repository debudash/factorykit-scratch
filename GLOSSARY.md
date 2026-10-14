# Glossary

- **Order total**: the sum computed by `calc` for an order. Computing it is what triggers a notification.
- **Partner**: an external system that registered a URL to be told about order events.
- **Event**: one `order.totalled` message for one order and one partner. Carries an Idempotency key.
- **Idempotency key**: a UUID generated once when an event is enqueued, sent as the `Idempotency-Key` header and unchanged across retries, so partners can de-duplicate.
- **Event queue**: the in-memory queue that holds events waiting for delivery. Lost on restart (persistence is out of scope).
- **Delivery worker**: the background thread that takes events off the event queue and sends them.
- **Attempt**: one HTTP POST of an event to a partner. An event gets at most 3 attempts.
- **Backoff**: the wait between attempts: 1s after attempt 1, 2s after attempt 2.
- **Permanent failure**: a 4xx response other than 429. Not retried.
- **Dead-letter list**: the in-memory list of events that failed permanently or ran out of attempts, each with the last error.
