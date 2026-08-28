import sys
import os

# Add scripts directory to path to import ingest_docs
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))

from ingest_docs import length_constrained_accumulator

def test_length_constrained_accumulator_short():
    text = "Short text.\n\nAnother short text."
    chunks = length_constrained_accumulator(text, max_length=1500, min_length=500)
    assert len(chunks) == 1
    assert "Short text." in chunks[0]
    assert "Another short text." in chunks[0]

def test_length_constrained_accumulator_long():
    # Create a long text with multiple paragraphs
    para1 = "a" * 600
    para2 = "b" * 600
    para3 = "c" * 600
    text = f"{para1}\n\n{para2}\n\n{para3}"
    
    chunks = length_constrained_accumulator(text, max_length=1000, min_length=500)
    assert len(chunks) == 3
    assert chunks[0] == para1
    assert chunks[1] == para2
    assert chunks[2] == para3

def test_length_constrained_accumulator_empty():
    chunks = length_constrained_accumulator("", max_length=1500, min_length=500)
    assert len(chunks) == 0

def test_length_constrained_accumulator_no_newlines():
    text = "a" * 2000
    chunks = length_constrained_accumulator(text, max_length=1500, min_length=500)
    # If there are no double newlines, it just returns the whole text as one chunk
    assert len(chunks) == 1
    assert chunks[0] == text
