from middleware_handler import MiddlewareHandler
from response import Response

class AbstractMiddlewareHandler(MiddlewareHandler): 
    def __init__(self):
        self.__next = None

    def set_next(self, middleware_handler):
        self.__next = middleware_handler
        return middleware_handler

    def handle(self, request):
        if self.__next:
            return self.__next.handle(request)
        else:
            return Response("Request has passed all checks successfully", True)