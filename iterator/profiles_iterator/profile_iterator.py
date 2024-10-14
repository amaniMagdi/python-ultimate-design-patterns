from abc import ABC, abstractmethod

class ProfileIterator(ABC):

    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass
