for i in range(1,10):
    print(i)

example = range(1, 10)
print(example)

example_iterable = iter(range(1, 4))
                         
print(next(example_iterable))
print(next(example_iterable))
print(next(example_iterable))
print(next(example_iterable))##Here it gives an error stopiteration
