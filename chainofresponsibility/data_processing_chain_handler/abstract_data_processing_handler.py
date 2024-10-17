from data_processing_chain_handler import DataProcessingChainHandler
from response import Response

class AbstractDataProcessingHandler(DataProcessingChainHandler):
    def __init__(self):
        self.__next_hanlder = None

    def set_next(self, next_hanlder):
        self.__next_hanlder = next_hanlder
        return next_hanlder
    
    def handle(self, data):
        if self.__next_hanlder is not None:
            return self.__next_hanlder.handle(data)
        else:
            return Response("Succeeded to proceed the job", True)
        
    

    