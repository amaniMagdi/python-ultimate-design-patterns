from card_type import CardType
from visa import Visa
from master_card import MasterCard
from american_express import AmericanExpress

class PaymentMethodFactory:
    def create_payment_method(self, card_type, card_holder, card_number, cvv, expiry_date):
        if card_type == CardType.VISA:
            return Visa(card_holder, card_number, cvv, expiry_date)
        elif card_type == CardType.MASTER_CARD:
            return MasterCard(card_holder, card_number, cvv, expiry_date)
        elif card_type == CardType.AMERICAN_EXPRESS:
            return AmericanExpress(card_holder, card_number, cvv, expiry_date)
        else:
            raise ValueError("Card type is not supported...")