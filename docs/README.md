# A.I.M. Operating System Protocols (`docs/`)

This directory contains the highly distilled, operational markdown files that define the A.I.M. architecture and behavioral guardrails for the **Antigravity IDE** environment.

## 🟢 AUTO-INGESTION ARCHITECTURE
Unlike the legacy Linux OS that required manual `aim bake` commands to compile these docs into a LanceDB Parquet cartridge, **this folder is natively managed by the Antigravity KI System**.
Any modifications, additions, or deletions in this directory are automatically chunked, embedded, and indexed by the IDE into its internal Vector Database in real-time.

---

## Index of Protocol Files

*   **`BLACKBOX_VAULT.md`**: Details the forensic, Operator-locked anti-tampering archive designed to prevent agents from editing their own session histories.
*   **`COGNITIVE_ARCHITECTURE.md`**: Maps the flow of data through the system, identifying the Context Window, Continuity Pulse, Engram DB/Blackbox Vault, and the KI RAM / LanceDB ROM layers.
*   **`DATAJACK_SWARM.md`**: Outlines the knowledge sharing network for cartridges.
*   **`EUREKA_FARMING.md`**: Defines the self-optimization cycle, instructing agents on hindsight pruning and forging "sweat equity" into exportable skill cartridges.
*   **`GITOPS_DEPLOYMENT.md`**: The strict version control rules. Forbids raw git development on `main` and mandates the `aim-gitops` PowerShell workflow.
*   **`HANDOFF_PROTOCOL.md`**: Formalizes the handoff sequence that defeats the "Amnesia Problem," detailing the `aim-handoff` skill, Blackbox Vault sealing, and IDE native session continuations.
*   **`HYBRID_SEARCH.md`**: Details the mechanics of the LanceDB RAG engine used for searches.
*   **`LANCEDB_MCP_PROTOCOL.md`**: Explains how LanceDB is exposed natively to Antigravity IDE agents via the Model Context Protocol (MCP) server.
*   **`PERSISTENT_WIKI.md`**: Establishes the rule that Conscious Agents must use the `aim-memory-wiki` skill for Just-In-Time (JIT) synchronous maintenance of the `memory-wiki/` folder, which is auto-ingested by the KI system.
*   **`PROJECTS_KANBAN.md`**: Outlines the strict protocol for agents to claim and ship work natively on the shared GitHub Kanban board.
*   **`TESTING_AND_VALIDATION.md`**: Enforces the "TDD Reflex" and forbids "Vibe Coding." Mandates that all architectural changes must be empirically proven by automated tests before deployment.
*   **`AGENTS_AMENDMENT_PROTOCOL.md`**: Rules for updating `GEMINI.md` mandates.
*   **`HEADLESS_BOOTSTRAP_PROTOCOL.md`**: Rules for deploying sovereign agent nodes.
*   **`REMOTE_CONTROL.md`**: Operational guidelines for off-site execution and remote node command dispatching.
