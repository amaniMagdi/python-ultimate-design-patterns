from payment_method import PaymentMethod

class MasterCard(PaymentMethod):
    def __init__(self, card_number, cvv, expiry_date, card_holder):
        super().__init__(card_number, cvv, expiry_date, card_holder)

    def authorize(self):
        print("Authorizing master card...")

    def start_money_transfer(self):
        print("Start money transferring for a master card...")

    def calculate_payment_fees(self):
        print("Calculating master card payment fees...")