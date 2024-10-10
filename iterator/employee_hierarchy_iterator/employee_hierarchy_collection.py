from employee import Employee
from employee_direct_report_iterator import EmployeeDirectReportIterator
from employee_co_workers_iterator import EmployeeCoWorkersIterator
from employee_subordinates_iterator import EmployeeSubOrdinatesIterator

class EmployeeHierarchyCollection:
    def __init__(self, employee_id):
        self._employees = [
            Employee("123", "Mahmoud"), 
            Employee("345", "Ahmed")
        ]
        self._employee_id = employee_id

    def get_employees(self):
        return self._employees
    
    def create_employee_direct_report_iterator(self):
        return EmployeeDirectReportIterator(self)
        
    def create_employee_co_worker_iterator(self):
        return EmployeeCoWorkersIterator(self)

    def create_employee_sub_ordinate_iterator(self):
        return EmployeeSubOrdinatesIterator(self)