from abstract_data_processing_handler import AbstractDataProcessingHandler
from response import Response

class FormattingChecksHandler(AbstractDataProcessingHandler):
    def handle(self, data):
        print("Doing formatting checks on data...")
        if not data.has_passed_formatting_checks:
            print("Data has not passed formatting checks.")
            return Response("Data has not passed formatting checks", False)
        return super().handle(data)