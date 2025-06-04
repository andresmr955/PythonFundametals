class Counter:
    count = 0

    #cls means class
    #A class method (decorated with @classmethod) allows you to modify or interact with the class itself rather than with an instance of the class.
    @classmethod
    def increment(cls):
        cls.count += 1

Counter.increment()
Counter.increment()
Counter.increment()
print(Counter.count)