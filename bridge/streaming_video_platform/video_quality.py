from abc import ABC, abstractmethod

class VideoQuality(ABC):

    @abstractmethod
    def render(self):
        pass
