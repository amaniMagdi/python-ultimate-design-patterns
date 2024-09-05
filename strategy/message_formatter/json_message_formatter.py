from message_formatter import MessageFormatter

class JsonMessageFormatter(MessageFormatter):
    
    def format_message(self, message_to_formate: str) -> str:
        return message_to_formate + " JSON formatted"
    
    def get_type(self) -> str:
        return "JSON_TYPE"
