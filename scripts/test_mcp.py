import sys
import os

# Add parent directory to path so we can import mcp.lancedb_mcp
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mcp_servers.lancedb_mcp import search_lancedb

def run_test():
    print("Testing local LanceDB MCP tool...")
    
    # Query something that we know is in the docs (e.g. Sovereign Node, Blackbox Vault)
    query = "What is the Sovereign Node architecture and how does the memory isolation work?"
    print(f"Query: '{query}'\n")
    
    result = search_lancedb(query, limit=2)
    print("--- RAG RESULTS ---")
    print(result)

if __name__ == "__main__":
    run_test()
