import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_get_population(self):
        keys, values = utils.get_population()
        self.assertEqual(keys, ['col', 'bol'])
        self.assertEqual(values, [300, 400])

    def test_population_by_country(self):
        data = [
            {'Country': 'col', 'Population': 300},
            {'Country': 'bol', 'Population': 400},
            {'Country': 'per', 'Population': 500}
        ]
        result = utils.population_by_country(data, 'bol')

        expected = [{'Country': 'bol', 'Population': 400}]

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity =2)