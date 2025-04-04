import unittest

def suma(num_1, num_2):

     return num_1 + num_2

class BlackBox(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, 15, f"Error: {num_1} + {num_2} = {resultado}")

    def test_suma_two_negatives(self):
        num_1 = -10
        num_2 = -5

        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, -15, f"Error: {num_1} + {num_2} = {resultado}")
        
if __name__ == "__main__":
    unittest.main()