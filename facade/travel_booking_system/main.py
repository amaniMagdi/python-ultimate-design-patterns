from trip import Trip
from booking_trip_facade import BookingTravelFacade

from trip import Trip
from booking_trip_facade import BookingTravelFacade

def main():
    # Create a trip object
    trip = Trip()
    
    # Set trip details using setter methods
    trip.set_flight_departure("Amsterdam")
    trip.set_flight_destination("Spain")
    trip.set_flight_date("2024-01-01T08:00:00")
    trip.set_room_id("12345")
    trip.set_check_in_date("2024-01-01T14:00:00")
    trip.set_check_out_date("2024-01-04T11:00:00")
    trip.set_car_rental_location("Schiphol Airport")
    trip.set_car_rental_start_date("2024-01-01T15:00:00")
    trip.set_car_rental_end_date("2024-01-04T11:15:00")
    trip.set_amount(1000.0)
    trip.set_payment_method("Visa")
    
    # Create a BookingTravelFacade instance
    booking_travel_facade = BookingTravelFacade()
    
    # Book the trip
    booking_travel_facade.book_trip(trip)

if __name__ == "__main__":
    main()
