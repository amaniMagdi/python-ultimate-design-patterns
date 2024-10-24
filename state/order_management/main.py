from order import Order
from order_management import OrderManagement

def main():
    order = Order("Laptop", 1500)
    order_management = OrderManagement(order)
    order_management.process_order()
    order_management.ship_order()
    order_management.deliver_order()
    order_management.cancel_order()

if __name__ == "__main__":
    main()
        


    