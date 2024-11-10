from abc import ABC, abstractmethod

class AirTrafficControlMediator(ABC):
    @abstractmethod
    def request_takeoff(self, airplane):
        pass

    @abstractmethod
    def request_landing(self, airplane):
        pass

    @abstractmethod
    def register(self, airplane):
        pass