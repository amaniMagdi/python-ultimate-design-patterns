from abstract_middleware_handler import AbstractMiddlewareHandler
from response import Response

class SecurityChecksMiddleware(AbstractMiddlewareHandler):

    def handle(self, request):
        print("Checking if request pass security checks...")
        if not request.is_authenticated():
            print("equest failed to pass security checks...")
            return Response("equest failed to pass security checks...", False)
        return super().handle(request)  