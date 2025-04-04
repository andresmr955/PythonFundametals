import sys
print(sys.path)
## sys.path is a list of strings that specifies the search path for modules

import re 

text = "My telephone number is 123-456-7890. Call me at 555-1234."
x = re.findall('[0-9]+', text)
print(x)  # Returns a match object

import time
timestamp = time.time()
print(timestamp)  # Returns the current timestamp

local = time.localtime()
print(local)  # Returns the local time in struct_time format

result = time.asctime(local)
print(result)  # Returns the local time in a human-readable format

import collections
## to count the number of occurrences of each character in a string

numbers = [1, 2, 3, 4, 5, 1, 2, 3]

counter = collections.Counter(numbers)
print(counter)  # Returns a Counter object with counts of each element

import random 

## to generate a random number between 1 and 10
number = random.randint(1, 10)
print(number)  # Returns a random integer between 1 and 10