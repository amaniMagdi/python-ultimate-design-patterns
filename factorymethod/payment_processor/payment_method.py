from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self, card_number, cvv, expiry_date, card_holder):
        self.__card_number = card_number
        self.__cvv = cvv
        self.__expiry_date = expiry_date
        self.__card_holder = card_holder

    @abstractmethod
    def authorize(self):
        pass

    @abstractmethod
    def start_money_transfer(self):
        pass

    @abstractmethod
    def calculate_payment_fees(self):
        pass

    @property
    def card_number(self):
        return self.__card_number
    
    @card_number.setter
    def card_number(self, card_number):
        self.__card_number = card_number

    @property
    def cvv(self):
        return self.__cvv
    
    @cvv.setter
    def cvv(self, cvv):
        self.__cvv = cvv
    
    @property
    def expiry_date(self):
        return self.__expiry_date
    
    @expiry_date.setter
    def expiry_date(self, expiry_date): 
        self.__expiry_date = expiry_date

    @property
    def card_holder(self):
        return self.__card_holder
    
    @card_holder.setter
    def card_holder(self, card_holder):
        self.__card_holder = card_holder

    
