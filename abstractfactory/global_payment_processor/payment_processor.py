class PaymentProcessor:
    def __init__(self, payment_method_factory):
        # Dependency Injection of the PaymentMethodFactory
        self.__payment_method_factory = payment_method_factory

    def process_payment(self, card_type, card_holder, card_number, cvv, expiry_date):
        """
        Process the payment by creating the appropriate payment method and performing operations.
        """
        # Create the payment method using the factory
        payment_method = self.__payment_method_factory.create_payment_method(
            card_type, card_holder, card_number, cvv, expiry_date
        )

        # Perform operations on the payment method
        payment_method.authorize()
        payment_method.start_money_transfer()
        payment_method.calculate_payment_fees()
