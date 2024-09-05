from message_formatter import MessageFormatter

class PlainMessageFormatter(MessageFormatter):
    
    def format_message(self, message_to_formate: str) -> str:
        return message_to_formate + " Plain text formatted"
    
    def get_type(self) -> str:
        return "PLAIN_TEXT_TYPE"
