from abstract_middleware_handler import AbstractMiddlewareHandler
from response import Response

class AuthorizationMiddleware(AbstractMiddlewareHandler):

    def handle(self, request):
        print("Checking if request is authorized...")
        if not request.is_authenticated():
            print("Request is not authorized")
            return Response("Request is not authorized", False)
        return super().handle(request)  