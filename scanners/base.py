from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseScanner(ABC):
    """Abstract base class for scanner plugins."""

    @abstractmethod
    def run(self, target: str) -> Any:
        """Execute a scan against the target and return a JSON serializable result."""

    @abstractmethod
    def parse(self, raw_output: str) -> Any:
        """Parse raw scanner output into JSON-serializable findings."""

    def scan(self, target: str) -> Any:
        """Run the scanner and parse the raw output."""
        raw_output = self.run(target)
        return self.parse(raw_output)
