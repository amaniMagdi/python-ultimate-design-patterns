from payment_method import PaymentMethod

class AmericanExpress(PaymentMethod):
    def __init__(self, card_number, cvv, expiry_date, card_holder):
        super().__init__(card_number, cvv, expiry_date, card_holder)

    def authorize(self):
        print("Authorizing American Express...")

    def start_money_transfer(self):
        print("Start money transferring for American Express...")

    def calculate_payment_fees(self):
        print("Calculating American Express payment fees...")