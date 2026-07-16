# Scanners

This package contains security scanner wrappers. Only the `nmap` module is implemented.

Usage example:

```py
from scanners.nmap import run

result = run(["127.0.0.1"])
print(result)
```

Notes:
- Requires the `nmap` system executable to be installed and available in `PATH`.
- The `nmap` module runs `nmap -sV -oX -` and parses XML output.
