from abstract_message_formatter import AbstractMessageFormatter

class PlainMessageFormatter(AbstractMessageFormatter):
    
    def _format(self, message_to_formate: str) -> str:
        return message_to_formate + " Plain text formatted"
    
    def get_type(self) -> str:
        return "PLAIN_TEXT_TYPE"
