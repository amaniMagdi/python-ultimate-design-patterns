from abstract_message_formatter import AbstractMessageFormatter

class JsonMessageFormatter(AbstractMessageFormatter):
    
    def _format(self, message_to_formate: str) -> str:
        return message_to_formate + " JSON formatted"
    
    def get_type(self) -> str:
        return "JSON_TYPE"
