from employee_hierarchy_iterator import EmployeeHierarchyIterator

class EmployeeDirectReportIterator(EmployeeHierarchyIterator):
    def __init__(self, employee_hierarchy_collection):
        self._employee_hierarchy_collection = employee_hierarchy_collection
        self._current_direct_report_position = 0

    def has_next(self):
        return self._current_direct_report_position < len(self._employee_hierarchy_collection.get_employees())

    def get_next(self):
        print("Iterating through a graph DFS / BFS")
        if not self.has_next():
            return None
        employee = self._employee_hierarchy_collection.get_employees()[self._current_direct_report_position]
        self._current_direct_report_position +=1
        return employee