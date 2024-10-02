from abc import ABC, abstractmethod
from schedule_management import ScheduleManagement

class ScheduleManagementVisitor(ABC):

    @abstractmethod
    def visit_day_shift(self, day_shift_schedule_management: ScheduleManagement):
        pass

    @abstractmethod
    def visit_night_shift(self, night_shift_schedule_management: ScheduleManagement):
        pass

    @abstractmethod
    def visit_remote_work_shift(self, remote_work_shift_schedule_management: ScheduleManagement):
        pass