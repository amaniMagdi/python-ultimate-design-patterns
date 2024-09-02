from notification_sending_service import NotificationSendingService
from user import User

class SMSNotificationService(NotificationSendingService):
    def send_notification(self, user: User, message: str) -> None:
        print("Sending message: " + message + " to user's mobile: " + user.mobile)
