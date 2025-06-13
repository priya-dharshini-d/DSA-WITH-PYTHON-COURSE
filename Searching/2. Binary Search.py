#  Iterative Binary Search.


# It returns location of x in given array arr

def binarySearch(arr, low, high, x):

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == x:         # Check if x is present at mid
            return mid

        elif arr[mid] < x:        # If x is greater, ignore left half
            low = mid + 1

        else:                     # If x is smaller, ignore right half
            high = mid - 1

    return -1                      # If we reach here, then the element was not present


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")



# Recursive binary search.


# Returns index of x in arr if present, else -1

def binarySearch(arr, low, high, x):

    if high >= low:    # Check base case

        mid = low + (high - low) // 2

        if arr[mid] == x:            # If element is present at the middle itself
            return mid

        elif arr[mid] > x:           # If element is smaller than mid, then it can only be present in left subarray
            return binarySearch(arr, low, mid-1, x)

        else:                        # Else the element can only be present in right subarray
            return binarySearch(arr, mid + 1, high, x)

    else:                            # Element is not present in the array
        return -1


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")

