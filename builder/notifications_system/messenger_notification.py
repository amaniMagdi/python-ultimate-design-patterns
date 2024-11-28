
class MessengerNotification:
    def __init__(self, builder):
        self._content= builder.get_content()
        self._sender = builder.get_sender()
        self._recipient = builder.get_recipient()
        self._timestamp = builder.get_timestamp()
        self._attachments = builder.get_attachments()
        self._theme = builder.get_theme()

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
