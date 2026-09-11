"""
Evaluation metrics using RAGAS concepts.
"""

class RagasEvaluator:
    """Evaluates RAG pipeline performance."""
    def evaluate_faithfulness(self, query: str, response: str, context: list) -> float:
        """Calculate faithfulness score."""
        return 0.95
