from abc import ABC, abstractmethod

class ScheduleManagement(ABC):
    @abstractmethod
    def generate_report(self):
        pass
    @abstractmethod    
    def calculate_over_time(self):
        pass
    @abstractmethod
    def accept(self, schedule_management_visitor):
        pass
