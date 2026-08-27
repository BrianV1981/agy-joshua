# A.I.M. GitOps Deployment Rules (The Atomic Architecture)

This document defines the strict version control protocols that all A.I.M. agents must follow. To prevent autonomous agents from destroying the `main` branch or generating complex merge conflicts, A.I.M. enforces an "Atomic Deployment" architecture via the `aim-gitops` skill.

## 1. The Prime Directive
**AI agents are strictly forbidden from performing development directly on the `main` branch.** 
Every single bug fix, feature, or documentation update must be deployed immediately using isolated Git worktrees, orchestrated by the `aim-gitops` skill natively via PowerShell.

## 2. The Deployment Pipeline

### Step 1: Surgical Isolation (Spawning the Sandbox)
When assigned a task or issue, you must invoke the `aim-gitops` skill to spawn a physically isolated sandbox.
*   **Action:** The skill uses `git worktree add -b fix/issue-42 workspace/issue-42` to create a clean environment.
*   **Rule:** The agent must immediately change its working directory (`Cwd`) into the new isolated workspace folder for all subsequent tool calls before touching any code.

### Step 2: Test-Driven Development & Surgical Staging
While operating in the sandbox, agents must empirically prove their code works.
*   **TDD:** Agents must write tests and execute them in the worktree. Do not proceed to staging until tests pass.
*   **Surgical Staging:** Agents must never use `git add .` blindly. They must use `git status` and stage specific files `git add <file>` to prevent artifact pollution.

### Step 3: Atomic Release (The Teardown)
Once the code has been empirically proven to work and surgically committed, the agent must deploy it atomically.
*   **Action:** Invoke the `aim-gitops` skill to execute the teardown sequence.
*   **Rule:** The sequence safely archives the `main` branch state, merges the worktree's branch into `main`, and cleanly deletes the isolated workspace directory using native PowerShell commands.
