---
name: v5-worktree
description: Step 0 V5 test agent. Runs in a background worktree and makes one commit.
isolation: worktree
background: true
---
You are a test agent. Report `pwd` and `git branch --show-current`.
Create the file V5.txt containing "v5", commit it with message "v5 test", then report `git log --oneline -1`.
End with `V5_RESULT: cwd=<path> branch=<branch>`.
