from message_formatter import MessageFormatter
from abc import abstractmethod

class AbstractMessageFormatter(MessageFormatter):
    def format_message(self, message_to_format: str) -> str:
        self.__validate_message()
        self.__check_message_size()
        return self._format(message_to_format)

    
    def __validate_message(self):
        print("Validating the message...")

    def __check_message_size(self):
        print("Checking message size...")

    @abstractmethod
    def _format(self, message_to_format: str) -> str:
        pass
