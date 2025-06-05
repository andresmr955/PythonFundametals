import random 

def merge_sort(lst):
    if len(lst) > 1:
        middle = len(lst) // 2
        left_lst = lst[:middle]
        right_lst = lst[middle:]
        print(f'{left_lst} ---- {right_lst}')

        ## We call recursivity

        merge_sort(left_lst)
        merge_sort(right_lst)


        #Iterators to iterate both sublist
        i = 0
        j = 0
        # Iterator to iterate the main list
        k = 0

        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                lst[k] = left_lst[i]
                i += 1
            else:
                lst[k] = right_lst[j]
                j += 1
            k += 1

        
        while i < len(left_lst):
            lst[k] = left_lst[i]
            i += 1
            k += 1
        
        while j < len(right_lst):
            lst[k]  = right_lst[j]
            j += 1
            k += 1
        print(f'Left list {left_lst}, right list {right_lst}')
        print(lst)
        print('-' * 50 )
    return lst

if __name__ == '__main__':
    # size_lst = int(input("How long the list would be of?"))
    lst_done = [7, 3, 2, 16, 24, 4, 11, 9]

    print(lst_done)
    print('*' * 100)

    sorted_lst = merge_sort(lst_done)
    print(sorted_lst)