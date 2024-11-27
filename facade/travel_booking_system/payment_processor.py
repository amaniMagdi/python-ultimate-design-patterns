class PaymentProcessor:
    def process_payment(self, amount, payment_method):
        print(f"Processing the overall payment with amount: {amount} using: {payment_method.get_type()}")

