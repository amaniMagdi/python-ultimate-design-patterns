class Response:
    def __init__(self, reason, is_succeeded):
        self._reason = reason
        self._is_succeeded = is_succeeded

    def get_reason(self):
        return self._reason
    
    def is_succeeded(self):
        return self._is_succeeded
    