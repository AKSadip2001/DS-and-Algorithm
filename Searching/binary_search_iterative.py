def binarySearch(array, search_element):
    low = 0
    high = len(array)-1

    while low<=high:
        mid = (high+low)//2

        if array[mid] == search_element:
            return mid

        elif array[mid] < search_element:
            low = mid + 1

        else:
            high = mid - 1
    
    return -1



array = [3, 4, 5, 6, 7, 8, 9]
search = 5

result = binarySearch(array, search)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")