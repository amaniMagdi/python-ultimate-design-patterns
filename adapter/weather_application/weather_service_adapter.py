from abc import ABC, abstractmethod

class WeatherServiceAdapter(ABC):
    @abstractmethod
    def get_temperature(self, longitude: float, latitude: float):
        pass