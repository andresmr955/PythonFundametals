

import unittest
from reservations import Reservation
from unittest.mock import patch
from io import StringIO
import sys


class TestReservation(unittest.TestCase):

    def test_display_reservation_details(self):
    
        """
        Test that display_reservation_details() prints the correct reservation details

        """

        reservation = Reservation(
            reservation_id=1, 
                guest_name="Alice", 
                room_number=101, 
                check_in_date="2025-06-05", 
                check_out_date="2025-06-10"
        )

        expected_output = (
            "1\n"
            "Alice\n"
            "101\n"
            "2025-06-05\n"
            "2025-06-10\n"
        )

        with patch('sys.stdout', new=StringIO()) as fake_out:
            reservation.display_reservation_details()
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()