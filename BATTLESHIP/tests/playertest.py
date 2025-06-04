import unittest

class Juego:
    def __init__(self):
        # Tablero inicial de 3x3 para simplificar
        self.tablero_jugador = [['agua', 'agua', 'agua'],
                                ['agua', 'barco', 'agua'],
                                ['agua', 'agua', 'agua']]
        self.tablero_impactos = [['' for _ in range(3)] for _ in range(3)]

    def attack(self, fila, columna):
        """Método para atacar una posición en el tablero."""
        # Verificar que la posición esté dentro del tablero
        if fila < 0 or fila >= 3 or columna < 0 or columna >= 3:
            raise ValueError("Posición inválida")

        # Si ya se ha atacado en esa posición
        if self.tablero_impactos[fila][columna] != '':
            raise ValueError("Ya has atacado esta posición")

        # Registrar el ataque en el tablero de impactos
        self.tablero_impactos[fila][columna] = 'X'

        # Verificar si el ataque fue un impacto o agua
        if self.tablero_jugador[fila][columna] == 'barco':
            return "¡Impacto!"
        else:
            return "¡Agua!"

# Tests
class TestJuego(unittest.TestCase):

    def setUp(self):
        """Prepara el juego antes de cada prueba."""
        self.juego = Juego()

    def test_ataque_agua(self):
        """Prueba que un ataque a una posición vacía sea agua."""
        resultado = self.juego.attack(0, 0)  # Atacamos a (0, 0)
        self.assertEqual(resultado, "¡Agua!")

    def test_ataque_impacto(self):
        """Prueba que un ataque a una posición con un barco sea un impacto."""
        resultado = self.juego.attack(1, 1)  # Atacamos a (1, 1) donde está el barco
        self.assertEqual(resultado, "¡Impacto!")

    def test_posicion_invalida(self):
        """Prueba que atacar fuera del tablero lance una excepción."""
        with self.assertRaises(ValueError):
            self.juego.attack(3, 3)  # Fuera del tablero (3, 3)

    def test_ataque_repetido(self):
        """Prueba que no se pueda atacar la misma posición dos veces."""
        self.juego.attack(1, 1)  # Primer ataque
        with self.assertRaises(ValueError):
            self.juego.attack(1, 1)  # Ataque repetido en (1, 1)

# Ejecutar los tests
if __name__ == "__main__":
    unittest.main()
