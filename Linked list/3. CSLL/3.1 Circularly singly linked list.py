"""

Operations on the Circular Linked list

1. Insertion
      a. Insertion at the empty list
      b. Insertion at the beginning
      c. Insertion at the end
      d. Insertion at the given position
      
2. Deletion
      a. Delete the first node
      b. Delete the node from any position
      c. Delete the last node

3. Searching

4. Printing the Contents of Circularly linked list


"""

# Insertion in the circular linked list

#+______________________________________________________________________________________________________________________+

# a. Insertion in an empty List in the circular linked list

class Node:
    def __init__(self, value):
        self.data = value
        self.next = self                              # Point to itself

def insertInEmptyList(last, data):
    if last is not None:
        return last
    
    new_node = Node(data)
    
    last = new_node                                  # Update last to point to the new node
    return last


if __name__ == "__main__":
    last = None
    last = insertInEmptyList(last, 1)      # Insert a node into the empty list
  
    printList(last)

"""
Time Complexity: O(1)
Auxiliary Space: O(1)

"""

#+______________________________________________________________________________________________________________________+

# b. Insertion at the beginning in circular linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to insert a node at the beginning of the circular linked list

def insert_at_beginning(last, value):
    new_node = Node(value)

    if last is None:                            # If the list is empty, make the new node point to itself and set it as last
        new_node.next = new_node
        return new_node

    new_node.next = last.next                   # Insert the new node at the beginning
    last.next = new_node

    return last

# Create circular linked list: 2, 3, 4

first = Node(2)
first.next = Node(3)
first.next.next = Node(4)
last = first.next.next
last.next = first

last = insert_at_beginning(last, 5)

print_list(last)


"""
Time Complexity: O(1)
Auxiliary Space: O(1)

"""

#+______________________________________________________________________________________________________________________+

# c. Insertion at the end

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# Function to insert a node at the end of a circular linked list

def insert_end(tail, value):
    new_node = Node(value)
  
    if tail is None:

        tail = new_node                        # If the list is empty, initialize it with the new node
        new_node.next = new_node
      
    else:

        new_node.next = tail.next              # Insert new node after the current tail and update the tail pointer
        tail.next = new_node
        tail = new_node
      
    return tail


if __name__ == "__main__":
  
    # Create circular linked list: 2, 3, 4
    first = Node(2)
    first.next = Node(3)
    first.next.next = Node(4)

    last = first.next.next
    last.next = first

    # Insert elements at the end of the circular linked list
    last = insert_end(last, 5)
    last = insert_end(last, 6)

    print("List after inserting 5 and 6: ", end="")
    print_list(last)
  

"""
Time Complexity: O(1)
Auxiliary Space: O(1)

"""

#+______________________________________________________________________________________________________________________+

# d. Insertion at the given position

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# Function to insert a node at a specific position in a circular linked list

def insertAtPosition(last, data, pos):
  
    if last is None:

        if pos != 1:                                                # If the list is empty
            print("Invalid position!")
            return last

        new_node = Node(data)                                       # Create a new node and make it point to itself
      
        last = new_node
        last.next = last
      
        return last

    new_node = Node(data)                                           # Create a new node with the given data

    curr = last.next                                                # curr will point to head initially

    if pos == 1:                                                    # Insert at the beginning

        new_node.next = curr
        last.next = new_node
        return last

    for i in range(1, pos - 1):                                    # Traverse the list to find the insertion point
        curr = curr.next

        if curr == last.next:                                      # If position is out of bounds
            print("Invalid position!")
            return last

    new_node.next = curr.next                                      # Insert the new node at the desired position
    curr.next = new_node

    if curr == last:                                               # Update last if the new node is inserted at the end
        last = new_node

    return last


if __name__ == "__main__":
  
    # Create circular linked list: 2, 3, 4
    first = Node(2)
    first.next = Node(3)
    first.next.next = Node(4)

    last = first.next.next
    last.next = first

    # Insert elements at specific positions
    data = 5
    pos = 2
  
    last = insertAtPosition(last, data, pos)

    print_list(last)
  

"""
✅ Time Complexity of Insertion at Given Position in DLL

Best Case (insertion at beginning or end, if pointers are known):
🔹 O(1)

Average / Worst Case (insertion at arbitrary position pos):
🔹 O(n) — because you may need to traverse up to pos nodes to find the insertion point.



✅ Space Complexity: O(1)

Only one new node is created.

No extra space is used apart from a few pointers.

"""


#+______________________________________________________________________________________________________________________+

# 2. Deletion

