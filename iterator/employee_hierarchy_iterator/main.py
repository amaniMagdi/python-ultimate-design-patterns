from employee_hierarchy_collection import EmployeeHierarchyCollection
def main():
    hierarchy = EmployeeHierarchyCollection("123")

    print("Direct Reports:")
    direct_report_iterator = hierarchy.create_employee_direct_report_iterator()
    while direct_report_iterator.has_next():
        employee = direct_report_iterator.get_next()
        print(f"Employee ID: {employee._id}, Name: {employee._name}")

    print("\nCoworkers:")
    coworker_iterator = hierarchy.create_employee_co_worker_iterator()
    while coworker_iterator.has_next():
        employee = coworker_iterator.get_next()
        print(f"Employee ID: {employee._id}, Name: {employee._name}")

    print("\nSubordinates:")
    subordinate_iterator = hierarchy.create_employee_sub_ordinate_iterator()
    while subordinate_iterator.has_next():
        employee = subordinate_iterator.get_next()
        print(f"Employee ID: {employee._id}, Name: {employee._name}")


if __name__ == "__main__":
    main()