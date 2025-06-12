# Recursive Algorithm
def quick_sort(arr):     #Your version of Quick Sort is not stable
    if len(arr) <= 1:
        return arr

    pivot = arr[0] # Starting element as pivot # Last element - arr[-1] 
                   # Middle element - arr[len(arr)//2]
                   # random.choice(arr)
    
    left = [x for x in arr if x < pivot]
    pivot_list = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + pivot_list + quick_sort(right)


# Using Lomuto Partition Scheme. 

def partition(arr, low, high):
    
    pivot = arr[high]  # Choose the pivot
  
    i = low - 1 # Index of smaller element and indicates the right position of pivot found so far
    
    # Traverse arr[low..high] and move all smaller elements to the left side. 
    # Elements from low to i are smaller after every iteration
  
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    swap(arr, i + 1, high) # Move pivot after smaller elements and return its position
    return i + 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, low, high):
    if low < high:
        
        pi = partition(arr, low, high)  # pi is the partition return index of pivot
        quickSort(arr, low, pi - 1)   # Recursion calls for smaller elements and greater or equals elements
        quickSort(arr, pi + 1, high)


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSort(arr, 0, n - 1)

# USING 2 WHILE LOOPS
# Hoare’s Partition Scheme 

def partition(arr, start, end):
    pivot = arr[start]
    i = start - 1
    j = end + 1

    while True:
        # Move i to the right until arr[i] >= pivot
        while True:
            i += 1
            if arr[i] >= pivot:
                break

        # Move j to the left until arr[j] <= pivot
        while True:
            j -= 1
            if arr[j] <= pivot:
                break

        if i >= j:
            return j  # partition index

        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        quick_sort(arr, start, pi)
        quick_sort(arr, pi + 1, end)

# Example usage
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted:", arr)


# Naive Partition Scheme 
# Function to partition the array according to the pivot (last element)
def partition(arr):
    n = len(arr)
    pivot = arr[n - 1]  # Last element is the pivot

    # Temporary array to store rearranged elements
    temp = [0] * n
    idx = 0

    # First: fill the elements <= pivot into the temp array
    for i in range(n):
        if arr[i] <= pivot:
            temp[idx] = arr[i]
            idx += 1

    # Second: fill the elements > pivot
    for i in range(n):
        if arr[i] > pivot:
            temp[idx] = arr[i]
            idx += 1

    # Copy back to the original array into the temp array
    for i in range(n):
        arr[i] = temp[i]

# Iterative Quick sort


# This function is same in both iterative and recursive
def partition(arr, l, h):
    i = ( l - 1 )
    x = arr[h]

    for j in range(l, h):
        if   arr[j] <= x:

            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)

# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index

def quickSortIterative(arr, l, h):

    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition( arr, l, h )

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

# Driver code to test above
arr = [4, 3, 5, 2, 1, 3, 2, 3]
n = len(arr)
quickSortIterative(arr, 0, n-1)

# QuickSort on Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

def getTail(node):
    while node and node.next:
        node = node.next
    return node

def partition(start, end):
    pivot = start
    prev = start
    curr = start.next

    while curr != end.next:
        if curr.data < pivot.data:
            prev = prev.next
            prev.data, curr.data = curr.data, prev.data
        curr = curr.next

    start.data, prev.data = prev.data, start.data
    return prev

def quickSortHelper(start, end):
    if start and start != end:
        pivot = partition(start, end)
        quickSortHelper(start, pivot)
        quickSortHelper(pivot.next, end)

def quickSort(head):
    tail = getTail(head)
    quickSortHelper(head, tail)
    return head

# Example usage
head = Node(30)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(20)
head.next.next.next.next = Node(5)

head = quickSort(head)
printList(head)

# QuickSort on Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Function to swap data between two nodes
def swap(a, b):
    a.data, b.data = b.data, a.data

# Partition function for quicksort
def partition(low, high):
    pivot = high.data
    i = low.prev
    curr = low

    while curr != high:
        if curr.data <= pivot:
            i = low if i is None else i.next
            swap(i, curr)
        curr = curr.next

    i = low if i is None else i.next
    swap(i, high)
    return i

# Recursive quicksort
def quick_sort(low, high):
    if low and high and low != high and low != high.next:
        pivot = partition(low, high)
        quick_sort(low, pivot.prev)
        quick_sort(pivot.next, high)

# Function to get the last node
def get_last_node(head):
    while head and head.next:
        head = head.next
    return head

# Function to print list
def print_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

if __name__ == '__main__':
    # Create the doubly linked list: 5 <-> 3 <-> 4 <-> 1
    head = Node(5)
    second = Node(3)
    third = Node(4)
    fourth = Node(1)

    # Linking the nodes
    head.next = second
    second.prev = head
    second.next = third
    third.prev = second
    third.next = fourth
    fourth.prev = third

    # Perform quicksort
    last = get_last_node(head)
    quick_sort(head, last)

    # Print sorted list
    print_list(head)
  
# Nuts & Bolts Problem (Lock & Key problem) using Quick Sort

from typing import List

def printArray(arr: List[str]) -> None:
    print(" ".join(arr))

def partition(arr: List[str], low: int, high: int, pivot: str) -> int:
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif arr[j] == pivot:
            arr[j], arr[high] = arr[high], arr[j]
            j -= 1  # Re-check swapped item
    arr[i], arr[high] = arr[high], arr[i]
    return i  # Pivot final position

def matchPairs(nuts: List[str], bolts: List[str], low: int, high: int) -> None:
    if low < high:
        # Partition nuts with last bolt as pivot
        pivot_index = partition(nuts, low, high, bolts[high])
        
        # Partition bolts with the nut at pivot_index
        partition(bolts, low, high, nuts[pivot_index])

        # Recurse for subarrays
        matchPairs(nuts, bolts, low, pivot_index - 1)
        matchPairs(nuts, bolts, pivot_index + 1, high)

if __name__ == "__main__":
    nuts = ['@', '#', '$', '%', '^', '&']
    bolts = ['$', '%', '&', '^', '@', '#']
    
    matchPairs(nuts, bolts, 0, len(nuts) - 1)

    print("Matched nuts and bolts:")
    printArray(nuts)
    printArray(bolts)




# Adaptive quick sort Algorithm

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def is_sorted(arr, low, high):
    for i in range(low, high - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def quick_sort(arr, low, high):
    if is_sorted(arr, low, high):
        return
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    print(arr)

    
