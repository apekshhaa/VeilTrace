from typing import List, Optional, Dict, Any
import subprocess
import json
import sys
import os
import shutil

from . import parser
from .models import ScanResult


class NmapScanner:
    """
    Wrapper around the Nmap executable.
    """

    def __init__(self, nmap_path: Optional[str] = None):

        if nmap_path:
            self.nmap_path = nmap_path
        else:
            self.nmap_path = shutil.which("nmap")

            if not self.nmap_path:
                candidates = [
                    r"C:\Program Files\Nmap\nmap.exe",
                    r"C:\Program Files (x86)\Nmap\nmap.exe",
                ]

                for path in candidates:
                    if os.path.exists(path):
                        self.nmap_path = path
                        break

        if not self.nmap_path:
            raise FileNotFoundError("Nmap executable not found.")

    def run_raw(
        self,
        targets: List[str],
        extra_args: Optional[List[str]] = None,
    ) -> str:

        if not targets:
            raise ValueError("Targets list cannot be empty.")

        command = [
            self.nmap_path,
            "-sS",
            "-sV",
            "-oX",
            "-"
        ]

        if extra_args:
            command.extend(extra_args)

        command.extend(targets)

        process = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if process.returncode != 0:
            raise RuntimeError(process.stderr)

        return process.stdout

    def run(
        self,
        targets: List[str],
        extra_args: Optional[List[str]] = None,
    ) -> Dict[str, Any]:

        xml_output = self.run_raw(
            targets,
            extra_args
        )

        findings = parser.parse(xml_output)

        result = ScanResult(
            module="nmap",
            status="completed",
            findings=findings
        )

        return result.model_dump()


def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print("python -m scanners.nmap.scanner <target>")
        sys.exit(1)

    target = sys.argv[1]

    scanner = NmapScanner()

    try:
        result = scanner.run([target])

        print(
            json.dumps(
                result,
                indent=4,
                default=str
            )
        )

    except Exception as e:
        print("\nScan Failed:")
        print(str(e))


if __name__ == "__main__":
    main()