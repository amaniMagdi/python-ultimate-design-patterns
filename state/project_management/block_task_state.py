from task_state import TaskState

class BlockTaskState(TaskState):
    def __init__(self, project_management):
        self._project_management = project_management

    def pickup_task(self, assigned_user, task):
        print(f"Task: {task.name} is already asigned to {assigned_user.email}")

    def process_task(self, task):
        print(f"Task: {task.name} cannot be processed because it's blocked")

    def block_task(self, task, reason):
        print(f"Task: {task.name} is already blocked")

    def review_task(self, task, reviewer):
        print(f"Task: {task.name} cannot be reviewed because it's blocked")

    def finish_task(self, task):
        print(f"Task: {task.name} cannot be finished because it's blocked")