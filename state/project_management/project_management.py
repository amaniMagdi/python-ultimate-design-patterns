from backlog_task_state import BacklogTaskState

class ProjectManagement:
    def __init__(self, task):
        self._task = task
        self.task_state = BacklogTaskState(self)

    def change_state(self, changed_task_state):
        self.task_state = changed_task_state

    def pickup_task(self, assigned_user, task):
        self.task_state.pickup_task(assigned_user, task)

    def process_task(self, task):
        self.task_state.process_task(task)

    def block_task(self, task, reason):
        self.task_state.block_task(task, reason)

    def review_task(self, task, reviewer):
        self.task_state.review_task(task, reviewer)

    def finish_task(self, task):
        self.task_state.finish_task(task)
