from payment_strategy import PaymentStrategy

class VisaCardPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount: float) -> None:
        print("Processing payment of visa cards...")
        print(f"Calculating fees of the amount {amount} for visa cards...")