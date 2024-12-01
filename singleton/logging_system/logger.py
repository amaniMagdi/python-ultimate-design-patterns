from log_level import LogLevel
from threading import Lock

class Logger:

    _instance= None
    _lock = Lock() # for thread-safe 

    def __init__(self):
        if Logger._instance is not None:
            raise Exception("This class is a singleton")
        self.log_level = LogLevel.INFO

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = Logger()
        return cls._instance
    
    def set_log_level(self, log_level):
        self.log_level = log_level

    def log_debug(self, message):
        if self.log_level.value <= LogLevel.DEBUG.value:
            print(f"DEBUG: {message}")

    def log_info(self, message):
        if self.log_level.value <= LogLevel.INFO.value:
            print(f"INFO: {message}")

    def log_warn(self, message):
        if self.log_level.value <= LogLevel.WARN.value:
            print(f"WARN: {message}")

   # Log Error messages
    def log_error(self, message):
        if self.log_level.value <= LogLevel.ERROR.value:
            print(f"ERROR: {message}")