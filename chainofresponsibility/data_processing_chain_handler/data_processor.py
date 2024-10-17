from response import Response

class DataProcessor:
    def __init__(self, data_processing_chain_hanlder):
        self._data_processing_chain_hanlder = data_processing_chain_hanlder
    def process_data(self, data):
        if not self._data_processing_chain_hanlder.handle(data).is_succeeded():
            return Response("Request failed!", False)
        
        print("Processing data!")
        return Response("Data Successfully Processed", True)