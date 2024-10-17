from abstract_data_processing_handler import AbstractDataProcessingHandler
from response import Response

class DataSizeChecksHandler(AbstractDataProcessingHandler):
    def handle(self, data):
        print("Doing data size checks on data...")
        if not data.has_passed_data_size_checks:
            print("Data has not passed data size checks.")
            return Response("Data has not passed data size checks", False)
        return super().handle(data)