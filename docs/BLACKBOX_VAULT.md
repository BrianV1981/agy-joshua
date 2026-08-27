# A.I.M. Blackbox Vault Protocol

This document outlines the strict mechanism for preserving an immutable, forensic audit trail of every autonomous agent session. While the Antigravity IDE natively logs transcripts to the `brain/` directory, these directories are fully accessible and mutable by the active agent. 

To prevent a compromised or failing agent from erasing its own history, A.I.M. enforces the Blackbox Vault protocol.

## 1. The Immutable Truth
The Blackbox Vault is an Operator-owned, read-only directory located outside of the agent's typical workspace and scratch areas (e.g., an Administrator-locked folder on Windows). Agents are strictly forbidden from modifying or deleting files within this directory.

## 2. The Sealing Protocol
Before an agent completes a mission or executes a Handoff, it MUST securely seal its session transcript into the Blackbox Vault.

1. **Locate the Transcript:** The agent locates its current `transcript.jsonl` within its active `~/.gemini/antigravity-ide/brain/<conversation-id>/.system_generated/logs/` directory.
2. **Execute the Sealing Skill:** The agent executes the `aim-blackbox` skill.
3. **The Vaulting Action:** The skill compresses the JSONL transcript into a timestamped `.zip` file and moves it directly into the Operator-locked Vault directory. 
4. **Epistemic Lockdown:** Once the file enters the Vault, the agent loses all permission to delete or modify the archived transcript. 

This guarantees a perfect, untouchable record of all tool calls and reasoning, no matter how the session ends.
