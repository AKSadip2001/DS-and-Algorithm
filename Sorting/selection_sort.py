def selectionSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        
        array[min_index], array[i] = array[i], array[min_index]

data = [-2, 45, 0, 11, -9]
selectionSort(data)
print('Sorted Array in Ascending Order:')
print(data)