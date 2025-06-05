unsorted_list = [7, 3, 2, 22]
sorted_list = []


for element in unsorted_list:
    if sorted_list == []:
        sorted_list.append(element)
    else: 
        inserted = False
        for i in range(len(sorted_list)):
            if element < sorted_list[i]:
                sorted_list.insert(i, element)
                inserted = True
                break
        if not inserted:
            sorted_list.append(element)
                
print(sorted_list)

unsorted_list = [7, 3, 2, 22]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        
        key = arr[i]
        j = i - 1
        # Aquí va la comparación y desplazamiento
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insertion_sort(unsorted_list)