from flight_manager import FlightManager
from hotel_reservation import HotelReservation
from car_rental import CarRental
from payment_processor import PaymentProcessor
from payment_method_factory import PaymentMethodFactory

class BookingTravelFacade:
    def __init__(self):
        self.flight_manager = FlightManager()
        self.hotel_reservation = HotelReservation()
        self.car_rental = CarRental()
        self.payment_processor = PaymentProcessor()
        self.payment_method_factory = PaymentMethodFactory()

    def book_trip(self, trip):
        self.flight_manager.book_flight(
            trip.get_flight_departure(),
            trip.get_flight_destination(),
            trip.get_flight_date()
        )
        self.hotel_reservation.reserve_room(
            trip.get_room_id(),
            trip.get_check_in_date(),
            trip.get_check_out_date()
        )
        self.car_rental.rent_car(
            trip.get_car_rental_location(),
            trip.get_car_rental_start_date(),
            trip.get_car_rental_end_date()
        )
        payment_method = self.payment_method_factory.create_payment_method_of(trip.get_payment_method())
        self.payment_processor.process_payment(trip.get_amount(), payment_method)
