from pricing_strategy import PricingStrategy

class GoldPricingStrategy(PricingStrategy):

    def calculate_price(self, price: float) -> float:
        return price * 0.9 # 10% discount