class TempratureData:
    def __init__(self, temperature_date: str):
        self._result = temperature_date

    def get_temperature(self):
        return self._result
    
    