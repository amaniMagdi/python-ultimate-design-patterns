from employee import Employee
from department import Department

def main():
    # Create employees
    employee1 = Employee("John Doe", 5000.0)
    employee2 = Employee("Jane Smith", 6000.0)

    # Create a department and add employees
    department = Department()
    department.add_organization_unit(employee1)
    department.add_organization_unit(employee2)

    # Create another department with a sub-department
    sub_department = Department()
    sub_employee = Employee("Alice Brown", 4000.0)
    sub_department.add_organization_unit(sub_employee)
    department.add_organization_unit(sub_department)

    # Calculate total salary for the main department
    print(f"Total Salary for Department: {department.calculate_total_salary()}")

if __name__ == "__main__":
    main()