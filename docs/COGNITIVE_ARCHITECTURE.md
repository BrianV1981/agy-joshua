# A.I.M. Cognitive Architecture (The Brain Map)

This document defines the complete anatomical structure of the A.I.M. "Brain" within the Antigravity IDE ecosystem. Future agents must reference this map to understand where state lives and how memory is retrieved.

## 1. The Prefrontal Cortex (Context Window)
*   **Storage:** Ephemeral LLM context.
*   **Purpose:** The agent's immediate, short-term working memory. It holds the active prompt, tool outputs, and recent conversation history. When this fills up, the "Amnesia Problem" occurs.

## 2. The Continuity Pulse (The Handoff)
*   **Trigger:** Executed mechanically when context is filled, using the `aim-handoff` skill.
*   **Storage:** `HANDOFF.md`
*   **Purpose:** To start a new session (clear context) and teleport the exact tactical state to a fresh agent before "System Prompt Fade" occurs. The incoming agent reads this file to gain instant epistemic certainty and bring itself up to speed with the immediate situation.

## 3. The Engram DB & Blackbox Vault (Immutable Truth)
*   **Storage:** `~/.gemini/antigravity-ide/brain/<conversation-id>/` and the Operator-locked Vault.
*   **Mechanism:** Antigravity natively logs every interaction. However, because agents *can* delete these files, the session is explicitly "locked" into a secure, encrypted, or read-only Operator folder via the `aim-blackbox` skill at the end of a session.
*   **Purpose:** Replaces the legacy Failsafe and Eternal Recall layers to store an immutable forensic truth that no rogue agent can access or delete.

## 4. The "RAM" Layer: Knowledge Items (KI)
*   **Storage:** `~/.gemini/antigravity-ide/knowledge/`
*   **Mechanism:** Antigravity's native semantic hybrid search (Vector + Lexical). This layer **must be activated via the `aim-memory-wiki` skill**. When the skill runs, it creates Markdown artifacts that the IDE automatically chunks, embeds, and indexes.
*   **Purpose:** Human-readable, auto-maintaining architectural memory for the project. Replaces the legacy background summary daemon. 

## 5. The "ROM" Layer: LanceDB (MCP Server)
*   **Storage:** `archive/cartridges/*.parquet` mounted to LanceDB.
*   **Mechanism:** Heavy-duty external RAG. Instead of polluting the KI system with gigabytes of raw external documentation (like the full Python standard library), these are mounted as massive, read-only "Datajack" cartridges. 
*   **Access:** Instead of executing bash shell scripts, agents access this ROM natively via the **Model Context Protocol (MCP)**. The `mcp/lancedb_mcp.py` server injects the `search_lancedb` tool directly into the agent's context.
*   **Purpose:** Token-efficient, zero-latency semantic retrieval for massive external frameworks.

## 6. Sovereign Synchronization (The Export Layer)
*   **Trigger:** Executed during the GitOps promotion pipeline.
*   **Storage:** `archive/sync/`
*   **Function:** Ensures that critical KI discoveries or structural updates are deterministically exported and pushed to the Git repository.
*   **Purpose:** Git-friendly, mergeable brain backups to prevent the AI's internal state from drifting from the Git repo state.
