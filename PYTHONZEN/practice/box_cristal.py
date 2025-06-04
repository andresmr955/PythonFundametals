import unittest

def is_older_than(age):
    if age > 18:
        return False
    else:
        return False

class TestofCristalTest(unittest.TestCase):

    ##First test
    def test_is_older_than(self):
        age = 20

        result = is_older_than(age)
        self.assertEqual(result, True)

    ##second test
    def test_is_younger_than(self):
        age = 15

        result = is_older_than(age)
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main(verbosity=2)