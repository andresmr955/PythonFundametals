from collections import defaultdict
from datetime import datetime
from typing import List, Dict, Optional


class Reservation:
    """
    Represents a hotel reservation.
    """
    def __init__(self, 
                 reservation_id: int, 
                 guest_name: str, 
                 room_number: int, 
                 check_in_date: Optional[str] = None, 
                 check_out_date: Optional[str] = None):
        """
        Initializes a reservation object.

        Args:
            reservation_id (int): The unique identifier for the reservation.
            guest_name (str): The name of the guest.
            room_number (int): The room number assigned to the reservation.
            check_in_date (str): The check-in date in 'YYYY-MM-DD' format. Defaults to today.
            check_out_date (str): The check-out date in 'YYYY-MM-DD' format. Defaults to today.
        """
        self.reservation_id: int = reservation_id
        self.guest_name: str = guest_name
        self.room_number: int = room_number
        self.check_in_date: str = check_in_date if check_in_date else datetime.today().date().strftime('%Y-%m-%d')
        self.check_out_date: str = check_out_date if check_out_date else datetime.today().date().strftime('%Y-%m-%d')

    def display_reservation_details(self) -> None:
        """
        Prints the details of the reservation.
        """
        print(self.reservation_id)
        print(self.guest_name)
        print(self.room_number)
        print(self.check_in_date)
        print(self.check_out_date)
    
    def update_dates(self, new_check_in, new_check_out):
        """
        Updates the check-in and check-out dates of the reservation.

        Args:
            new_check_in (str): The new check-in date.
            new_check_out (str): The new check-out date.
        """
        self.check_in_date = new_check_in
        self.check_out_date = new_check_out

    def cancel_reservation(self) -> None:
        """
        Prints a message indicating that the reservation has been canceled.
        """
        print(f"The reservation {self.reservation_id} for {self.guest_name} has been canceled.")

    def __str__(self) -> str:
        """
        Returns a string representation of the reservation.
        """
        return f'{self.reservation_id} - {self.guest_name} - {self.room_number} - {self.check_in_date} - {self.check_out_date}'
    

class ReservationsSystem:
    """
    Manages a system of reservations grouped by check-in date.
    """
    def __init__(self) -> None:
        """
        Initializes the reservation system with a defaultdict(list) to store reservations by date.
        """
        self.reservations_date: Dict[str, list[Reservation]] = defaultdict(list)

    def add_reservations(self, reservation):
        """
        Adds a reservation to the system, grouping by check-in date.

        Args:
            reservation (Reservation): The reservation to add.
        """
        self.reservations_date[reservation.check_in_date].append(reservation)

    def print_reservations(self):
        """
        Prints all reservations grouped by their check-in date.
        """
        for res_date, reservations in self.reservations_date.items():
            print(f"Date: {res_date}")
            for res in reservations:
                print(f" - {res}")

    def __str__(self):
        """
        Returns a string representation of the reservations system.
        """
        return f"{self.reservations_date}"

    


if __name__ == "__main__":
    system = ReservationsSystem()

    reservation1 = Reservation(1, "Alice", 101)
    reservation2 = Reservation(2, "Bob", 102)
    reservation3 = Reservation(3, "Charlie", 103)

    system.add_reservations(reservation1)
    system.add_reservations(reservation2)
    system.add_reservations(reservation3)

    system.print_reservations()