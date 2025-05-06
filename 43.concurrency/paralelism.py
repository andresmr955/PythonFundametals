import multiprocessing

#function to calculate square of a number
def calculate_square(n):
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    #Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        result = pool.map(calculate_square, numbers)
        print("Squares:", result)
# This code uses the multiprocessing module to create a pool of worker processes that calculate the square of numbers in parallel.