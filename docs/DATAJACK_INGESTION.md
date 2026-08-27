# The DataJack Ingestion Protocol

This document outlines the mechanics of A.I.M.'s localized knowledge embedding pipeline. The DataJack protocol allows operators to inject massive external datasets (e.g., Python documentation, framework source code) into a project's Sovereign Node, making the information instantly accessible to agents via native MCP queries without expensive API embedding calls.

## 1. The Local Memory Pool (`memory_lance`)
A.I.M. strictly separates global OS context from project-specific knowledge:
*   **Sovereign Node Isolation:** Every workspace initialized via `init-workspace.ps1` receives its own isolated `./memory_lance` folder.
*   **Zero Contamination:** Datajacks compiled into a project remain strictly air-gapped. An agent working in a Django backend will never hallucinate vectors from a Unity C# Datajack stored in a different workspace.

## 2. Ingestion Engine (`scripts/ingest_docs.py`)
To feed the local LanceDB pool, A.I.M. utilizes a fully autonomous ingestion script that runs locally without requiring cloud APIs.

**Workflow:**
1.  **Drop Files:** Operators drop markdown or text documentation into the `docs/` folder (or designated ingestion folders).
2.  **Execute Ingestion:** Run `uv run scripts/ingest_docs.py`.
3.  **The Accumulator:** The script parses the raw files and intelligently chunks them using the **Length-Constrained Accumulator** algorithm (chunking strictly by paragraphs between 500-1500 characters to prevent cutting off semantic ideas).
4.  **Local Embeddings (Ollama):** The script natively calls your local Ollama instance (at `localhost:11434`) using the `nomic-embed-text` model to embed the text blocks.
5.  **Native PyArrow Storage:** The vectors are stored directly into the air-gapped `./memory_lance/datajacks` table as highly compressed `.parquet` files.

## 3. Retrieving the Datajacks
Once ingested, the vectors are accessed exclusively via the local MCP server (`mcp_servers/lancedb_mcp.py`). 
*   The Antigravity IDE natively mounts the local MCP server when the workspace is opened.
*   Agents use the `search_lancedb` tool to instantly retrieve the embedded context, bypassing the need for manual vector similarity math or shell script orchestration.

*(Note: The legacy BitTorrent P2P Swarm distribution protocol for Parquet cartridges was deprecated with the shift to Sovereign Nodes and local Ollama integrations).*
