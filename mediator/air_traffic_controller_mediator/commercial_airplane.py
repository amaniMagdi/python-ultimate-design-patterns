from airplane import Airplane

class CommercialAirplane(Airplane):
    def __init__(self, mediator):
        self.mediator = mediator

    def get_type(self) -> str:
        return "Commercial"

    def request_takeoff(self):
        self.mediator.request_takeoff(self)

    def request_landing(self):
        self.mediator.request_landing(self)

    def notify_air_traffic_control(self, message: str):
        print(f"Commercial Airplane: {message}")