def binarySearch(array, search_element, low, high):
    if low <= high:
        mid = (high + low)//2

        if array[mid] > search_element:
            return binarySearch(array, search_element, low, mid-1)
        elif array[mid] < search_element:
            return binarySearch(array, search_element, mid+1, high)
        else:
            return mid
    else:
        return -1



array = [3, 4, 5, 6, 7, 8, 9]
search = 8

result = binarySearch(array, search, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")