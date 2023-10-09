def mergeSort(array):
    if len(array)>1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)

        i=j=k=0

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                array[k] = left[i]
                i += 1
            elif left[i]>right[j]:
                array[k] = right[j]
                j += 1
            k += 1

        while i<len(left):
            array[k]=left[i]
            i += 1
            k += 1
        
        while j<len(right):
            array[k]=right[j]
            j += 1
            k += 1

array = [6, 5, 12, 10, 9, 1]

mergeSort(array)

print("Sorted array is: ")
print(array)
