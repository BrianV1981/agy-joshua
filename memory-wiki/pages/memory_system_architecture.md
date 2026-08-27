# The Three-Tier Memory Architecture

The Antigravity J.O.S.H.U.A. ecosystem separates memory into three distinct, hierarchical tiers. This design ensures that ephemeral agent thinking (scratchpads) doesn't pollute the source code, while long-term architectural lore and repository knowledge securely travel with the codebase.

## 1. The Ephemeral Session (`brain/`)
**Location:** `~/.gemini/antigravity/brain/<session-id>/`
**Scope:** Single Conversation / Single Agent Lifecycle
**Persistence:** Temporary / Ephemeral

The `brain/` directory acts as the short-term working memory for a specific agent session. It isolates the messy "thinking" process from the rest of the system.
* **`.system_generated/`**: Contains the immutable `transcript.jsonl` (the agent's internal monologue and tool calls) and logs for background tasks.
* **`.user_uploaded/`**: Files or screenshots dragged into the chat UI during this specific session.
* **`scratch/`**: Safe sandbox folders where the agent can run temporary scripts, test logic, or store temporary data without polluting the Git repository.
* **Artifacts (`.md`)**: Documents (like `HANDOFF.md` drafts or `walkthrough.md`) generated specifically to render interactive UI elements for the Operator.

*Note: Because this memory dies with the session, critical milestones must be extracted using `aim-handoff` or `aim-memory-wiki`.*

## 2. The Persistent Global Memory (`knowledge/`)
**Location:** `~/.gemini/antigravity/knowledge/`
**Scope:** Machine-Wide / Cross-Project
**Persistence:** Permanent (Local to the IDE/Machine)

This directory sits parallel to `brain/` and stores **Knowledge Items (KIs)**. KIs are real-time, dynamically chunked embeddings that the Antigravity IDE uses to learn about the Operator and their workflows across *all* projects.
* **`aim_operator_profile/`**: Preferences, operational boundaries, and facts learned about the Operator.
* **`aim_project_architecture/`**: Cross-project architectural patterns.

Because KIs are stored at this global level rather than inside a session's `brain/`, they are successfully shared across every new agent conversation and workspace you open on the machine.

## 3. The Project Sovereign Node (`workspace/`)
**Location:** Inside the Git Repository (e.g., `C:\agy-joshua\`)
**Scope:** Project-Specific / Multi-Tenant Air-Gapped
**Persistence:** Permanent (Travels with the Git codebase)

This is the repository's dedicated long-term memory. It ensures the codebase retains its own context, rules, and history independently of the Operator's local machine. If the repository is cloned by another developer, the Sovereign Node memory goes with it.
* **`memory_lance/`**: The local LanceDB vector pool. Ingests raw documentation (Datajacks) into an air-gapped database accessible via the repository's local MCP server.
* **`memory-wiki/`**: The compounding, human-readable markdown knowledge base. It tracks architectural shifts, configuration drift, and core concepts.
* **`.agents/` (or `skills/`)**: Workspace-specific agent tools, rules, and plugins that dictate how an agent must behave within this specific repository.

## The Data Lifecycle
1. An agent operates within its **Ephemeral Session (`brain/`)**, utilizing its global **Knowledge (`knowledge/`)** for context.
2. During the session, the agent queries the **Sovereign Node (`memory_lance/`)** via MCP to retrieve project-specific documentation.
3. Before the session ends, the agent uses the `aim-memory-wiki` skill to extract tactical takeaways from its `brain/` and commit them into the **Sovereign Node (`memory-wiki/`)** so the knowledge becomes permanent.
