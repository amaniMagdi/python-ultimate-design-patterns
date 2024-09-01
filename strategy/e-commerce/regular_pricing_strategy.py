from pricing_strategy import PricingStrategy

class RegularPricingStrategy(PricingStrategy):

    def calculate_price(self, price: float) -> float:
        return price 