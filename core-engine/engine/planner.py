from models.task import Task
class Planner:
    def create_task(
        self,
        investigation_id: str,
        module: str,
        priority: str = "MEDIUM",
    ) -> Task:
        return Task(
            investigation_id=investigation_id,
            module=module,
            priority=priority,
        )