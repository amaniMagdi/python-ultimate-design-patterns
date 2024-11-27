class Trip:
    def __init__(self):
        self.flight_departure = None
        self.flight_destination = None
        self.flight_date = None
        self.room_id = None
        self.check_in_date = None
        self.check_out_date = None
        self.car_rental_location = None
        self.car_rental_start_date = None
        self.car_rental_end_date = None
        self.payment_method = None
        self.amount = 0.0

    # Getters
    def get_flight_departure(self):
        return self.flight_departure

    def get_flight_destination(self):
        return self.flight_destination

    def get_flight_date(self):
        return self.flight_date

    def get_room_id(self):
        return self.room_id

    def get_check_in_date(self):
        return self.check_in_date

    def get_check_out_date(self):
        return self.check_out_date

    def get_car_rental_location(self):
        return self.car_rental_location

    def get_car_rental_start_date(self):
        return self.car_rental_start_date

    def get_car_rental_end_date(self):
        return self.car_rental_end_date

    def get_payment_method(self):
        return self.payment_method

    def get_amount(self):
        return self.amount

    # Setters
    def set_flight_departure(self, flight_departure):
        self.flight_departure = flight_departure

    def set_flight_destination(self, flight_destination):
        self.flight_destination = flight_destination

    def set_flight_date(self, flight_date):
        self.flight_date = flight_date

    def set_room_id(self, room_id):
        self.room_id = room_id

    def set_check_in_date(self, check_in_date):
        self.check_in_date = check_in_date

    def set_check_out_date(self, check_out_date):
        self.check_out_date = check_out_date

    def set_car_rental_location(self, car_rental_location):
        self.car_rental_location = car_rental_location

    def set_car_rental_start_date(self, car_rental_start_date):
        self.car_rental_start_date = car_rental_start_date

    def set_car_rental_end_date(self, car_rental_end_date):
        self.car_rental_end_date = car_rental_end_date

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    def set_amount(self, amount):
        self.amount = amount
