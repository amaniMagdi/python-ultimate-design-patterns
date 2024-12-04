from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def authorize(self):
        pass

    @abstractmethod
    def start_money_transfer(self):
        pass

    @abstractmethod
    def calculate_payment_fees(self):
        pass
