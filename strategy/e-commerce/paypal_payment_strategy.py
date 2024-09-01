from payment_strategy import PaymentStrategy

class PaypalPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount: float) -> None:
        print("Processing payment of paypal...")
        print(f"Calculating fees of the amount {amount} for paypal...")