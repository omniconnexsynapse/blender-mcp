"""
Telemetry DISABLED — all collection functions are no-ops.
Original telemetry sent data to Supabase. Removed for privacy.
"""


def record_tool_usage(tool_name, success, duration_ms, error=None):
    pass


def record_startup(blender_version=None):
    pass


def is_telemetry_enabled():
    return False


def get_telemetry():
    return None
