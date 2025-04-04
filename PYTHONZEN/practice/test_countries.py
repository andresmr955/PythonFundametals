import unittest

class TestCountries(unittest.TestCase):
    def test_union_sets(self):
        countries = {"MX", "COL", "ARG", "USA"}
        northAm = {"USA", "CANADA"}
        centralAm = {"MX", "GT", "BZ"}
        southAm = {"COL", "BZ", "ARG"}

        new_set = countries.union(northAm, centralAm, southAm)
        # Resultado esperado
        expected_set = {'ARG', 'CANADA', 'BZ', 'GT', 'MX', 'COL', 'USA'}

        self.assertEqual( new_set, expected_set, f"Error: {new_set}")

if __name__ == '__main__':
    unittest.main(verbosity=2)