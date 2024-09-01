from pricing_strategy import PricingStrategy

class PremiumPricingStrategy(PricingStrategy):

    def calculate_price(self, price: float) -> float:
        return price * 0.8 # 20% discount