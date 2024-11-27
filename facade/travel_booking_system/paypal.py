from payment_method import PaymentMethod

class Paypal(PaymentMethod):
    def get_type(self) -> str:
        return "Paypal"
