# The Persistent LLM Wiki (Long-Term Memory)

This document outlines the mechanics of the A.I.M. Persistent Wiki within the Antigravity IDE. To prevent "Context Collapse", A.I.M. physically separates raw reference data from synthesized logic (The Wiki) using the native Knowledge Items (KI) system.

## 1. The Knowledge Items (KI) Architecture
The Wiki operates on Antigravity's native KI engine to maximize speed and semantic understanding:
*   **Vector Auto-Ingestion:** The entire `memory-wiki/` directory is purely native Markdown. When an agent creates or updates a Markdown artifact in this directory, the IDE automatically chunks, embeds, and indexes it into the local KI Vector Database.
*   **Human-Readable Vault:** Because the wiki is just a directory of Markdown files, it can be read by the Operator natively or opened in Obsidian, providing a real-time graphical representation of the project's subconscious memory.

## 2. The Golden Rule of Epistemic Certainty
A "Conscious Agent" (the agent the operator is actively using) is responsible for maintaining the wiki through the `aim-memory-wiki` skill.
*   **To Read:** Agents natively pull KI context automatically, or explicitly read the `memory-wiki/` folder natively when deep context is needed.
*   **To Write:** Agents must invoke the `aim-memory-wiki` skill to synchronously edit the files.

## 3. Just-In-Time (JIT) Memory Synthesis
Wiki maintenance is handled synchronously by the active agent using the `aim-memory-wiki` skill.
1.  **The Trigger:** The user invokes the `aim-memory-wiki` skill directly, or the agent determines a critical architectural milestone has been reached.
2.  **Synthesis:** The agent synthesizes recent context, extracting tactical takeaways and architectural changes without copying raw transcripts.
3.  **Surgical Edits:** The agent natively edits `memory-wiki/index.md`, appends an entry to `memory-wiki/log.md`, and surgically modifies or creates markdown files in `memory-wiki/pages/` using standard file edit tools.
4.  **Automatic Indexing:** The updated wiki files are instantly ingested into the KI engine by the IDE, ensuring the AI's semantic search database always reflects the live markdown state.
