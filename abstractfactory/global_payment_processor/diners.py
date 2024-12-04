from local_payment_method import LocalPaymentMethod

class Diners(LocalPaymentMethod):
    def __init__(self, card_number, cvv, expiry_date, card_holder):
        super().__init__(card_number, cvv, expiry_date, card_holder)

    def authorize(self):
        print("Authorizing Diners...")

    def start_money_transfer(self):
        print("Start money transferring for Diners...")

    def calculate_payment_fees(self):
        print("Calculating Diners payment fees...")