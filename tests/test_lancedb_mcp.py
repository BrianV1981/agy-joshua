import sys
import os
import json
import unittest
from unittest.mock import patch, MagicMock

# Add mcp_servers directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mcp_servers')))

from lancedb_mcp import search_lancedb, LOCAL_DB_PATH

class TestLanceDBMCP(unittest.TestCase):
    @patch("lancedb_mcp.os.path.exists")
    def test_search_lancedb_no_db(self, mock_exists):
        mock_exists.return_value = False
        
        result = search_lancedb("test query")
        data = json.loads(result)
        
        self.assertEqual(data["status"], "error")
        self.assertIn("does not exist", data["message"])
        self.assertIn("telemetry", data)

    @patch("lancedb_mcp.os.path.exists")
    @patch("lancedb_mcp.lancedb.connect")
    def test_search_lancedb_no_tables(self, mock_connect, mock_exists):
        mock_exists.return_value = True
        
        mock_db = MagicMock()
        mock_db.list_tables.return_value = []
        mock_connect.return_value = mock_db
        
        result = search_lancedb("test query")
        data = json.loads(result)
        
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["message"], "Database exists but contains no tables.")

    @patch("lancedb_mcp.os.path.exists")
    @patch("lancedb_mcp.lancedb.connect")
    def test_search_lancedb_no_results(self, mock_connect, mock_exists):
        mock_exists.return_value = True
        
        mock_db = MagicMock()
        mock_db.list_tables.return_value = ["datajacks"]
        mock_table = MagicMock()
        
        # Chain mock for table.search().limit().to_list()
        mock_search = MagicMock()
        mock_limit = MagicMock()
        mock_limit.to_list.return_value = []
        mock_search.limit.return_value = mock_limit
        mock_table.search.return_value = mock_search
        
        mock_db.open_table.return_value = mock_table
        mock_connect.return_value = mock_db
        
        result = search_lancedb("test query")
        data = json.loads(result)
        
        self.assertEqual(data["status"], "empty")
        self.assertIn("No relevant data found", data["message"])

    @patch("lancedb_mcp.os.path.exists")
    @patch("lancedb_mcp.lancedb.connect")
    def test_search_lancedb_with_results(self, mock_connect, mock_exists):
        mock_exists.return_value = True
        
        mock_db = MagicMock()
        mock_db.list_tables.return_value = ["datajacks"]
        mock_table = MagicMock()
        
        mock_search = MagicMock()
        mock_limit = MagicMock()
        # Mock result containing 'text'
        mock_limit.to_list.return_value = [{"text": "Found content"}]
        mock_search.limit.return_value = mock_limit
        mock_table.search.return_value = mock_search
        
        mock_db.open_table.return_value = mock_table
        mock_connect.return_value = mock_db
        
        result = search_lancedb("test query")
        
        # It shouldn't return JSON, it should return formatted markdown string
        self.assertIn("---", result)
        self.assertIn("Found content", result)

if __name__ == "__main__":
    unittest.main()
