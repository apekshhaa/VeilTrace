from engine.investigation_manager import InvestigationManager
from models.evidence import Evidence
from scanners.runner import run_scan
class ScannerService:

    def __init__(self):
        self.investigation_manager = InvestigationManager()

    def execute_scan(self, module: str, target: str):

        if run_scan is None:
            raise RuntimeError(
                "Scanner framework not integrated yet."
            )

        result = run_scan(module, target)
        current = self.investigation_manager.investigation_service.get()
        for finding in result["findings"]:
            evidence = Evidence(**finding)
            if current:
                evidence.investigation_id = current.id
            self.investigation_manager.receive_evidence(evidence)

        return result