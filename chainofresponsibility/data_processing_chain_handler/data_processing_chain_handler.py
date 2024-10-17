from abc import ABC, abstractmethod

class DataProcessingChainHandler(ABC):
    @abstractmethod
    def set_next(self, data_processing_chain_handler):
        pass
    @abstractmethod
    def handle(self, data):
        pass
    