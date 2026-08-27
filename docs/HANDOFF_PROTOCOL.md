# A.I.M. Handoff Protocols

This document formalizes the exact sequence of events that occur during an A.I.M. Handoff. This protocol exists to prevent context window bloat (the "Amnesia Problem") while preserving absolute epistemic continuity across agent lifetimes in the Antigravity IDE.

---

## The 3-Step Handoff Pipeline

When an agent's context window fills up, or a specific vessel is needed, the agent must undergo an **Agent Handoff** to start a new session (clear context) and bring the new agent up to speed with the immediate situation.

### 1. The Blackbox Vault Sealing (Immutable Truth)
Because agents natively have access to delete their own `brain/` directories, the session must be securely archived before handoff.
- **Action:** The agent must run the `aim-blackbox` skill to zip its `transcript.jsonl` and lock it into a secure, Operator-owned folder that no agent can access. This ensures an immutable forensic truth is preserved.

### 2. The `aim-handoff` Skill
The agent invokes the `aim-handoff` skill to write a highly structured `HANDOFF.md`.
- **Prerequisite:** Before initiating the handoff, the agent MUST ensure the `memory-wiki/` is up to date by synchronously running the `aim-memory-wiki` skill. *The wiki is the long-term memory; the handoff is just the short-term baton.*
- **Format:** The `HANDOFF.md` contains the tactical state, completed work, local constraints, and immediate next commands for the incoming agent.

### 3. The Baton Pass
Unlike legacy Linux environments that used `tmux` to spawn new bash sessions, Antigravity handles handoffs directly in the IDE UI.
- **Action:** The agent finalizes the `HANDOFF.md` artifact in the workspace. Crucially, the agent **creates a clickable markdown link to the `HANDOFF.md` document** in its final chat message.
- **Next Session:** This makes it easy for the Operator to copy the link and paste it into the prompt of the next agent, ensuring the incoming agent reads it automatically to gain epistemic certainty on the exact next steps.
