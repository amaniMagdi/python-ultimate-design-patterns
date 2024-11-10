from airport_control_tower import AirportControlTower
from commercial_airplane import CommercialAirplane
from travel_airplane import TravelAirplane


def main():
    control_tower = AirportControlTower()

    commercial_plane = CommercialAirplane(control_tower)
    travel_plane = TravelAirplane(control_tower)

    control_tower.register(commercial_plane)
    control_tower.register(travel_plane)

    commercial_plane.request_takeoff()
    travel_plane.request_landing()


if __name__ == "__main__":
    main()