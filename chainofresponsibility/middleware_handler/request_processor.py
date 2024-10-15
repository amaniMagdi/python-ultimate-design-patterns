from response import Response

class RequestProcessor:
    def __init__(self, middleware_chain_handler):
        self._request_middleware_handler_chain = middleware_chain_handler
    
    def process_request(self, request):
        if not self._request_middleware_handler_chain.handle(request).is_succeeded():
            return Response("Request failed!", False)

        print("Processing request")
        return Response("Request Successfully Processed", True)