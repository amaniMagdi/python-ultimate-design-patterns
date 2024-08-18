from subscriber import Subscriber

class User(Subscriber):
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    def notify(self, message):
        print(f"{self.name} is receiving a message {message}")
    