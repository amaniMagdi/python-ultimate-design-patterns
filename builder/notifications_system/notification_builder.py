from abc import ABC, abstractmethod

class NotificationBuilder(ABC):
    @abstractmethod
    def set_content(self, content: str):
        pass

    @abstractmethod
    def set_sender(self, sender: str):
        pass

    @abstractmethod
    def set_recipient(self, recipient: str):
        pass

    @abstractmethod
    def set_timestamp(self, timestamp: str):
        pass