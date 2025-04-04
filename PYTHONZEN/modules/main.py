'''
from package.mod_1 import funct_1, funct_2
from package.mod_2 import func_3
import package
print(funct_1())
print(funct_2())

print(func_3())
print(package.URL)
'''

import package
print(package.URL)
print(package.mod_1.funct_1())