# Using for loop alone
def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):         # Last i elements are already in place
            if arr[j] > arr[j+1]:         # Traverse the array from 0 to n-i-1
                arr[j], arr[j+1] = arr[j+1], arr[j]             # Swap if the element found is greater than the next element
                swapped = True
        if (swapped == False):
            break

# Using while loop alone

def bubble_sort_while(arr):
    n = len(arr)
    swapped = True
    i = 0
    while swapped:
        swapped = False
        j = 0
        while j < n - i - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            j += 1
        i += 1
    return arr

# Using for and While loop

def bubble_sort_for_while(arr):
    n = len(arr)
    i = 0
    while i < n:
        # Inner loop using for
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if needed
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        i += 1
    return arr
  
# Adding a swapped flag makes the bubble sort more efficient by stopping early if no swaps occur during a pass — which means the list is already sorted.

def bubble_sort_for_while(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
    return arr

# Recursive algorithm

def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    
    # Base case: If array size is 1, return
    if n == 1:
        return arr

    # One pass of bubble sort
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # Recursive call for remaining array
    return bubble_sort_recursive(arr, n - 1)


# Bubble Sort for Linked List by Swapping nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubble_sort_linked_list(head):
    if not head or not head.next:
        return head

    changed = True
    while changed:
        changed = False
        prev = None
        curr = head

        while curr.next:
            nxt = curr.next
            if curr.data > nxt.data:
                changed = True
                # Swap nodes (not data)
                if prev:
                    prev.next = nxt
                else:
                    head = nxt
                curr.next = nxt.next
                nxt.next = curr
                prev = nxt
            else:
                prev = curr
                curr = curr.next
    return head

# Helper to print list
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Example usage
nodes = [Node(4), Node(3), Node(1), Node(2)]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
head = nodes[0]

print("Before sorting:")
print_list(head)

head = bubble_sort_linked_list(head)

print("After sorting:")
print_list(head)

# Sorting Strings using Bubble Sort

def bubble_sort_strings(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
arr = ["GeeksforGeeks", "Quiz", "Practice", "Gblogs", "Coding"]
bubble_sort_strings(arr)

print("Sorted strings:")
for s in arr:
    print(s)


# Sort an array using Bubble Sort without using loops

def bubble_sort_full_recursive(arr, n=None, i=0):
    if n is None:
        n = len(arr)

    # Base case
    if n == 1:
        return

    # If we reached the end of one pass, call for next pass
    if i == n - 1:
        bubble_sort_full_recursive(arr, n - 1, 0)
        return

    # Swap if needed
    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursive call for next comparison
    bubble_sort_full_recursive(arr, n, i + 1)


# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_full_recursive(arr)
print("Sorted array is:", arr)

# Bubble Sort On Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def bubble_sort(self):
        if not self.head:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head

            while current.next:
                if current.data > current.next.data:
                    # Swap data
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "")
            current = current.next
        print()

# Example usage:
dll = DoublyLinkedList()
for value in [4, 3, 1, 5, 2]:
    dll.append(value)

print("Before sorting:")
dll.print_list()

dll.bubble_sort()

print("After sorting:")
dll.print_list()

# Bubble sort using two Stacks

def bubble_sort_two_stacks(stack1):
    n = len(stack1)
    for i in range(n):
        swapped = False
        stack2 = []
        prev = None

        # Move elements from stack1 to stack2, swapping if needed
        while stack1:
            curr = stack1.pop()
            if prev is not None and prev > curr:
                # Swap elements
                stack2.append(prev)
                prev = curr
                swapped = True
            else:
                if prev is not None:
                    stack2.append(prev)
                prev = curr

        # Push the last saved element
        if prev is not None:
            stack2.append(prev)

        # Move back to stack1 for next pass
        while stack2:
            stack1.append(stack2.pop())

        if not swapped:
            break

# Example usage:
stack = [3, 1, 4, 2, 5]  # Bottom is left, top is right
print("Original stack (top right):", stack)

bubble_sort_two_stacks(stack)
print("Sorted stack (top right):", stack)














