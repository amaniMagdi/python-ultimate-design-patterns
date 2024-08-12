from typing import List, Dict
from event_type import EventType
from subscriber import Subscriber
from product import Product
from offer import Offer


class OnlineMarketPlace:
    def __init__(self):
        self.subscribers: Dict[EventType, List[Subscriber]] = {}
        self.init_subscriber_events()
        self.products: List[Product] = []
        self.offers: List[Offer] = []

    def init_subscriber_events(self):
        for event_type in EventType:
            self.subscribers[event_type] = []

    def subscribe(self, event_type: EventType, subscriber: Subscriber):
        self.subscribers[event_type].append(subscriber)

    def unsubscribe(self, event_type: EventType, subscriber: Subscriber):
        self.subscribers[event_type].remove(subscriber)

    def notify_subscribers(self, event_type: EventType, message: str):
        for subscriber in self.subscribers[event_type]:
            subscriber.notify(message)

    def add_product(self, product: Product):
        self.products.append(product)
        self.notify_subscribers(EventType.NEW_PRODUCT, f"new product is added, {product.name}, with price {product.price}")

    def add_offer(self, offer: Offer):
        self.offers.append(offer)
        self.notify_subscribers(EventType.NEW_OFFER, f"new offer is added, {offer.message}")