from pricing_strategy import PricingStrategy

class Product:
    def __init__(self, name: str, price: float, pricing_strategy: PricingStrategy):
        self._name = name
        self._price = price
        self._pricing_strategy = pricing_strategy

    def calculate_price(self) -> float:
        return self._pricing_strategy.calculate_price(self._price)
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name) -> None:
        self._name = name
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, price) -> None:
        self._price = price
    