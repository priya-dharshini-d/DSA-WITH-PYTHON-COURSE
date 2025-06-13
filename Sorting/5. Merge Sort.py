# Using While loop

def Mergesort(array):

    if len(array) > 1:

        middle = len(array) // 2

        left = array[:middle]
        right = array[middle:]

        Mergesort(left)
        Mergesort(right)

        lp = rp = fp = 0

        while lp < len(left) and rp < len(right):
            if left[lp] < right[rp]:
                array[fp] = left[lp]
                lp += 1
            else:
                array[fp] = right[rp]
                rp += 1
            fp += 1

        while lp < len(left):
            array[fp] = left[lp]
            lp += 1
            fp += 1

        while rp < len(right):
            array[fp] = right[rp]
            rp += 1
            fp += 1


array = [3, 2, 24, 27, 29, 31, 32]
Mergesort(array)
print(array)

# Using for and while loop

def merge(arr, left, mid, right):
    n1 = mid - left + 1         # Size of left subarray
    n2 = right - mid            # Size of right subarray

    L = [0] * n1                # Temp array for left half
    R = [0] * n2                # Temp array for right half

    for i in range(n1):
        L[i] = arr[left + i]    # Copy left half to L
    for j in range(n2):
        R[j] = arr[mid + 1 + j] # Copy right half to R

    i = j = 0                   # Initial indexes for L and R
    k = left                   # Initial index for merged array

    while i < n1 and j < n2:
        if L[i] <= R[j]:        # Pick smaller or equal for stability
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:               # Copy any remaining elements from L
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:               # Copy any remaining elements from R
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2       # Find the middle point

        merge_sort(arr, left, mid)      # Sort first half
        merge_sort(arr, mid + 1, right) # Sort second half
        merge(arr, left, mid, right)    # Merge the two halves

# Descending order

def Mergesort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]

        Mergesort(left)
        Mergesort(right)

        lp = rp = fp = 0

        # CHANGED: '>' instead of '<' to sort in descending order
        while lp < len(left) and rp < len(right):
            if left[lp] > right[rp]:  # <-- changed from < to >
                array[fp] = left[lp]
                lp += 1
            else:
                array[fp] = right[rp]
                rp += 1
            fp += 1

        # These two loops are unchanged
        while lp < len(left):
            array[fp] = left[lp]
            lp += 1
            fp += 1

        while rp < len(right):
            array[fp] = right[rp]
            rp += 1
            fp += 1

# Driver code
array = [3, 2, 24, 27, 29, 31, 32]
Mergesort(array)
print(array)  # Output will be sorted in descending order




# Merge Sort for Linked Lists


# Node class definition
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# Function to split the linked list into two halves
def split_list(head):
    fast_pointer = head
    slow_pointer = head

    # Move fast two steps and slow one step
    while fast_pointer and fast_pointer.next:
        fast_pointer = fast_pointer.next.next
        if fast_pointer:
            slow_pointer = slow_pointer.next

    second_half = slow_pointer.next
    slow_pointer.next = None  # Break the list into two halves
    return second_half

# Function to merge two sorted linked lists
def merge_sorted_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.data < list2.data:
        list1.next = merge_sorted_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_sorted_lists(list1, list2.next)
        return list2

# Merge sort function
def merge_sort(head):
    if not head or not head.next:
        return head  # Base case

    second_half = split_list(head)

    # Recursively sort both halves
    left_sorted = merge_sort(head)
    right_sorted = merge_sort(second_half)

    # Merge the sorted halves
    return merge_sorted_lists(left_sorted, right_sorted)

# Function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Driver code
if __name__ == "__main__":
    head = Node(9)
    head.next = Node(8)
    head.next.next = Node(5)
    head.next.next.next = Node(2)

    print("Original list:")
    print_linked_list(head)

    head = merge_sort(head)

    print("Sorted list:")
    print_linked_list(head)


# Merge Sort for Doubly Linked List

# Node definition for doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Function to split a doubly linked list into two halves
def split(head):
    fast = head
    slow = head

    # Move fast two steps and slow one step
    while fast and fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    # Detach second half
    second = slow.next
    slow.next = None
    if second:
        second.prev = None  # Remove backward link

    return second

# Function to merge two sorted doubly linked lists
def merge(first, second):
    # Base cases
    if not first:
        return second
    if not second:
        return first

    # Choose the smaller node
    if first.data < second.data:
        first.next = merge(first.next, second)
        if first.next:
            first.next.prev = first
        first.prev = None
        return first
    else:
        second.next = merge(first, second.next)
        if second.next:
            second.next.prev = second
        second.prev = None
        return second

# Merge sort function
def merge_sort(head):
    # Base case: already sorted
    if not head or not head.next:
        return head

    # Split into halves
    second = split(head)

    # Sort each half recursively
    first_sorted = merge_sort(head)
    second_sorted = merge_sort(second)

    # Merge the sorted halves
    return merge(first_sorted, second_sorted)

# Print doubly linked list
def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

# Driver code
if __name__ == "__main__":
    # Create: 10 <-> 8 <-> 5 <-> 2
    head = Node(10)
    head.next = Node(8)
    head.next.prev = head
    head.next.next = Node(5)
    head.next.next.prev = head.next
    head.next.next.next = Node(2)
    head.next.next.next.prev = head.next.next

    # Sort and print
    head = merge_sort(head)
    print_list(head)




# Find a permutation that causes worst case of Merge Sort

# Python program to generate Worst Case input for Merge Sort

# Function to merge two subarrays into the main array
def join(arr, left, right, l, m, r):
    # Copy elements from left[] first
    for i in range(m - l + 1):
        arr[i] = left[i]

    # Copy elements from right[] next
    for j in range(r - m):
        arr[i + j] = right[j]

# Function to split array into left and right
# using alternate elements
def split(arr, left, right, l, m, r):
    # Left gets even indices
    for i in range(m - l + 1):
        left[i] = arr[i * 2]

    # Right gets odd indices
    for i in range(r - m):
        right[i] = arr[i * 2 + 1]

# Recursive function to generate worst-case input
def generate_worst_case(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        # Create temporary arrays
        left = [0] * (m - l + 1)
        right = [0] * (r - m)

        # Split arr into left and right
        split(arr, left, right, l, m, r)

        # Recursively generate worst-case on both halves
        generate_worst_case(left, l, m)
        generate_worst_case(right, m + 1, r)

        # Join the results
        join(arr, left, right, l, m, r)

# Driver code
if __name__ == "__main__":
    # Start with a sorted array
    arr = [i for i in range(1, 17)]  # 1 to 16
    print("Sorted array is:")
    print(arr)

    # Generate a worst-case merge sort input
    generate_worst_case(arr, 0, len(arr) - 1)

    print("\nWorst-case input for merge sort:")
    print(arr)
