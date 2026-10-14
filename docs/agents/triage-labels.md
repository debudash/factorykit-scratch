# Triage Labels

The skills speak in terms of five canonical triage roles. This file maps those roles to the actual label strings used in this repo's issue tracker.

| Label in mattpocock/skills | Label in our tracker | Meaning                                  |
| -------------------------- | -------------------- | ---------------------------------------- |
| `needs-triage`             | `needs-triage`       | Maintainer needs to evaluate this issue  |
| `needs-info`               | `needs-info`         | Waiting on reporter for more information |
| `ready-for-agent`          | `ready-for-agent`    | Fully specified, ready for an AFK agent  |
| `ready-for-human`          | `ready-for-human`    | Requires human implementation            |
| `wontfix`                  | `wontfix`            | Will not be actioned                     |

When a skill mentions a role (e.g. "apply the AFK-ready triage label"), use the corresponding label string from this table.

Edit the right-hand column to match whatever vocabulary you actually use.

<!-- factorykit:triage:begin -->
## FactoryKit

`ready-for-human`: not used. If an agent should not implement an issue, apply `needs-decision` and state why.

Two more labels sit outside the triage roles:

| Label | Meaning |
|---|---|
| `needs-decision` | A human must decide before work continues. Applied by `/triage` on issues and by the dispatcher on PRs |
| `no-dispatch` | The dispatcher ignores this PR entirely. Applied by the owner |
<!-- factorykit:triage:end -->
