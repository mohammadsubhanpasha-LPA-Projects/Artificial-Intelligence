"""
Grounded Answer Generator.
"""
from typing import List, Dict, Any

class GroundedGenerator:
    """Generates answers based on retrieved context."""
    
    def generate(self, query: str, context: List[Dict[str, Any]]) -> str:
        """
        Generate a response citing sources.
        """
        if not context:
            return "I don't know from current knowledge base. Information not available in entangled memory."
            
        # Example formatting with citation
        sources = ", ".join([f"[{doc.get('doc_id', 'unknown')}]" for doc in context])
        return f"Based on the context, the answer is... Sources: {sources}"
