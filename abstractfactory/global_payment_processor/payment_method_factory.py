from abc import ABC, abstractmethod

class PaymentMethodFactory(ABC):
    @abstractmethod
    def create_payment_method(self, card_type, card_holder, card_number, cvv, expiry_date):
        pass