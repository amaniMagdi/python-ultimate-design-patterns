from abc import ABC, abstractmethod
from user import User

class NotificationSendingService(ABC):
    @abstractmethod
    def send_notification(user: User, message: str) -> None:
        pass