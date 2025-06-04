
##This is a protected member of the class. It is not meant to be accessed directly outside the class or its subclasses.
# In Python, a single underscore prefix (e.g., _variable) is a convention to indicate that a variable or method is intended for internal use only.
class BaseClass:
    def __init__(self):
        self._protected_variable  = 'Protected Variable'
    #We will create a private attribute
        self.__private_variable = 'Private Variable'    
    def _protected_method(self):
        print('This is a Protected Method')
#we will create a private method in the base class and try to access it from the derived class.

    def __private_method(self):
        print('This is a Private Method')

    def public_method(self):
        print('This is a Public Method')
        self.__private_method()

base = BaseClass()
print(base._protected_variable)
#base._protected_method()


#base.public_method()
print(base.__private_variable)