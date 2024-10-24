from new_order_state import NewOrderState

class OrderManagement:
    def __init__(self, order):
        self._order = order
        self._order_state = NewOrderState(self)

    def change_state(self, changed_order_state):
        self._order_state = changed_order_state

    def process_order(self):
        self._order_state.process_order()

    def ship_order(self):
        self._order_state.ship_order()

    def deliver_order(self):
        self._order_state.deliver_order()
    
    def cancel_order(self):
        self._order_state.cancel_order()

    def get_order(self):
        return self._order
    




