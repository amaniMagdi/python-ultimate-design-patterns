from payment_method_options import PaymentMethodOptions
from visa_card import VisaCard
from master_card import MasterCard
from paypal import Paypal


class PaymentMethodFactory:
    def create_payment_method_of(self, payment_method: str):
        if payment_method.upper() == PaymentMethodOptions.VISA.name:
            return VisaCard()
        elif payment_method.upper() == PaymentMethodOptions.MASTER_CARD.name:
            return MasterCard()
        elif payment_method.upper() == PaymentMethodOptions.PAYPAL.name:
            return Paypal()
        else:
            raise ValueError("Card type is not supported") 