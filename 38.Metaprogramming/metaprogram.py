class MultiplierFactory:

    def __new__(cls, factor: int):
        print(f'Creating an instance with factor {factor}')
        return super(MultiplierFactory, cls).__new__(cls)

    def __init__(self, factor:int):
        print(f'Initializing with factor {factor}')
        self.factor = factor
    
    def __call__(self, number: int):
        print(f'Calling with number {number}')
        return number * self.factor
    
    def multiplier(self, number: int) -> int:
        print(f'activating my function with number {number}')
        return number * self.factor

multiplier = MultiplierFactory(5)

result = multiplier(10) # we call __call__ automatically
result_func = multiplier.multiplier(11)
print(result)
print(result_func)