import random
from bubblesort import selection_sort_ascending

def search(list_x, objective):
    match = False
    for i in list_x:
        if i == objective:
            match = True
            break
    return match

if __name__ == "__main__":
    list_size = int(input("What list's size do you want for? ->"))
    number_guess = int(input("What number do you want to find? ->"))

    my_list = [random.randint(0, 100) for i in range(list_size)]
    selection_sort_ascending(my_list)
    print(my_list)

    found_it = search(my_list, number_guess)
    print(f"The element {number_guess} {"is" if found_it else 'is not'} in the list")