# Python program for implementation of Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
              
        if i != min_idx:  # ✅ Only swap when needed
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
  
#Stable Selection Sort code

def stable_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            min_value = arr[min_index]
            for k in range(min_index, i, -1):
                arr[k] = arr[k - 1]
            arr[i] = min_value
    return arr
  
"""

🔍 Step-by-step:
Initial: [4a, 2a, 3, 2b, 1]

Pass 1: Min = 1 → insert at index 0, shift everything
→ [1, 4a, 2a, 3, 2b]

Pass 2: Min = 2a → insert at index 1, shift
→ [1, 2a, 4a, 3, 2b]

Pass 3: Min = 2b → insert at index 2, shift
→ [1, 2a, 2b, 4a, 3]

Pass 4: Min = 3 → insert at index 3
→ [1, 2a, 2b, 3, 4a]

✅ Stable result: [1, 2a, 2b, 3, 4a]


Step-by-step with the loop:

for k in range(4, 1, -1):
    arr[k] = arr[k - 1]
    
The loop runs like this:

k = 4 → arr[4] = arr[3] → arr becomes [1, 2a, 4a, 3, 3]

k = 3 → arr[3] = arr[2] → arr becomes [1, 2a, 4a, 4a, 3]

k = 2 → arr[2] = arr[1] → arr becomes [1, 2a, 2a, 4a, 3]

"""

#Using Recursion


def selection_sort_recursive(arr, i=0):
    n = len(arr)
    if i >= n - 1:
        return
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    if min_idx != i:  # Swap only if needed
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    selection_sort_recursive(arr, i + 1)


def stable_selection_sort_recursive(arr, start=0):
    n = len(arr)
    if start >= n - 1:
        return
    
    min_index = start
    for i in range(start + 1, n):
        if arr[i] < arr[min_index]:
            min_index = i

    if min_index != start:
        min_value = arr[min_index]
    
        for k in range(min_index, start, -1):
            arr[k] = arr[k - 1]
        arr[start] = min_value
    
    stable_selection_sort_recursive(arr, start + 1)

# Iterative selection sort for linked list

# 1. Swapping Node Values (Easy & Optimized)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def selection_sort_swap_values(head):
    current = head
    while current:
        min_node = current
        searcher = current.next
        while searcher:
            if searcher.data < min_node.data:
                min_node = searcher
            searcher = searcher.next
        
        if min_node != current:
            current.data, min_node.data = min_node.data, current.data
        
        current = current.next
    return head
  
# 2.Changing Node Links (Easy & Optimized)


def selection_sort_change_links(head):
    if not head or not head.next:
        return head

    sorted_head = None  # Start with empty sorted list

    while head:
        min_node = head
        min_prev = None
        prev = None
        curr = head
        
        # Find min node and its previous node
        while curr:
            if curr.data < min_node.data:
                min_node = curr
                min_prev = prev
            prev = curr
            curr = curr.next
        
        # Remove min_node from original list
        if min_prev:
            min_prev.next = min_node.next
        else:
            head = min_node.next
        
        # Insert min_node at front of sorted list
        min_node.next = sorted_head
        sorted_head = min_node
    
    # Reverse sorted list to correct order
    prev = None
    curr = sorted_head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    return prev


# Program to sort an array of strings using Selection Sort

def selection_sort_strings(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap only if min_index is different
      
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = ["paper", "true", "soap", "floppy", "flower"]

print("Given array:")
print(arr)

sorted_arr = selection_sort_strings(arr)

print("\nSorted array:")
print(sorted_arr)

