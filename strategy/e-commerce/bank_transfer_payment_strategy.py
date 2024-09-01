from payment_strategy import PaymentStrategy

class BankTransferPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount: float) -> None:
        print("Processing payment of bank transfer...")
