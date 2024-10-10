from abc import ABC, abstractmethod

class EmployeeHierarchyIterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def get_next(self):
        pass