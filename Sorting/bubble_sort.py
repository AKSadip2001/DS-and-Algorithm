def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j+1]<array[j]:
                array[j+1], array[j] = array[j], array[j+1]

data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)