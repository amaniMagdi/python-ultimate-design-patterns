from schedule_management_visitor import ScheduleManagementVisitor
from schedule_management import ScheduleManagement

class DayShiftScheduleManagement(ScheduleManagement):

    def generate_report(self):
        print("Generating report for day shift...")

    def calculate_over_time(self):
        print("Calculating over time for day shift...")

    def accept(self, schedule_management_visitor: ScheduleManagementVisitor):
        schedule_management_visitor.visit_day_shift(self)
