from user import User
from notification_service import NotificationService
from sms_notification_service import SMSNotificationService
from email_notification_service import EmailNotificationService

def main():
    hala = User("hala@yahoo.com", "023659745")
    sms_notification = NotificationService(SMSNotificationService()) # Dependency Inversion Principle
    email_notification = NotificationService(EmailNotificationService()) # Dependency Inversion Principle

    sms_notification.send_notification(hala, "welcome dear, ")
    email_notification.send_notification(hala, "welcome dear, ")

if __name__ == "__main__":
    main()