from collections import deque

counter = 8
character ="%"
my_rows = []

mi_list = deque(my_rows)

def spacesPyramid(summation,  counterPara):
        return " " * (counterPara - summation) + character * (2 * summation - 1) + " " * (counterPara - summation)

def spacesPyramidInverse(summation,  counterPara):
        return " " * (counterPara - summation) + character * (2 * summation - 1) + " " * (counterPara - summation)

my_rows_one = [spacesPyramid(i + 1, counter) for i in range(counter)]

for i in range(counter): 
     mi_list.appendleft(spacesPyramid(i + 1, counter))

my_rows_third = [spacesPyramidInverse(i, counter) for i in range(counter, 0, -1)]

result_one = "\n".join(my_rows_one)

result_first_inverse_deque = "\n".join(mi_list)

result_second_inverse_slice = '\n'.join(my_rows_one[::-1]) + '\n'

result_third_inverse_join = "\n".join(my_rows_third)

print(result_one)
print('*' * 10  + "INVERSE WITH DEQUE" + '*' * 10)
print(result_first_inverse_deque)
print('*' * 10  + "INVERSE WITH SLICE" + '*' * 10)
print(result_second_inverse_slice)
print('*' * 10 + "INVERSE WITH for i in range( counter, 0, -1)" + '*' * 10)
print(result_third_inverse_join)