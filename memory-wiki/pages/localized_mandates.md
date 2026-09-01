# The Decentralized Local Mandate Architecture

Prior to September 2026, J.O.S.H.U.A. installed the core `GEMINI.md` mandates into the Antigravity global configuration directory (`~/.gemini/config/rules/`). This meant all projects across the machine inherited the exact same behavior natively.

Based on Operator preference, this architecture was decentralized. The system now enforces **Zero Global Mandates**.

## How it works:
1. **Global Base (Skills Only):** `install.ps1` no longer touches rules. It exclusively installs universal tool skills (like `aim-gitops` and `aim-handoff`) to the global Antigravity `skills/` directory.
2. **Workspace Overrides (Mandates):** The `init-workspace.ps1` script (Sovereign Node initializer) now explicitly copies `GEMINI.md` into the root of the target project workspace upon initialization.

## Why the shift?
Having a monolithic global rule set made it difficult to tweak an agent's behavior for a specific project without affecting every other project on the machine. True Sovereign Nodes should have self-contained rules (their own `GEMINI.md`) just like they have self-contained memory (`memory_lance/`).
