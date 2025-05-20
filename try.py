import sys
import os
import unittest

# Añadir el directorio raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ejecutar las pruebas
unittest.TextTestRunner().run(unittest.defaultTestLoader.discover('UNITTESTPYTHON/bankaccount/tests'))
