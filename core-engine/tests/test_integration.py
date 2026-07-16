from services.scanner_service import ScannerService

def test_nmap_integration():
    scanner_service = ScannerService()

    result = scanner_service.execute_scan(
        "nmap",
        "scanme.nmap.org"
    )

    print("\n===== Scan Result =====")
    print(result)

    evidence = scanner_service.investigation_manager.get_evidence()

    print("\n===== Evidence Stored =====")
    for item in evidence:
        print(item)

    assert len(evidence) > 0


if __name__ == "__main__":
    test_nmap_integration()