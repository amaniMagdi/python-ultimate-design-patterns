from card_type import CardType
from payment_method_factory import PaymentMethodFactory
from diners import Diners
from carte_bancaire import CarteBancaire
class LocalPaymentMethodFactory(PaymentMethodFactory):
    def create_payment_method(self, card_type, card_holder, card_number, cvv, expiry_date):
        if card_type == CardType.DINERS:
            return Diners(card_holder, card_number, cvv, expiry_date)
        elif card_type == CardType.CARTE_BANCAIRE:
            return CarteBancaire(card_holder, card_number, cvv, expiry_date)
        else:
            raise ValueError("Card type is not supported...")