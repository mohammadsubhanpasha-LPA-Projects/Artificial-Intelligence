"""
Embedder Module.
"""
from typing import List
import numpy as np

class Embedder:
    """Generates dense embeddings for text."""
    def embed(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings."""
        return [np.random.rand(768).tolist() for _ in texts]
