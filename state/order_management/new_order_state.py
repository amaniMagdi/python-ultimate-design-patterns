from order_state import OrderState
from processing_order_state import ProcessingOrderState

class NewOrderState(OrderState):
    def __init__(self, order_management):
        self._order_management = order_management

    def process_order(self):
        print(f"Order: {self._order_management.get_order().name} is being processed now...")
        self._order_management.change_state(ProcessingOrderState(self._order_management))

    def ship_order(self):
        print(f"Cannot ship the order: {self._order_management.get_order().name} at the current state...")

    def deliver_order(self):
        print(f"Cannot deliver the order: {self._order_management.get_order().name} at the current state...")

    def cancel_order(self):
        print(f"Cancelling order: {self._order_management.get_order().name}")