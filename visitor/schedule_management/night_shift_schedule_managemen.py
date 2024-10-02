from schedule_management_visitor import ScheduleManagementVisitor
from schedule_management import ScheduleManagement

class NightShiftScheduleManagement(ScheduleManagement):

    def generate_report(self):
        print("Generating report for night shift...")

    def calculate_over_time(self):
        print("Calculating over time for night shift...")

    def accept(self, schedule_management_visitor: ScheduleManagementVisitor):
        schedule_management_visitor.visit_night_shift(self)
