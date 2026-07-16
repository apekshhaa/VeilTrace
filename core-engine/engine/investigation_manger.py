from services.investigation_service import InvestigationService
from services.evidence_service import EvidenceService


class InvestigationManager:

    def __init__(self):
        self.investigation_service = InvestigationService()
        self.evidence_service = EvidenceService()

    def start(self, name: str, target: str):
        return self.investigation_service.start(name, target)

    def receive_evidence(self, evidence):
        self.evidence_service.add_evidence(evidence)

    def get_evidence(self):
        return self.evidence_service.get_all_evidence()