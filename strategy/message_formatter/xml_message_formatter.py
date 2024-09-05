from message_formatter import MessageFormatter

class XMLMessageFormatter(MessageFormatter):
    
    def format_message(self, message_to_formate: str) -> str:
        return message_to_formate + " XML formatted"
    
    def get_type(self) -> str:
        return "XML_TYPE"