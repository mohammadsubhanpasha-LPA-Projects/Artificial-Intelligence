"""
Data Ingestion Loader.
"""
from typing import List, Dict

class DocumentLoader:
    """Loads documents from various sources."""
    def load(self, path: str) -> List[Dict[str, str]]:
        """Load documents from a given path."""
        return [{"doc_id": "doc_1", "text": "Sample document content."}]
