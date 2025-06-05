import random
from bubblesort import selection_sort_ascending

def binary_search(target, lst, start, final):
    print(f"Searching {target} between {lst[start]} and {lst[final - 1]}")

    if start > final:
        return False
    
    mid = (start + final) // 2
    
    print(f"the middle number {lst[mid]}")
    if lst[mid] == target:
        return True
    
    elif lst[mid] < target: 
        return binary_search(target, lst, mid + 1, final)
    else :
        return binary_search(target, lst, start , mid - 1)
    


if __name__ == "__main__":
    cus_inp = int(input("Which size do you want for the list?  "))
    cus_target = int(input("Which is your target?  "))

    list_x = [random.randint(0, 10) for i in range(cus_inp)]
    sorted_lst = selection_sort_ascending(list_x)
    print(sorted_lst)
    print(binary_search(cus_target, sorted_lst, 0, len(sorted_lst)))

