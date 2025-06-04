
# The objective of the program is to simulate milk production on a farm for one week. It is assumed that there are n cows, and each cow produces a variable amount of milk each day. The program must create a 7xN matrix to store the milk production data of the cows during the 7 days of the week. In addition, it must calculate:



# The total milk production per day (i.e., the amount of milk produced by all cows on a given day).


# The number of the cow that gave the most milk each day.

# Translated with DeepL.com (free version)
import random

# Function to generate the milk production matrix
def generate_cow_production(n):
    # Create a 7xN matrix with random milk production values (in liters)
    # Each cow produces between 10 and 50 liters of milk per day
    matrix = [[random.randint(10, 50) for _ in range(n)] for _ in range(7)]
    return matrix

# Function to calculate the total milk production of the herd each day
def calculate_total_production(matrix):
    total_per_day = []
    for day in range(7):
        total_per_day.append(sum(matrix[day]))  # Sum the values of all cows for each day
    return total_per_day

# Function to find the cow that gave the most milk each day
def cow_with_most_milk(matrix):
    cows_max = []
    for day in range(7):
        max_milk = max(matrix[day])  # Find the maximum value for the day
        cow_max = matrix[day].index(max_milk) + 1  # Index of the cow with the most milk, adding 1 to make it a valid cow number
        cows_max.append((cow_max, max_milk))
    return cows_max

# Main function
def main():
    # Ask the user for the number of cows
    n = int(input("Enter the number of cows: "))
    
    # Generate the milk production matrix
    production = generate_cow_production(n)
    
    # Display the milk production matrix
    print("\nMilk production matrix (liters) over 7 days:")
    for i in range(7):
        print(f"Day {i+1}: {production[i]}")
    
    # Calculate and display the total milk production per day
    total_per_day = calculate_total_production(production)
    print("\nTotal milk production per day:")
    for i, total in enumerate(total_per_day):
        print(f"Day {i+1}: {total} liters")
    
    # Find the cow that gave the most milk each day
    cows_max = cow_with_most_milk(production)
    print("\nCow that gave the most milk each day:")
    for i, (cow, milk) in enumerate(cows_max):
        print(f"Day {i+1}: Cow {cow} with {milk} liters")

# Run the program
if __name__ == "__main__":
    main()
