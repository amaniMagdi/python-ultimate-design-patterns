from payment_method import PaymentMethod

class VisaCard(PaymentMethod):
    def get_type(self) -> str:
        return "VisaCard"
