# Python program for implementation of Insertion sort.
def insertionSort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i-1
        while j >= 0 and curr < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = curr


arr = [12, 11, 13, 5, 6]
insertionSort(arr)



# Recursive function to sort an array using insertion sort


"""
✅ Recursive Insertion Sort Logic (Simplified)

Base Case:
If the array size is 1, it's already sorted. → So, do nothing and return.

Recursive Step:
Recursively sort the first n-1 elements of the array.

Insertion Step:
Take the n-th element (which is arr[n-1]) and insert it into its correct position in the already sorted subarray of size n-1."""


def recursiveInsertionSort(arr, n):
    if n <= 1:                      # Base case: if array has 1 or no elements, it's already sorted
        return
      
    recursiveInsertionSort(arr, n - 1)   # Sort first n-1 elements

    last = arr[n - 1]  # Insert last element at its correct position in sorted array
    j = n - 2

    while j >= 0 and arr[j] > last:     # Move elements greater than last one position ahead
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last


arr = [12, 11, 13, 5, 6]
recursiveInsertionSort(arr, len(arr))




# Python Program implementation of binary insertion sort


def binary_search(arr, val, start, end):
    
    # we need to distinguish whether we should insert before or after the left boundary. 
    # imagine [0] is the last step of the binary search and we need to decide where to insert -1
  
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1

    # this occurs if we are moving beyond left's boundary meaning 
    # the left boundary is the least position to find a number greater than val
  
    if start > end:
        return start

    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid


def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr

# Recursive implementation

def binarySearch(a, item, low, high):
    while (low <= high):
        mid = low + (high - low) // 2
        if (item == a[mid]):
            return mid + 1
        elif (item > a[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return low
    
# Function to sort an array a[] of size 'n'
def insertionSort(a, n):
    for i in range (n): 
        j = i - 1
        selected = a[i]
        
        # find location where selected should be inserted
        loc = binarySearch(a, selected, 0, j)
        
        # Move all elements after location to create space
        while (j >= loc):
            a[j + 1] = a[j]
            j-=1
        a[j + 1] = selected

# Driver Code
a = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
n = len(a)
insertionSort(a, n)


# Function to sort odd and even positioned elements separately using insertion sort

def evenOddInsertionSort(arr, n):
    # Sort odd-positioned elements (i.e., even indices) in descending order
    for i in range(2, n, 2):
        temp = arr[i]
        j = i - 2
        while j >= 0 and arr[j] < temp:  # descending
            arr[j + 2] = arr[j]
            j -= 2
        arr[j + 2] = temp

    # Sort even-positioned elements (i.e., odd indices) in ascending order
    for i in range(3, n, 2):
        temp = arr[i]
        j = i - 2
        while j >= 1 and arr[j] > temp:  # ascending
            arr[j + 2] = arr[j]
            j -= 2
        arr[j + 2] = temp

# Function to print the array
def printArray(arr):
    print(" ".join(str(x) for x in arr))

# Example usage
arr = [7, 10, 11, 3, 6, 9, 2, 13, 0]      # Output: 11 3 7 9 6 10 2 13 0
evenOddInsertionSort(arr, len(arr))
printArray(arr)

# Count swaps required to sort an array using Insertion Sort

def insertionSortSwaps(arr):
    swaps = 0
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1  # Count the shift as a swap

        arr[j + 1] = key

    return swaps

# Example usage
arr = [2, 1, 3, 1, 2]
print(insertionSortSwaps(arr))  # Output: 4


# Linked list implementation

# Node definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List definition
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end for testing purposes
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node

    # Print linked list
    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    # Insertion sort for linked list
    def insertionSort(self):
        sorted_head = None  # Start with empty sorted list
        current = self.head

        while current:
            next_node = current.next  # Save next node
            sorted_head = self.sortedInsert(sorted_head, current)
            current = next_node

        self.head = sorted_head  # Update head to new sorted list

    # Helper function to insert a node into sorted linked list
    def sortedInsert(self, head, node):
        if head is None or node.data < head.data:
            node.next = head
            return node
        else:
            current = head
            while current.next and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
        return head

ll = LinkedList()
for value in [12, 11, 13, 5, 6]:
    ll.append(value)

print("Original List:")
ll.printList()

ll.insertionSort()

print("Sorted List:")
ll.printList()

"""
Output:

Original List:
12 11 13 5 6 
Sorted List:
5 6 11 12 13 

"""
