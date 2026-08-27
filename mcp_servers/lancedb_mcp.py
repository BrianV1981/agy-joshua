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

# Hardcoded to the local workspace's air-gapped memory pool
LOCAL_DB_PATH = "./memory_lance"

@mcp.tool()
def search_lancedb(query: str, limit: int = 5) -> str:
    """
    Searches the localized LanceDB vector store for the given query.
    Use this tool to retrieve massive external documentation injected into this specific workspace's Datajacks.
    """
    if not os.path.exists(LOCAL_DB_PATH):
        return f"Error: Local database '{LOCAL_DB_PATH}' does not exist in this workspace. No Datajacks have been ingested here yet."
        
    try:
        # Connect to the local, tenant-specific database
        db = lancedb.connect(LOCAL_DB_PATH)
        
        # We assume the user has a table named 'datajacks' or we search all tables.
        # For this skeleton, we assume 'datajacks' is the primary table.
        table_names = db.table_names()
        if not table_names:
            return "Error: Database exists but contains no tables."
            
        # Default to the first available table if 'datajacks' doesn't exist
        target_table = "datajacks" if "datajacks" in table_names else table_names[0]
        table = db.open_table(target_table)
        
        # Execute the native hybrid/FTS search (Requires a vector or FTS index)
        # Using a simple FTS search as a fallback if vector embeddings aren't passed
        results = table.search(query, query_type="fts").limit(limit).to_list()
        
        if not results:
            return f"No relevant data found for '{query}' in {target_table}."
            
        formatted_results = []
        for r in results:
            # Assuming 'text' or 'content' is the primary column
            content = r.get("content", r.get("text", str(r)))
            formatted_results.append(f"---\n{content}\n")
            
        return "\n".join(formatted_results)
        
    except Exception as e:
        return f"Error executing native LanceDB search: {str(e)}"

if __name__ == "__main__":
    # Start the standard input/output MCP server loop
    mcp.run()
