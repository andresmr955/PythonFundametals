class Calculator:

    #A static method (decorated with @staticmethod) is used when a method does not need access to the instance (self) or the class (cls). 
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
