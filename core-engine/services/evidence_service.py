from models.evidence import Evidence


class EvidenceService:

    def __init__(self):
        self.evidence = []

    def add_evidence(self, evidence: Evidence):
        self.evidence.append(evidence)

    def get_all_evidence(self):
        return self.evidence

    def get_by_type(self, evidence_type: str):
        return [
            e
            for e in self.evidence
            if e.type == evidence_type
        ]

    def get_by_source(self, source: str):
        return [
            e
            for e in self.evidence
            if e.source == source
        ]

    def clear(self):
        self.evidence.clear()