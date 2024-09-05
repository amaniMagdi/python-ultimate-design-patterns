from abc import ABC, abstractmethod

class MessageFormatter(ABC):
    @abstractmethod
    def format_message(self, message_to_formate: str) -> str:
        pass
    def get_type(self) -> str:
        pass