def my_merge_sort(lst):
    if len(lst) > 1:
        middle = len(lst) // 2
        left_lst = lst[:middle]
        right_lst = lst[middle:]

        my_merge_sort(left_lst)
        my_merge_sort(right_lst)

        i = k = j = 0

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

        while j < len(left_lst):
            lst[k] = left_lst[j]
            j += 1
            k += 1
              

    return lst
