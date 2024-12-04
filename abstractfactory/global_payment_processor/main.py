from payment_processor import PaymentProcessor
from local_payment_method_factory import LocalPaymentMethodFactory
from international_payment_method_factory import InternationalPaymentMethodFactory
from card_type import CardType

def main():
    #local payment method factory
    payment_method_factory = LocalPaymentMethodFactory()
    payment_processor = PaymentProcessor(payment_method_factory)
    payment_processor.process_payment(CardType.DINERS, "test", "11-89-86", "789", "11-8-2025")

    #international payment method factory
    payment_method_factory = InternationalPaymentMethodFactory()
    payment_processor = PaymentProcessor(payment_method_factory)
    payment_processor.process_payment(CardType.VISA, "test2", "71-89-86", "736", "11-8-2025")

if __name__ == '__main__':
    main()