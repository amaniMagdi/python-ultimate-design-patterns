from abc import ABC, abstractmethod

class TaskState(ABC):
    @abstractmethod
    def pickup_task(self, assigned_user, task):
        pass

    @abstractmethod
    def process_task(self, task):
        pass

    @abstractmethod
    def block_task(self, task):
        pass

    @abstractmethod
    def review_task(self, task, user):
        pass
    
    @abstractmethod
    def finish_task(self, task):
        pass