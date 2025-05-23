import random

def production_week(n):
    matrix = [[ random.randint(10,50) for _ in range(n)] for _ in range(7)]
    return matrix

def calculate_day(matrix):
    total_day = []
    for day, production in enumerate(matrix):
        
        total_day.append(sum(production))

    return total_day


def cow_production(matrix):
    total_max = []
    for day, production in enumerate(matrix):
        total_max.append((production.index(max(production)), max(production)))

    return total_max

n = int(input("How many cows do you want?"))
production_var = production_week(n)

print(f"- Production of {len(production_var)} days of {n} cows.")
for day, production in enumerate(production_var):
    print(f"Day: {day + 1 }  {production}")

print("******************************\n")
for day, production in enumerate(calculate_day(production_var)):
        print(f"Day: {day + 1} - TOTAL PRODUCTION DAY: {production} liters.")
print("******************************\n")

for day, production in enumerate(cow_production(production_var)):
      print(f"Day: {day + 1} - HIGHT-YIELDING COW NUMBER {production[0] + 1} and total liters: {production[1]}")