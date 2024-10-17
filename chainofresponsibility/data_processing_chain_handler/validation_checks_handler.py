from abstract_data_processing_handler import AbstractDataProcessingHandler
from response import Response

class ValidationChecksHandler(AbstractDataProcessingHandler):
    def handle(self, data):
        print("Doing validation checks on data...")
        if not data.has_passed_validation_checks:
            print("Data has not passed validation checks.")
            return Response("Data has not passed validation checks", False)
        return super().handle(data)