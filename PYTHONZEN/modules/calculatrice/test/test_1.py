import unittest
import math
#from figures import area_circle, area_rectangle
def area_circle(radius):
    """Calculates the area of a circle given its radius."""
    return 3.14 * radius ** 2

def area_rectangle(length, width):
    """Calculates the area of a rectangle given its length and width."""
    return length * width

class TestCalculateArea(unittest.TestCase):
    def test_area_circle(self):
        result = area_circle(5)

        expected = math.pi * 5 ** 2

        self.assertAlmostEqual(result, expected, places=1)
        ## we try with a radius of 0

        result = area_circle(0)
        self.assertAlmostEqual(result, 0)

        ## we try with a radius of -5
        result = area_circle(-5)

        expected = math.pi * (-5) ** 2
        self.assertAlmostEqual(result, expected, places=1)

    def test_area_rectangle(self):
        result = area_rectangle(6,8)
        expected = 6 * 8

        self.assertAlmostEqual(result, expected)

        ## we try with a length of 0 and a width of 8
        result = area_rectangle(0, 8)
        expected = 0 * 8

        self.assertAlmostEqual(result, expected)

        #we try with negative values
        result = area_rectangle(-5,-6)

        expected = abs(-5) * abs(-6)

        self.assertAlmostEqual (result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)