# a. Delete the first node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteFirstNode(last):
  
    if last is None:                                        # If the list is empty
        print("List is empty")
        return None

    head = last.next

    if head == last:                                       # If there is only one node in the list
        last = None
      
    else:                                                  # More than one node in the list
        last.next = head.next

    return last


# Create circular linked list: 2, 3, 4
first = Node(2)
first.next = Node(3)
first.next.next = Node(4)

last = first.next.next
last.next = first

# Delete the first node
last = deleteFirstNode(last)

print_list(last)


"""
| Time Complexity | Space Complexity |
| --------------- | ---------------- |
| O(1)            | O(1)             |

"""

#+______________________________________________________________________________________________________________________+

# b. Delete a specific node in circular linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteSpecificNode(last, key):
  
    if last is None:                                                  # If the list is empty
        print("List is empty, nothing to delete.")
        return None

    curr = last.next
    prev = last

    if curr == last and curr.data == key:                             # If the node to be deleted is the only node in the list
        last = None
        return last

    if curr.data == key:                                              # If the node to be deleted is the first node
        last.next = curr.next
        return last

    while curr != last and curr.data != key:                          # Traverse the list to find the node to be deleted
        prev = curr
        curr = curr.next

    if curr.data == key:                                              # If the node to be deleted is found
        prev.next = curr.next
        if curr == last:
            last = prev
          
    else:                                                             # If the node to be deleted is not found
        print(f"Node with data {key} not found.")

    return last
  

# Create circular linked list: 2, 3, 4
first = Node(2)
first.next = Node(3)
first.next.next = Node(4)

last = first.next.next
last.next = first

# Delete a specific node
key = 3
last = deleteSpecificNode(last, key)

printList(last)

"""

| Case                             | Time Complexity | Space Complexity |
| -------------------------------- | --------------- | ---------------- |
| Delete first node                | O(1)            | O(1)             |
| Delete middle/last node          | O(n)            | O(1)             |
| Key not found                    | O(n)            | O(1)             |
| List is empty or has one element | O(1)            | O(1)             |

"""

#+__________________________________________________________________________________________________________________+

# c. Deletion at the end of Circular linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteLastNode(last):
  
    if last is None:                                                              # If the list is empty
        print("List is empty, nothing to delete.")
        return None

    head = last.next

    if head == last:                                                              # If there is only one node in the list
        last = None
        return last

    curr = head                                                                   # Traverse the list to find the second last node
  
    while curr.next != last:
        curr = curr.next

    curr.next = head                                                             # Update the second last node's next pointer to point to head
    last = curr

    return last


# Create circular linked list: 2, 3, 4
first = Node(2)
first.next = Node(3)
first.next.next = Node(4)

last = first.next.next
last.next = first

# Delete the last node
last = deleteLastNode(last)

printList(last)


"""
| Case                            | Time Complexity | Space Complexity |
| ------------------------------- | --------------- | ---------------- |
| List is empty / one node        | O(1)            | O(1)             |
| General case                    | O(n)            | O(1)             |

"""

#+__________________________________________________________________________________________________________________+

# 3. Searching

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def search_circular_list(last, key):
    if last is None:
        return False

    current = last.next  # Start from head
    while True:
        if current.data == key:
            return True
        current = current.next
        if current == last.next:  # Completed a full circle
            break
    return False

# Example: Create CSLL with nodes 2 → 3 → 4
first = Node(2)
second = Node(3)
third = Node(4)

first.next = second
second.next = third
third.next = first  # Make it circular
last = third        # Mark last node

# Search for a key
key = 3
found = search_circular_list(last, key)
print(f"Key {key} found?" , found)

"""

| Case                            | Time Complexity | Space Complexity | Description                                  |
| ------------------------------- | --------------- | ---------------- | -------------------------------------------- |
| List is empty                   | O(1)            | O(1)             | Immediate check returns `False`              |
| Key found at head (`last.next`) | O(1)            | O(1)             | First node matches                           |
| Key found at middle/end         | O(n)            | O(1)             | Traverse through list until key found        |
| Key not present                 | O(n)            | O(1)             | Traverse entire list once to confirm absence |


"""


#+__________________________________________________________________________________________________________________+

# 4. Printing the Contents of Circularly linked list

def printList(last):
  
    if last is None:
        print("List is Empty")
        return

    head = last.next
  
    while True:
      
        print(head.data, end=" ")
      
        head = head.next
      
        if head == last.next:
            break
          
    print()


"""
| Operation  | Time Complexity | Space Complexity |
| ---------- | --------------- | ---------------- |
| Print CSLL | O(n)            | O(1)             |

"""
#+__________________________________________________________________________________________________________________+
















