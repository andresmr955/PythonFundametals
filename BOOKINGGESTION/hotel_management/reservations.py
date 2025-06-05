from collections import defaultdict
from datetime import datetime

class Reservation:
    def __init__(self, reservation_id, guest_name, room_number, check_in_date=None, check_out_date=None):
        self.reservation_id = reservation_id
        self.guest_name = guest_name
        self.room_number = room_number
        self.check_in_date = check_in_date if check_in_date else datetime.today()
        self.check_out_date = check_out_date if check_out_date else datetime.today()

    def display_reservation_details(self):
        print(self.reservation_id)
        print(self.guest_name)
        print(self.room_number)
        print(self.check_in_date)
        print(self.check_out_date)
    
    def update_dates(self, new_check_in, new_check_out):
        self.check_in_date = new_check_in
        self.check_out_date = new_check_out

    def cancel_reservation(self):
        print(f"The reservation {self.reservation_id} for {self.guest_name} has been canceled")

    def __str__(self):
        return f'{self.reservation_id} - {self.guest_name} - {self.room_number} - {self.check_in_date} - {self.check_out_date}'
    

class ReservationsSystem:
    

    def __init__(self):
        self.reservations_date = defaultdict(list)

    def add_reservations(self, reservation):
        self.reservations_date[reservation.check_in_date].append(reservation)

    def print_reservations(self):
        for res_date, reservations in self.reservations_date.items():
            print(f"Date: {res_date}")
            for res in reservations:
                print(f" - {res}")

    def __str__(self):
        return f"{self.reservations_date}"
    


if __name__ == "__main__":
    system = ReservationsSystem()

    reservation1 = Reservation(1, "Alice", 101)
    reservation2 = Reservation(2, "Bob", 102)
    reservation3 = Reservation(3, "Charlie", 103, datetime(2025, 6, 5))

    system.add_reservations(reservation1)
    system.add_reservations(reservation2)
    system.add_reservations(reservation3)

    system.print_reservations()