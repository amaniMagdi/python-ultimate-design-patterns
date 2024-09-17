from abstract_message_formatter import AbstractMessageFormatter

class XMLMessageFormatter(AbstractMessageFormatter):
    
    def _format(self, message_to_formate: str) -> str:
        return message_to_formate + " XML formatted"
    
    def get_type(self) -> str:
        return "XML_TYPE"