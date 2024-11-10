from air_traffic_control_mediator import AirTrafficControlMediator

class AirportControlTower(AirTrafficControlMediator):
    def __init__(self):
        self.airplanes= []

    def request_takeoff(self, airplane):
        for other_airplane in self.airplanes:
            other_airplane.notify_air_traffic_control(
                f"The following airplane: {airplane.get_type()} is taking off..."
            )
        airplane.notify_air_traffic_control("Requesting takeoff accepted...")

    def request_landing(self, airplane):
        for other_airplane in self.airplanes:
            other_airplane.notify_air_traffic_control(
                f"The following airplane: {airplane.get_type()} is landing..."
            )
        airplane.notify_air_traffic_control("Requesting landing accepted...")

    def register(self, airplane):
        self.airplanes.append(airplane)
