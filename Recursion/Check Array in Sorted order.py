def is_sorted(arr, n):
    # Base case: if array has 0 or 1 element, it is sorted
    if n == 0 or n == 1:
        return True
    
    # Check if last two elements are in order
    if arr[n - 2] > arr[n - 1]:
        return False
    
    # Recursive call for the rest of the array
    return is_sorted(arr, n - 1)

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 3, 2, 4]

print(is_sorted(arr1, len(arr1)))  # Output: True
print(is_sorted(arr2, len(arr2)))  # Output: False
