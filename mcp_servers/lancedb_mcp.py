# /// script
# dependencies = [
#   "mcp",
#   "lancedb",
#   "pyarrow",
#   "ollama"
# ]
# ///

import os
import lancedb
from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server for the Sovereign Node
mcp = FastMCP("LanceDB Sovereign Node Server")

# Dynamically resolve the workspace root relative to this script's location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_ROOT = os.path.dirname(SCRIPT_DIR)
LOCAL_DB_PATH = os.path.join(WORKSPACE_ROOT, "memory_lance")

import json

@mcp.tool()
def search_lancedb(query: str, limit: int = 5) -> str:
    """
    Searches the localized LanceDB vector store for the given query.
    Use this tool to retrieve massive external documentation injected into this specific workspace's Datajacks.
    """
    if not os.path.exists(LOCAL_DB_PATH):
        return json.dumps({
            "status": "error",
            "message": f"Local database '{LOCAL_DB_PATH}' does not exist.",
            "telemetry": {
                "workspace": WORKSPACE_ROOT,
                "db_path": LOCAL_DB_PATH,
                "remediation": "Run scripts/ingest_docs.py to initialize the database."
            }
        })
        
    try:
        # Connect to the local, tenant-specific database
        db = lancedb.connect(LOCAL_DB_PATH)
        
        # We assume the user has a table named 'datajacks' or we search all tables.
        # For this skeleton, we assume 'datajacks' is the primary table.
        table_names = db.list_tables()
        if not table_names:
            return json.dumps({
                "status": "error",
                "message": "Database exists but contains no tables.",
                "telemetry": {
                    "workspace": WORKSPACE_ROOT,
                    "db_path": LOCAL_DB_PATH,
                    "remediation": "Run scripts/ingest_docs.py to ingest documents."
                }
            })
            
        # Default to the first available table if 'datajacks' doesn't exist
        target_table = "datajacks" if "datajacks" in table_names else table_names[0]
        table = db.open_table(target_table)
        
        # Execute the native hybrid/FTS search (Requires a vector or FTS index)
        # Using a simple FTS search as a fallback if vector embeddings aren't passed
        results = table.search(query, query_type="fts").limit(limit).to_list()
        
        if not results:
            return json.dumps({
                "status": "empty",
                "message": f"No relevant data found for '{query}' in {target_table}."
            })
            
        formatted_results = []
        for r in results:
            # Assuming 'text' or 'content' is the primary column
            content = r.get("content", r.get("text", str(r)))
            formatted_results.append(f"---\n{content}\n")
            
        return "\n".join(formatted_results)
        
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": f"Error executing native LanceDB search: {str(e)}"
        })

if __name__ == "__main__":
    # Start the standard input/output MCP server loop
    mcp.run()
