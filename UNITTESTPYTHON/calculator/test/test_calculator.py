
import unittest
from src.calculator import sum, subtract, multiply, divide

class CalculatorTest(unittest.TestCase):
    def test_sum(self):
        assert sum(2,3) == 5
    def test_subtract(self):
        assert subtract(9,4) == 5
    def test_multiply(self):
        assert multiply(3,4) == 12
    
    def test_divide(self):
        result = divide(8,4)
        expected = 2
        assert result == expected
    def test_division_zero(self):
        with self.assertRaises(ZeroDivisionError, msg="Debería haber lanzado un ZeroDivisionError"):
            divide(20,0)

    def test_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, divide, 30, 0)
