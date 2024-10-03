from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def accept(self, feature_visitor):
        pass