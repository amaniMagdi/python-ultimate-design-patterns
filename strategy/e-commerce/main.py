from product import Product
from regular_pricing_strategy import RegularPricingStrategy
from gold_pricing_strategy import GoldPricingStrategy
from premium_pricing_strategy import PremiumPricingStrategy
from checkout import Checkout
from visa_card_payment_strategy import VisaCardPaymentStrategy
from paypal_payment_strategy import PaypalPaymentStrategy

def main():

    wallet = Product("wallet", 200.0, RegularPricingStrategy())
    wallet_price = wallet.calculate_price()
    print(wallet_price)

    jacket = Product("jacket", 100.0, GoldPricingStrategy())
    jacket_price = jacket.calculate_price()
    print(jacket_price)


    mobile = Product("mobile", 200.0, PremiumPricingStrategy())
    mobile_price = mobile.calculate_price()
    print(mobile_price)
    
    visa_card_checkout = Checkout(VisaCardPaymentStrategy())
    visa_card_checkout.process_payment(wallet_price)

    paypal_checkout = Checkout(PaypalPaymentStrategy())
    paypal_checkout.process_payment(mobile_price)

if __name__ == "__main__":
    main()