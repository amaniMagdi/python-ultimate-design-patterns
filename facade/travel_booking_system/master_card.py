from payment_method import PaymentMethod

class MasterCard(PaymentMethod):
    def get_type(self) -> str:
        return "MasterCard"
