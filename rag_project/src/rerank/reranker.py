"""
Cross-encoder based reranker.
"""
from typing import List, Dict, Any

class Reranker:
    """Reranks retrieved documents."""
    def rerank(self, query: str, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Perform reranking."""
        return documents
