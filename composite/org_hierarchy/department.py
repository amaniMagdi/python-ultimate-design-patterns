from organization_unit import OrganizationUnit

class Department(OrganizationUnit):
    def __init__(self):
        self._organization_units = []

    def add_organization_unit(self, organization_unit):
        self._organization_units.append(organization_unit)

    def calculate_total_salary(self) -> float:
        return sum(unit.calculate_total_salary() for unit in self._organization_units)

