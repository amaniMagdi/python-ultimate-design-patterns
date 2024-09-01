from payment_strategy import PaymentStrategy

class Checkout:
    def __init__(self, payment_strategy: PaymentStrategy):
        self._payment_strategy = payment_strategy

    def process_payment(self, amount: float) -> None:
        self._payment_strategy.process_payment(amount)
