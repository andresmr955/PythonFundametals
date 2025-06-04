ages = [30, 15, 22, 48, 10]

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


print(sort_my(ages))

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
ages = [45, 120, 1, 35, 985]

print(selection_sort_ascending(ages))
