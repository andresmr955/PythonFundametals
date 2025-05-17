import time
import sys

print(sys.getrecursionlimit())

sys.setrecursionlimit(200000)

print(sys.getrecursionlimit())

def factorial(n):
    answer = 1

    while n > 1:
        answer *= n
        n -= 1
    return answer 

def factorial_r(n):
    if n == 1:
        return 1
    
    return n  * factorial(n -1)

if __name__ == "__main__":
    n = 500000

    starts = time.time()
    #print(factorial(n))
    factorial(n)
    final = time.time()
    print(final-starts)

    starts = time.time()
    #print(factorial_r(n))
    factorial_r(n)
    final = time.time()
    print(final-starts)
