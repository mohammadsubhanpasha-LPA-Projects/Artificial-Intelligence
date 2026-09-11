"""
Lexical search using BM25.
"""
from typing import List, Dict, Any

class BM25Index:
    """BM25 based lexical search index."""
    def build(self, documents: List[Dict[str, str]]):
        """Build the index."""
        pass
        
    def search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search the BM25 index."""
        return []
