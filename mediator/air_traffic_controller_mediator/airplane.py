from abc import ABC, abstractmethod

class Airplane(ABC):
    @abstractmethod
    def get_type(self) -> str:
        pass

    @abstractmethod
    def request_takeoff(self):
        pass

    @abstractmethod
    def request_landing(self):
        pass

    @abstractmethod
    def notify_air_traffic_control(self, message: str):
        pass