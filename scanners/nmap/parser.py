import xml.etree.ElementTree as ET
from typing import List
import uuid
from datetime import datetime
from .models import Finding


def _get_attr(elem, name: str) -> str:
    return elem.get(name) if elem is not None else ""


def parse(xml_str: str) -> List[Finding]:
    """Parse Nmap XML and return a list of `Finding` objects.

    Extracted fields per open port:
      - host
      - port (value)
      - protocol
      - service
      - product
      - version
      - state
    """
    findings: List[Finding] = []
    try:
        root = ET.fromstring(xml_str)
    except ET.ParseError:
        return findings

    for host in root.findall("host"):
        addr_elem = host.find("address")
        host_ip = _get_attr(addr_elem, "addr")

        ports_block = host.find("ports")
        if ports_block is None:
            continue

        for port in ports_block.findall("port"):
            portid = _get_attr(port, "portid")
            protocol = _get_attr(port, "protocol")

            state_elem = port.find("state")
            state = _get_attr(state_elem, "state")
            if state != "open":
                continue

            service_elem = port.find("service")
            service = _get_attr(service_elem, "name")
            product = _get_attr(service_elem, "product")
            version = _get_attr(service_elem, "version")

            f = Finding(
                id=str(uuid.uuid4()),
                type="open_port",
                value=str(portid),
                severity="medium",
                confidence=1.0,
                source="nmap",
                timestamp=datetime.utcnow(),
                metadata={
                    "host": host_ip,
                    "protocol": protocol,
                    "service": service,
                    "product": product,
                    "version": version,
                    "state": state,
                },
            )

            findings.append(f)

    return findings
