# 0001: Three attempts means two waits

Status: accepted (spec #6, owner accepted the recommended answer)

## Context
Spec #6 says "up to 3 attempts with backoff 1s, 2s, 4s" and defines `backoff_delays(3) == [1.0, 2.0, 4.0]`. Three attempts have only two gaps between them, so one delay is left over.

## Decision
- An event gets at most 3 attempts (the spec wording wins over "3 retries").
- The Delivery worker sleeps `delays[i]` after failed attempt `i` only when another attempt remains, so it uses 1s and 2s.
- `backoff_delays(n)` still returns `n` values as the spec defines; the last (4.0) is never slept. It exists so raising `max_attempts` later needs no helper change.

## Consequences
Worst case for one event is 3s of waiting plus up to 3 x 5s attempt timeouts. No sleep follows the final failure, so dead-lettering is immediate.
