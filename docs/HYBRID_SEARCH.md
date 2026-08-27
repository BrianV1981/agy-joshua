# MCP Native Hybrid Search Engine

This document details the mechanics of the RAG 5.21 retrieval engine. In the Antigravity OS environment, agents do not construct complex Bash vector commands; they interface seamlessly with LanceDB via the Model Context Protocol (MCP).

## 1. The MCP Interface
The `mcp_servers/lancedb_mcp.py` script exposes a native `search_lancedb(query: str, limit: int = 5)` tool to the agent.
Because LanceDB stores the embedding model configuration directly inside its table metadata, the MCP server automatically invokes the appropriate embedding model (e.g., Ollama's `nomic-embed-text`) dynamically when the tool is called.

## 2. Dynamic Embedding & FTS Fallback
When an agent submits a natural language query via the MCP tool:
1.  **Native Vectorization:** LanceDB reaches out to the local Ollama instance at `localhost:11434` and vectorizes the query string in real-time.
2.  **Hybrid Routing:** The backend attempts to fire a semantic vector query against the `./memory_lance/datajacks` table. 
3.  **FTS Fallback:** If the query fails to vectorize (e.g., the Ollama service is down, or vectors were not properly ingested), the `lancedb_mcp.py` script automatically catches the exception and falls back to a pure Tantivy Full-Text Search (FTS) index. This guarantees the agent never experiences a hard crash during retrieval.

## 3. Context Stitching (The Results)
The MCP server intercepts the top `k` hits from the database and stitches them into a highly readable Markdown response for the agent.
*   Results are separated by delimiter tags `---`.
*   Agents use this returned context natively to bypass "Entity Blindness" and solve complex architectural issues without hallucinating.