from __future__ import annotations

from .manager import ScannerManager
from .registry import ScannerRegistry


def run_scan(module: str, target: str) -> dict:
    """Run a scan through the plugin manager and return JSON results."""
    manager = ScannerManager()
    try:
        return manager.run(module, target)
    except KeyError as exc:
        return {
            "module": module,
            "status": "error",
            "error": str(exc),
            "findings": [],
        }
    except Exception as exc:
        return {
            "module": module,
            "status": "error",
            "error": str(exc),
            "findings": [],
        }
