"""
Memory Module for Agentic Brain.
Handles conversation and semantic memory with rollback capabilities.
"""
from typing import Dict, Any, List

class Memory:
    """Memory class managing agent state, semantic, and conversation history."""
    
    def __init__(self):
        self._history: List[Dict[str, Any]] = []
        self._checkpoints: Dict[str, List[Dict[str, Any]]] = {}

    def store(self, key: str, value: Any) -> None:
        """Store an item in memory."""
        self._history.append({"key": key, "value": value})

    def retrieve(self, key: str) -> Any:
        """Retrieve an item from memory by key."""
        for item in reversed(self._history):
            if item["key"] == key:
                return item["value"]
        return None
        
    def create_checkpoint(self, checkpoint_id: str) -> None:
        """Create a checkpoint for rollback."""
        self._checkpoints[checkpoint_id] = list(self._history)

    def rollback(self, checkpoint_id: str) -> bool:
        """Rollback memory to a specific checkpoint."""
        if checkpoint_id in self._checkpoints:
            self._history = list(self._checkpoints[checkpoint_id])
            return True
        return False
