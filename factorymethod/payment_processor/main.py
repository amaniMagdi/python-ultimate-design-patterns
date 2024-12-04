from payment_processor import PaymentProcessor
from payment_method_factory import PaymentMethodFactory
from card_type import CardType

def main():
    payment_method_factory = PaymentMethodFactory()
    payment_processor = PaymentProcessor(payment_method_factory)
    payment_processor.process_payment(CardType.VISA, "test", "11-89-86", "789", "11-8-2025")

if __name__ == '__main__':
    main()