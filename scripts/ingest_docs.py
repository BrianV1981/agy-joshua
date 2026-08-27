# /// script
# dependencies = [
#   "lancedb",
#   "pyarrow",
#   "ollama",
#   "pandas"
# ]
# ///

import os
import glob
import lancedb
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry
import pandas as pd

# Load the Ollama embedding model natively
embed_model = get_registry().get("ollama").create(name="nomic-embed-text")

class DocumentChunk(LanceModel):
    id: str
    vector: Vector(embed_model.ndims()) = embed_model.VectorField()
    text: str = embed_model.SourceField()
    filepath: str

def length_constrained_accumulator(text, max_length=1500, min_length=500):
    """
    Chunks text by double newlines (paragraphs). Accumulates paragraphs
    until the chunk reaches the desired character threshold.
    """
    blocks = text.split("\n\n")
    chunks = []
    current_chunk = ""
    
    for block in blocks:
        block = block.strip()
        if not block:
            continue
            
        # If adding this block exceeds the max length, flush the current chunk
        if len(current_chunk) + len(block) > max_length and len(current_chunk) > min_length:
            chunks.append(current_chunk.strip())
            current_chunk = block + "\n\n"
        else:
            current_chunk += block + "\n\n"
            
    # Flush any remaining text
    if current_chunk.strip():
        chunks.append(current_chunk.strip())
        
    return chunks

import argparse

def ingest_docs(docs_dir):
    LOCAL_DB_PATH = "./memory_lance"
    
    print(f"Connecting to Local Sovereign Database at {LOCAL_DB_PATH}...")
    db = lancedb.connect(LOCAL_DB_PATH)
    
    # Create or open the 'datajacks' table
    table_name = "datajacks"
    
    docs_files = glob.glob(os.path.join(docs_dir, "**/*.md"), recursive=True)
    if not docs_files:
        print(f"No markdown files found in {docs_dir}")
        return
        
    all_chunks = []
    chunk_id = 0
    
    print(f"Processing {len(docs_files)} documentation files...")
    
    for filepath in docs_files:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
            
        print(f"  - Chunking: {os.path.basename(filepath)}")
        chunks = length_constrained_accumulator(content)
        
        for c in chunks:
            all_chunks.append({
                "id": str(chunk_id),
                "text": c,
                "filepath": filepath
            })
            chunk_id += 1
            
    print(f"Generated {len(all_chunks)} semantic chunks. Embedding and inserting into LanceDB...")
    
    # Using pandas DataFrame for bulk insertion
    df = pd.DataFrame(all_chunks)
    
    # Drop table if it exists to refresh
    if table_name in db.table_names():
        db.drop_table(table_name)
        
    table = db.create_table(table_name, schema=DocumentChunk, data=df)
    
    # Create the Tantivy FTS index for Hybrid Search
    print("Creating Tantivy Full-Text Search (FTS) index...")
    table.create_fts_index("text")
    
    print("Ingestion complete! Datajacks are fully operational.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest markdown documents into LanceDB.")
    parser.add_argument("docs_dir", nargs="?", default="./docs", help="Directory containing markdown files (default: ./docs)")
    args = parser.parse_args()
    ingest_docs(args.docs_dir)
