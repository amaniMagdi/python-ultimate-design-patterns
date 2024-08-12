from customer import Customer
from job_finder import JobFinder
from online_market_place import OnlineMarketPlace
from event_type import EventType
from product import Product
from offer import Offer

def main():
    marketplace = OnlineMarketPlace()

    noha = Customer("Noha")
    mona = Customer("Mona")

    marketplace.subscribe(EventType.NEW_PRODUCT, noha)
    marketplace.subscribe(EventType.NEW_OFFER, mona)


    new_product = Product("Labtop", 1500)
    marketplace.add_product(new_product)

    new_offer = Offer("50% off on all electronics!")
    marketplace.add_offer(new_offer)

if __name__ == "__main__":
    main()




