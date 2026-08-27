# A.I.M. Protocol: LanceDB MCP Server Integration (RAG 5.21)

## Overview
This protocol defines the standard architecture for querying massive external conversational datasets and documentation (e.g., the full Python Standard Library) using LanceDB. 
To achieve true **Sovereign Node Multi-Tenant Isolation**, the LanceDB database is strictly air-gapped per workspace and bridged to the Antigravity IDE via a local Model Context Protocol (MCP) Server.

## The Sovereign Node Architecture

To prevent context contamination and ensure project privacy, LanceDB is NOT installed globally. Each repository acts as its own Sovereign Node.

### 1. Embedded Local Memory (`./memory_lance`)
When a repository is initialized via the `init-workspace.ps1` script, an empty `./memory_lance` folder is created. This folder is the localized vector database. The Datajacks inside this folder never leak to other projects on your machine. The database travels with the Git repository.

### 2. The Localized MCP Server (`mcp/lancedb_mcp.py`)
The server script is injected directly into the repository. It uses the FastMCP Python framework and is hardcoded to connect ONLY to the `./memory_lance` folder. 
Because the script uses `uv` inline metadata (`/// script`), all dependencies (`mcp`, `lancedb`) are resolved dynamically without requiring you to manually manage a virtual environment.

### 3. Workspace Plugin Injection
The MCP server is registered via `.agents/plugins/lancedb/mcp_config.json`. This means the Antigravity IDE natively detects and boots the server **only** when you open this specific workspace.
The `search_lancedb` tool is automatically injected into the agent's context window.

## Usage
When the Operator asks a factual question about an external framework, the agent's first instinct MUST be to call the `search_lancedb` tool natively. 

## The Datajack Ingestion Pipeline
To feed this local database, follow the ingestion mechanics:
1. **Multimodal Flattening:** Extract text from external docs.
2. **Format Shifting:** Shatter LLM memorization n-grams.
3. **Length-Constrained Accumulator:** Chunk at 500-1,500 characters.
4. **Native PyArrow Ingestion:** Write embeddings directly to the localized `./memory_lance` folder.
