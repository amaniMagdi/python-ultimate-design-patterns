from abc import ABC, abstractmethod

class OrganizationUnit(ABC):
    @abstractmethod
    def calculate_total_salary(self) -> float:
        pass