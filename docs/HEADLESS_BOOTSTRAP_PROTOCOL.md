# A.I.M. Sovereign Node Bootstrap Protocol

This document outlines the standard operating procedure for installing a fresh, isolated instance of the A.I.M. OS architecture into a new project directory. 

This protocol is specifically designed for deploying **Sovereign Nodes** (multi-tenant air-gapped workspaces) natively via Windows 11 PowerShell.

## Prerequisites
Ensure the host system has:
*   Windows 11
*   PowerShell 7+
*   Antigravity IDE
*   `uv` (The ultrafast Python package installer and resolver)
*   Ollama (with the `nomic-embed-text` model pulled)

## Step-by-Step Deployment

### 1. Initialize the Sovereign Node
To grant a specific repository the A.I.M. OS architecture and an isolated RAG memory pool, execute the bootstrap installer:

```powershell
.\init-workspace.ps1 -TargetWorkspace "C:\path\to\target_project"
```

### 2. What the Installer Does
The bootstrap script executes a surgical injection of the A.I.M. architecture:
1.  **Plugin Architecture:** It creates the `.agents/plugins/lancedb/` folder inside the target project.
2.  **MCP Routing:** It injects `mcp_config.json` and the `lancedb_mcp.py` server. The config is wired to use `uv run`, eliminating the need for manual virtual environment configuration.
3.  **Memory Pool Generation:** It creates an empty `./memory_lance` folder. This is the air-gapped vector database unique to this repository.

### 3. Verification
If the deployment is successful, opening the project in the Antigravity IDE will natively boot the LanceDB MCP Server. 

You should verify the generation of the following artifacts in your target project:
- `.agents/plugins/lancedb/mcp_config.json`
- `mcp_servers/lancedb_mcp.py`
- `memory_lance/` (The empty initialized vector database)

The new A.I.M. Sovereign Node is now fully federated, completely air-gapped from other projects, and ready for Datajack ingestion and autonomous agent execution.