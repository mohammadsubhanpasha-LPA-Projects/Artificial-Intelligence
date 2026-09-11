"""
Planner Module for Agentic Brain.
Handles goal decomposition.
"""
from typing import List, Dict, Any

class Planner:
    """Decomposes high-level goals into actionable sub-tasks."""
    
    def decompose(self, goal: str) -> List[str]:
        """
        Break down a goal into sub-tasks.
        """
        return ["Analyze request", "Retrieve context", "Generate response"]
