"""
Orchestrator Module for Agentic Brain.
Handles tool orchestration and delegation.
"""
from typing import Any, Callable, Dict

class Orchestrator:
    """Manages the execution flow and agent delegation."""
    
    def __init__(self):
        self.tools: Dict[str, Callable] = {}
        
    def register_tool(self, name: str, func: Callable):
        """Register a tool."""
        self.tools[name] = func
        
    def execute(self, tool_name: str, *args, **kwargs) -> Any:
        """Execute a specific tool."""
        if tool_name in self.tools:
            return self.tools[tool_name](*args, **kwargs)
        raise ValueError(f"Tool {tool_name} not found.")
