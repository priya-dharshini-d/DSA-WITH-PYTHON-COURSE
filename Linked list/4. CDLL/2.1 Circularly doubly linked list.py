"""
Operations on the Circular Doubly Linked List

1. Insertion
      a. Insertion at the beginning
      b. Insertion at the end
      c. Insertion at the given position

2. Deletion
      a. Delete from the beginning
      b. Delete from the end
      c. Delete from the given position

3. Searching

4. Printing the Circular Doubly Linked List (forward and backward)
"""

#+______________________________________________________________________________________________________________________+

# Node class for Circular Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self
        self.next = self


#+______________________________________________________________________________________________________________________+

# a. Insertion at the beginning

def insert_at_beginning(last, data):
    new_node = Node(data)

    if last is None:
        return new_node

    head = last.next
    new_node.next = head
    new_node.prev = last
    head.prev = new_node
    last.next = new_node

    return last

"""
| Operation               | Time Complexity | Space Complexity |
|------------------------|-----------------|------------------|
| Insert at beginning    | O(1)            | O(1)             |
"""

#+______________________________________________________________________________________________________________________+

# b. Insertion at the end

def insert_at_end(last, data):
    new_node = Node(data)

    if last is None:
        return new_node

    head = last.next
    new_node.next = head
    new_node.prev = last
    last.next = new_node
    head.prev = new_node

    return new_node  # Update last pointer

"""
| Operation            | Time Complexity | Space Complexity |
|---------------------|-----------------|------------------|
| Insert at end       | O(1)            | O(1)             |
"""

#+______________________________________________________________________________________________________________________+

# c. Insertion at a given position (1-based index)

def insert_at_position(last, pos, data):
    if pos <= 0:
        print("Invalid position.")
        return last

    if last is None:
        if pos == 1:
            return Node(data)
        else:
            print("Invalid position on empty list.")
            return last

    if pos == 1:
        return insert_at_beginning(last, data)

    temp = last.next
    for _ in range(pos - 2):
        temp = temp.next
        if temp == last.next:
            print("Position out of bounds.")
            return last

    new_node = Node(data)
    new_node.next = temp.next
    new_node.prev = temp
    temp.next.prev = new_node
    temp.next = new_node

    if temp == last:
        last = new_node

    return last

"""
| Operation               | Time Complexity | Space Complexity |
|------------------------|-----------------|------------------|
| Insert at position p   | O(n)            | O(1)             |
"""

#+______________________________________________________________________________________________________________________+

# a. Delete from beginning

def delete_from_beginning(last):
    if last is None:
        return None

    if last == last.next:
        return None

    head = last.next
    new_head = head.next
    last.next = new_head
    new_head.prev = last

    return last

"""
| Operation               | Time Complexity | Space Complexity |
|------------------------|-----------------|------------------|
| Delete from beginning  | O(1)            | O(1)             |
"""

#+______________________________________________________________________________________________________________________+

# b. Delete from end

def delete_from_end(last):
    if last is None:
        return None

    if last == last.next:
        return None

    prev_node = last.prev
    prev_node.next = last.next
    last.next.prev = prev_node

    return prev_node  # Update last

"""
| Operation         | Time Complexity | Space Complexity |
|------------------|-----------------|------------------|
| Delete from end  | O(1)            | O(1)             |
"""

#+______________________________________________________________________________________________________________________+

# c. Delete from given position

def delete_from_position(last, pos):
    if last is None or pos <= 0:
        return last

    if pos == 1:
        return delete_from_beginning(last)

    curr = last.next
    for _ in range(pos - 1):
        curr = curr.next
        if curr == last.next:
            print("Position out of bounds.")
            return last

    curr.prev.next = curr.next
    curr.next.prev = curr.prev

    if curr == last:
        last = curr.prev

    return last

"""
| Operation               | Time Complexity | Space Complexity |
|------------------------|-----------------|------------------|
| Delete from position p | O(n)            | O(1)             |
"""

#+______________________________________________________________________________________________________________________+

# 3. Searching

def search_cdll(last, key):
    if last is None:
        return False

    curr = last.next
    while True:
        if curr.data == key:
            return True
        curr = curr.next
        if curr == last.next:
            break

    return False

"""
| Case                | Time Complexity | Space Complexity |
|---------------------|-----------------|------------------|
| Key found/not found | O(n)            | O(1)             |
"""

#+______________________________________________________________________________________________________________________+

# 4. Printing forward and reverse

def print_forward(last):
    if last is None:
        print("List is empty.")
        return

    curr = last.next
    print("Forward:", end=" ")
    while True:
        print(curr.data, end=" ")
        curr = curr.next
        if curr == last.next:
            break
    print()

def print_backward(last):
    if last is None:
        print("List is empty.")
        return

    curr = last
    print("Backward:", end=" ")
    while True:
        print(curr.data, end=" ")
        curr = curr.prev
        if curr == last:
            break
    print()

"""
| Operation    | Time Complexity | Space Complexity |
|--------------|-----------------|------------------|
| Print forward| O(n)            | O(1)             |
| Print reverse| O(n)            | O(1)             |
"""

#+______________________________________________________________________________________________________________________+

# Sample usage

if __name__ == "__main__":
    last = None
    last = insert_at_end(last, 10)
    last = insert_at_end(last, 20)
    last = insert_at_end(last, 30)
    last = insert_at_beginning(last, 5)
    last = insert_at_position(last, 3, 15)

    print_forward(last)
    print_backward(last)

    last = delete_from_position(last, 3)
    last = delete_from_beginning(last)
    last = delete_from_end(last)

    print_forward(last)
    print("Search 20:", search_cdll(last, 20))
    print("Search 100:", search_cdll(last, 100))

