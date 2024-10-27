from task_state import TaskState
from todo_task_state import TodoTaskState

class BacklogTaskState(TaskState):
    def __init__(self, project_management):
        self._project_management = project_management

    def pickup_task(self, assigned_user, task):
        print(f"Task: {task.name} is being asigned to {assigned_user.email}")
        self._project_management.change_state(TodoTaskState(self._project_management))

    def process_task(self, task):
        print(f"Task: {task.name} cannot be processed until it's assigned to someone")

    def block_task(self, task, reason):
        print(f"Task: {task.name} cannot be blocked because it's still in the backlog")

    def review_task(self, task, reviewer):
        print(f"Task: {task.name} cannot be reviewed because it's still in the backlog")

    def finish_task(self, task):
        print(f"Task: {task.name} cannot be finished because it's still in the backlog")