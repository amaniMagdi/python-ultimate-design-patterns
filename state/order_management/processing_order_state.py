from order_state import OrderState
from cancelled_order_state import CancelledOrderState
from shipped_order_state import ShippedOrderState

class ProcessingOrderState(OrderState):
    def __init__(self, order_management):
        self._order_management = order_management

    def process_order(self):
        print("The order is currently being processed!")

    def ship_order(self):
        print("Shipping the order...")
        self._order_management.change_state(ShippedOrderState(self._order_management))

    def deliver_order(self):
        print("The order cannot be delivered at the current state")

    def cancel_order(self):
        print("The order is being cancelled now...")
        self._order_management.change_state(CancelledOrderState(self._order_management))