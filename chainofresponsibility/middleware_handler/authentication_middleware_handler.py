from abstract_middleware_handler import AbstractMiddlewareHandler
from response import Response

class AuthenticationMiddleware(AbstractMiddlewareHandler):

    def handle(self, request):
        print("Checking if request is Authenticated...")
        if not request.is_authenticated():
            print("Request is not authenticated")
            return Response("Request is not authenticated", False)
        return super().handle(request)  