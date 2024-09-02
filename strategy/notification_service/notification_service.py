from notification_sending_service import NotificationSendingService
from user import User

class NotificationService:
    def __init__(self, notification_sending_service: NotificationSendingService):
        self._notification_sending_service = notification_sending_service

    def send_notification(self, user: User, message: str):
        self._notification_sending_service.send_notification(user, message)
