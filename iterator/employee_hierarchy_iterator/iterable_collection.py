from abc import ABC, abstractmethod

class IterableCollection(ABC):
    
    @abstractmethod
    def create_employee_direct_report_iterator(self):
        pass

    @abstractmethod
    def create_employee_co_worker_iterator(self):
        pass

    @abstractmethod
    def create_employee_sub_ordinate_iterator(self):
        pass