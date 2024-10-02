from schedule_management_visitor import ScheduleManagementVisitor
from schedule_management import ScheduleManagement

class CalculateBonusVisitor(ScheduleManagementVisitor):

    def visit_day_shift(self, day_shift_schedule_management: ScheduleManagement):
        print("Calculating bonus for day shift...")

    def visit_night_shift(self, night_shift_schedule_management: ScheduleManagement):
        print("Calculating bonus for night shift...")

    def visit_remote_work_shift(self, remote_work_shift_schedule_management: ScheduleManagement):
        print("Calculating bonus for remote work shift...")
