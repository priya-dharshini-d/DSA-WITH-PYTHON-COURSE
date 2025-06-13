# Iterative method

def linear_search(array, size, target):
  
    for index in range(size):
        if array[index] == target:
            return index
    return -1


# Main program
if __name__ == "__main__":
    numbers = [2, 3, 4, 10, 40]
    element_to_find = 10
    array_length = len(numbers)

    # Call the search function
    found_index = linear_search(numbers, array_length, element_to_find)

    # Display the result
    if found_index == -1:
        print("Element is not present in the array.")
    else:
        print(f"Element is present at index {found_index}.")



# Recursive method

def recursive_linear_search(array, size, target, index=0):

    # Base case: If we reach end of array
    if index >= size:
        return -1

    # If element is found
    if array[index] == target:
        return index

    # Recursive call
    return recursive_linear_search(array, size, target, index + 1)


# Main Program
if __name__ == "__main__":
    numbers = [2, 3, 4, 10, 40]
    element_to_find = 10
    array_length = len(numbers)

    result = recursive_linear_search(numbers, array_length, element_to_find)

    if result == -1:
        print("Element is not present in the array.")
    else:
        print(f"Element is present at index {result}.")


