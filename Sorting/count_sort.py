def countingSort(array):
    count = [0] * 10
    output = [0]*len(array)

    for i in range(len(array)):
        count[array[i]] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for i in range(len(array)):
        output[count[array[i]]-1] = array[i]
        count[array[i]] -= 1

    for i in range(0, len(array)):
        array[i] = output[i]

data = [4, 2, 2, 8, 3, 3, 1, 5, 7, 6]
print(data)
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)