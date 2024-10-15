from abc import ABC, abstractmethod

class MiddlewareHandler(ABC): 
    @abstractmethod
    def set_next(self, middleware_hanlder):
       pass

    @abstractmethod
    def handle(self, request):
        pass