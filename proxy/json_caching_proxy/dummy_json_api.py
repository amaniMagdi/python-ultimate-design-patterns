from abc import ABC, abstractmethod

class DummyJsonApi(ABC):
    @abstractmethod
    def get_all_products(self) -> str:
        """Retrieve all products."""
        pass

    @abstractmethod
    def get_all_recipes(self) -> str:
        """Retrieve all recipes."""
        pass
