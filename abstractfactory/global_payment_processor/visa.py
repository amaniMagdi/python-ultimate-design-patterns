from international_payment_method import InternationalPaymentMethod

class Visa(InternationalPaymentMethod):
    def __init__(self, card_number, cvv, expiry_date, card_holder):
        super().__init__(card_number, cvv, expiry_date, card_holder)

    def authorize(self):
        print("Authorizing visa card...")

    def start_money_transfer(self):
        print("Start money transferring for a visa card...")

    def calculate_payment_fees(self):
        print("Calculating visa card payment fees...")