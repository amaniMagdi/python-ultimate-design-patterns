class Request:
    def __init__(self, request_type, is_authenticated, is_authorized, has_passed_security_checks):
        self._type = request_type
        self._is_authenticated = is_authenticated
        self._is_authorized = is_authorized
        self._has_passed_security_checks = has_passed_security_checks

    def set_type(self, request_type):
        self._type = request_type
        
    def get_type(self):
        return self._type
        
    def is_authenticated(self):
        return self._is_authenticated
        
    def is_authorized(self):
        return self._is_authorized
        
    def has_passed_security_checks(self):  
        return self._has_passed_security_checks
