from abc import ABC, abstractmethod

class VideoProvider(ABC):

    @abstractmethod
    def playback(self, video_id: str):
        pass