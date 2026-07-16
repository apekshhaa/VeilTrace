from __future__ import annotations

from typing import Any, Dict, Type


class ScannerRegistry:
    """Registry for available scanner plugins."""

    def __init__(self) -> None:
        self._registry: Dict[str, Type[Any]] = {}

    def register(self, name: str, scanner: Type[Any]) -> None:
        """Register a scanner class under a name."""
        self._registry[name] = scanner

    def get(self, name: str) -> Type[Any]:
        """Retrieve a registered scanner class by name."""
        if name not in self._registry:
            raise KeyError(f"Scanner '{name}' is not registered.")
        return self._registry[name]
