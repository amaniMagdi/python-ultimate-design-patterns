from schedule_management_visitor import ScheduleManagementVisitor
from schedule_management import ScheduleManagement

class RemoteWorkShiftScheduleManagement(ScheduleManagement):

    def generate_report(self):
        print("Generating report for remote work shift...")

    def calculate_over_time(self):
        print("Calculating over time for remote work shift...")

    def accept(self, schedule_management_visitor: ScheduleManagementVisitor):
        schedule_management_visitor.visit_remote_work_shift(self)
