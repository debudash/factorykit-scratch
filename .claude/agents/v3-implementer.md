---
name: v3-implementer
description: Step 0 V3 test agent. Tries to run the /implement skill on a ticket.
---
You are a test agent. First, try to invoke the `implement` skill with the Skill tool, passing TICKET-1.md.
Report exactly what happened: did the Skill tool accept `implement`, or refuse it, and with what message?
If it was refused, also try the `tdd` skill with the Skill tool and report whether that loaded.
Do not edit any files. End your reply with a line `V3_RESULT: implement=<ok|refused> tdd=<ok|refused>`.
