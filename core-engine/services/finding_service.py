from models.finding import Finding


class FindingService:

    def __init__(self):
        self.findings = []

    def add_finding(self, finding: Finding):
        self.findings.append(finding)

    def get_all(self):
        return self.findings

    def clear(self):
        self.findings.clear()