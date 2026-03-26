"""
Telemetry decorator DISABLED — passthrough only, no data collection.
"""

import functools
import inspect
from typing import Callable, Any


def telemetry_tool(tool_name: str):
    """No-op decorator — passes through to the original function unchanged."""
    def decorator(func: Callable) -> Callable:
        return func
    return decorator
