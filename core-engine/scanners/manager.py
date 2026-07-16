from __future__ import annotations

from .registry import ScannerRegistry
from scanners.nmap.scanner import NmapScanner


class ScannerManager:
    """Manager that routes scan requests to registered scanners."""

    def __init__(self, registry: ScannerRegistry | None = None) -> None:
        self.registry = registry or ScannerRegistry()
        self._register_default_scanners()

    def _register_default_scanners(self) -> None:
        self.registry.register("nmap", NmapScanner)

    def run(self, module: str, target: str) -> dict:
        scanner_class = self.registry.get(module)
        scanner = scanner_class()
        return scanner.run([target])
