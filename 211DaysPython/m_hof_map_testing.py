import unittest

def my_map(list, func):
    return [func(x) for x in list]

class TestMyMap(unittest.TestCase):
    def test_multiply_by_two(self):
        input = [1, 2, 3, 4]
        output = [2, 4, 6, 8]
        result = my_map(input, lambda x: x * 2)
        self.assertEqual(result, output)

    def test_convert_to_str(self):
        input = [1,2,True]
        output = ["1", "2", "True"]
        result = my_map(input, lambda x: str(x))
        self.assertEqual(result, output)   
        
if __name__ == '__main__':
    unittest.main()