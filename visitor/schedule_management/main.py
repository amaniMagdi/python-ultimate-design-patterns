from day_shift_schedule_management import DayShiftScheduleManagement
from night_shift_schedule_managemen import NightShiftScheduleManagement
from remote_work_shift_schedule_managemen import RemoteWorkShiftScheduleManagement
from manage_leave_request_visitor import ManageLeaveRequestVisitor
from calculate_bonus_visitor import CalculateBonusVisitor

def main():
    schedule_management_list = [
        DayShiftScheduleManagement(),
        NightShiftScheduleManagement(),
        RemoteWorkShiftScheduleManagement()
    ]

    for schedule_management in schedule_management_list:
        schedule_management.accept(ManageLeaveRequestVisitor())
        schedule_management.accept(CalculateBonusVisitor())

if __name__ == "__main__":
    main()