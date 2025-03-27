'''
In this Python challenge, you must create the logic for the is_leap_year function, which determines whether a year is a leap year or not. A year is a leap year if it meets the following conditions:

It is divisible by 4, but not by 100.
If it is divisible by 100 it must be divisible by 400 as well.
The is_leap_year function receives a single parameter: the year to evaluate. It must return True if the year is a leap year or False otherwise.

Note that the function must be able to handle non-integer or negative values.

Translated with DeepL.com (free version)
'''
def is_leap_year(year):
    # tu código aquí 👈
    if year % 100  == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0:
        if year % 100 == 0:
            return False
        else:
            if year >= 0:
                return True
            else:
                return False
    else:
        return False         

