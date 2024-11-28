from typing import List
from notification_builder import NotificationBuilder  
from messenger_notification import MessengerNotification 

class MessengerNotificationBuilder(NotificationBuilder):
    def __init__(self):
        self._content= None
        self._sender= None
        self._recipient= None
        self._timesta= None
        self._attachments= None
        self._theme= None

    def set_content(self, content: str):
        self._content = content
        return self

    def set_sender(self, sender: str):
        self._sender = sender
        return self

    def set_recipient(self, recipient: str):
        self._recipient = recipient
        return self

    def set_timestamp(self, timestamp: str):
        self._timestamp = timestamp
        return self

    def set_attachments(self, attachments: List[str]):
        self._attachments = attachments
        return self

    def set_theme(self, theme: str):
        self._theme = theme
        return self

    def build(self) -> MessengerNotification:
        return MessengerNotification(self)

    # Getters for MessengerNotification
    def get_content(self):
        return self._content

    def get_sender(self):
        return self._sender

    def get_recipient(self):
        return self._recipient

    def get_timestamp(self):
        return self._timestamp

    def get_attachments(self):
        return self._attachments

    def get_theme(self):
        return self._theme
