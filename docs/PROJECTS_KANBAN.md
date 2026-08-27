# Project Management (Kanban)

## The `aim-projects` Skill
J.O.S.H.U.A. includes a native skill for the GitHub CLI (`gh project`) to manage multi-agent work streams directly via terminal commands. This allows agents to natively interface with Kanban boards without breaking workflow.
- Accessed via the `aim-projects` PowerShell skill in the Antigravity IDE.

## Agent Board Protocol
Agents must adhere to the following strict GitOps protocol to prevent collisions across parallel environments:

1. **Read the board**: Invoke the `aim-projects` skill to read the board.
   *Query the active project board to find available tasks or see active work.*
2. **Claim work**: Invoke the `aim-projects` skill to move a task to "In Progress".
   *Move the task to the "In Progress" column on the Kanban board so other agents know it is actively being worked on.*
3. **Execute**: 
   *Spawn a highly isolated Git worktree via `aim-gitops` to avoid colliding with `main`.*
4. **Ship**: 
   *Once the task is promoted to `main` via `aim-gitops`, officially close it on the Kanban board using the `aim-projects` skill.*
5. **Blocked**: 
   *If waiting on Operator input, DNS, or external dependencies, mark it as blocked using the skill.*

## Operator Prerequisites
The active GitHub CLI account (`gh auth status`) MUST have the specific project OAuth scopes to modify the board.
```powershell
gh auth refresh -h github.com -s project,read:project
```
Configuration relies on setting `AIM_PROJECTS_OWNER` and `AIM_PROJECTS_NUMBER` (and optionally `AIM_PROJECTS_REPO`) via environment variables in your Antigravity global profile.
