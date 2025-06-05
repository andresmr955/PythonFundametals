import random 

def sort_my(x_list):
    n = len(x_list)
    for i in range(n):
        min_num = i
        for j in range(i + 1, n):
            # print(f'This is i: {i}, This is min_num: {min_num}')
            # print(f'This is j: {j}, This is i + 1: {i + 1}')
            # print(f'{x_list[j]} < {x_list[min_num]}')
            if x_list[j] < x_list[min_num]:
                min_num = j
        #         print(f'This is min_num in J: {min_num}')
        # print('The cycle J has finished')
        # print(f"[[BEFORE]]] =>> xlist[i] -> {x_list[i]}, xlist[min_num]: {x_list[min_num]}")
        x_list[i], x_list[min_num] = x_list[min_num], x_list[i]
        # print(f"[[NOW]]] =>> xlist[i] -> {x_list[i]}, xlist[min_num]: {x_list[min_num]}")
        # print(x_list)
    return x_list




def selection_sort_ascending(x_list):
    n = len(x_list)
    for i in range(n):
        min_num = i
        for j in range(i + 1, n):
            # print(f'This is i: {i}, This is min_num: {min_num}')
            # print(f'This is j: {j}, This is i + 1: {i + 1}')
            # print(f'{x_list[j]} > {x_list[min_num]}')
            if not x_list[j] > x_list[min_num]:
                min_num = j
        #         print(f'This is min_num in J: {min_num}')
        # print('The cycle J has finished')
        # print(f"[[BEFORE]]] =>> xlist[i] -> {x_list[i]}, xlist[min_num]: {x_list[min_num]}")
        x_list[i], x_list[min_num] = x_list[min_num], x_list[i]
        # print(f"[[NOW]]] =>> xlist[i] -> {x_list[i]}, xlist[min_num]: {x_list[min_num]}")
        # print(x_list)
    return x_list


def selection_while (list_y):
    new_list = []

    while list_y:
        min_num = min(list_y)
        new_list.append(min_num)
        list_y.remove(min_num)

    return new_list

if __name__ == "__main__":  
    ages = [random.randint(1, 1000) for i in range(6)]
    print(ages)
    print(selection_sort_ascending(ages))

    ages = [random.randint(1, 1000) for i in range(6)]
    print(ages)
    print(sort_my(ages))

    ages = [random.randint(1, 1000) for i in range(6)]
    
    print(ages)
    print(selection_while(ages))