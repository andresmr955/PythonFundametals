import unittest

def is_leap_year(year):

    if year >= 0:
        if year % 4 == 0:
            if year % 100 != 0:
                return True 

            if year % 100 == 0 :
                if year % 400 == 0:
                    return True
            
            return False
   

    return False
class TestMyLeapYear(unittest.TestCase):
    def test_year_leap(self):
        input = -2024
        output = True
        result = is_leap_year(input)

        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()