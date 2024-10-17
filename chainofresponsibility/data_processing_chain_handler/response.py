class Response:
    def __init__(self, result, is_succeeded):
        self._result = result
        self._is_succeeded = is_succeeded

    def get_result(self):
        return self._result
    
    def is_succeeded(self):
        return self._is_succeeded
    