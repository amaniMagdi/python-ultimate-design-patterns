from subscriber import Subscriber

class Customer(Subscriber):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def notify(self, message):
        print(f"Notifying user: {self.name}, about {message}")