try: 
    print(0/0)
except ZeroDivisionError:
    print("It is not possible to divide in zero")

print("Hola")

#assert prints an error

try:
    assert 1 != 1, "One is not equal"

except AssertionError as error:
    print(error)

try:
    age = 10
    if age < 18:
        raise Exception("We do not allow younger than 18")
except Exception as error:
    print(error)

print("Hola")