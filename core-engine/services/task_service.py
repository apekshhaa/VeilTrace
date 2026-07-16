from models.task import Task


class TaskService:

    def __init__(self):

        self.tasks = []

    def create_task(
        self,
        investigation_id: str,
        module: str,
        priority: str = "MEDIUM",
    ):

        task = Task(
            investigation_id=investigation_id,
            module=module,
            priority=priority,
        )

        self.tasks.append(task)

        return task

    def get_tasks(self):

        return self.tasks

    def complete_task(self, task_id: str):

        for task in self.tasks:

            if task.id == task_id:

                task.status = "COMPLETED"

                return task

        return None