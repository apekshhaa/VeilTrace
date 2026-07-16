from fastapi import APIRouter

from engine.investigation_manager import InvestigationManager
from models.evidence import Evidence

router = APIRouter()

manager = InvestigationManager()


@router.post("/investigation/start")
def start_investigation(name: str, target: str):
    investigation = manager.start(name, target)
    return investigation


@router.post("/investigation/evidence")
def receive_evidence(evidence: Evidence):
    manager.receive_evidence(evidence)
    return {"status": "received"}


@router.get("/investigation/evidence")
def get_evidence():
    return manager.get_evidence()