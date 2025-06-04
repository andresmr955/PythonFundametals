import unittest
from length_encode import dicc_counter

class diccCounterTest(unittest.TestCase):
    def test_dicc_counter(self):
        self.assertEqual(dicc_counter("a"), [['a', 1]])

    def test_dicc_counter_x(self):
        self.assertEqual(dicc_counter("aaaabbcca"), [['a', 4], ['b', 2], ['c', 2], ['a', 1]])

if __name__ == '__main__':
    unittest.main()