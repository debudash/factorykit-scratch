# Scratch repo for FactoryKit Step 0
Run tests with: python -m unittest discover -s tests
Standards: standard library only; every function has a unit test.

<!-- factorykit:rules:begin -->
## FactoryKit

This repo is delivered with FactoryKit. Read `docs/agents/factory.md` before any build, fix or review; its settings and rules apply to every agent.

- Planning output (ADRs, glossary, HLD, LLD) goes through a docs PR on a `docs/spec-<issue#>` branch, never straight to `main`.
- Every PR description starts with `Closes #N` and the trace block.
- Post any decision the owner gives in chat on the PR as "Decision by @debudash: ..." before acting on it.
- Builders push only their own branch, never push `main`, never merge, never force-push, and print `NEEDS_DECISION: <question and options>` instead of guessing.
<!-- factorykit:rules:end -->

## Agent skills

### Issue tracker

Issues live in GitHub Issues on `debudash/factorykit-scratch`, managed with the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Triage labels

Uses the five default labels: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `GLOSSARY.md` and `docs/adr/` at the repo root. See `docs/agents/domain.md`.
