from notification_builder import NotificationBuilder
from slack_notification import SlackNotification


class SlackNotificationBuilder(NotificationBuilder):
    def __init__(self):
        self._content: str = ""
        self._sender: str = ""
        self._recipient: str = ""
        self._timestamp: str = ""
        self._has_markdown_language: bool = False

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

    def set_markdown_language(self, has_markdown_language: bool):
        self._has_markdown_language = has_markdown_language
        return self

    def get_content(self) -> str:
        return self._content

    def get_sender(self) -> str:
        return self._sender

    def get_recipient(self) -> str:
        return self._recipient

    def get_timestamp(self) -> str:
        return self._timestamp

    def has_markdown_language(self) -> bool:
        return self._has_markdown_language

    def build(self) -> SlackNotification:
        return SlackNotification(self)
