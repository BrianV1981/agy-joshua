# The Sovereign Node Architecture

The `agy-joshua` Operating System has undergone a fundamental architectural pivot. It is no longer a terminal-based wrapper executing legacy Linux Python scripts (`aim_cli.py`, BitTorrent Swarms, etc.). It is now a native OS for the **Windows 11 Antigravity IDE**.

## 1. Multi-Tenant Air-Gapping (Sovereign Nodes)
Instead of relying on a global installation script (`./setup.sh`) and a centralized `.aim_core/` engine, A.I.M. now deploys **Sovereign Nodes** via PowerShell (`init-workspace.ps1`).
- Every initialized workspace receives its own strictly isolated `./memory_lance` vector database.
- It receives a local `.agents/plugins/lancedb/` plugin architecture ensuring zero context contamination across multiple projects on the same machine.

## 2. MCP Datajack Integration
The legacy BitTorrent P2P Cartridge swarm has been replaced by the native **Model Context Protocol (MCP)**.
- **Ingestion:** The `scripts/ingest_docs.py` script now natively utilizes a local Ollama instance (`nomic-embed-text`) and a Length-Constrained Accumulator to digest raw files directly into the air-gapped `memory_lance` folder.
- **Retrieval:** The Antigravity IDE automatically connects to the `mcp_servers/lancedb_mcp.py` server using `uv run`, exposing a `search_lancedb` tool to the agent. This seamlessly triggers hybrid LanceDB FTS/Vector queries without requiring the agent to execute complex terminal math.

## 3. Skill & UI Migration
All legacy terminal commands (e.g., `aim search`, `aim memory`, `/reincarnate`, `aim projects`) have been deprecated.
- **Progressive Skills:** Commands are now handled via Antigravity Markdown Skills (`aim-handoff`, `aim-memory-wiki`, `aim-gitops`, `aim-projects`). These skills dynamically instruct agents on how to execute standard protocols (like Git worktree isolations or GitHub CLI Kanban manipulations).
- **Clean Root:** The entire `joshua_os` directory has been purged, leaving only the essential scripts, skills, and configuration wrappers.
