"""
Observability Module for Agentic Brain.
Handles tracing and telemetry.
"""
import time
from typing import Callable, Any

def trace_execution(func: Callable) -> Callable:
    """Decorator to trace function execution time and status."""
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            status = "success"
        except Exception as e:
            status = f"error: {str(e)}"
            raise
        finally:
            elapsed = (time.time() - start_time) * 1000
            print(f"[TRACE] {func.__name__} - {status} - {elapsed:.2f}ms")
        return result
    return wrapper
