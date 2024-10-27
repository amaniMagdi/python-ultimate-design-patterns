from task_state import TaskState
from block_task_state import BlockTaskState

class TodoTaskState(TaskState):
    def __init__(self, project_management):
        self._project_management = project_management

    def pickup_task(self, assigned_user, task):
        print(f"Task: {task.name} is already asigned to {assigned_user.email}")

    def process_task(self, task):
        print(f"Task: {task.name} is beeing processing")

    def block_task(self, task, reason):
        print(f"Task: {task.name} will be blocked because: {reason}")
        self._project_management.change_state(BlockTaskState(self._project_management))

    def review_task(self, task, reviewer):
        print(f"Task: {task.name} cannot be reviewed because it's still in the processing phase")

    def finish_task(self, task):
        print(f"Task: {task.name} cannot be finished because it's still in the processing phase")