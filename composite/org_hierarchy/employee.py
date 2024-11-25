from organization_unit import OrganizationUnit

class Employee(OrganizationUnit):
    def __init__(self, name: str, salary: float):
        self._name = name
        self._salary = salary

    def calculate_total_salary(self) -> float:
        return self._salary
