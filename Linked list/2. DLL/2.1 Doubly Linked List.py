class Node:
  
    def __init__(self, data):
        self.data = data

        self.prev = None         # Reference to the previous node
        self.next = None         # Reference to the next node

"""

1. Traversal of Doubly Linked List
        a. Forward Traversal of Doubly Linked List
        b. Backward Traversal of Doubly Linked List
2. Searching in Doubly Linked List
3. Length of Doubly Linked List
4. Insertion in Doubly Linked List
        a.Insertion at the Beginning
        b.Insertion at the End 
        c.Insertion at a Specific Position
5. Deletion in Doubly Linked List
        a. Deletion at the Beginning
        b. Deletion at the End 
        c. Deletion at a Specific Position
        d. Deleting by Value
        e. Delete by Node 
6. Reversing a Doubly Linked List
7. Delete Entire List
 
"""

# --------------- +  ==================================================== + --------------- #


# 1. Traversal of doubly Linked List


# a. Forward Traversal of Doubly Linked List

# Iterative method

def forward_traversal(head):
    curr = head
    while curr is not None:
        
        print(curr.data, end=" ")        # Output data of the current node
        
        curr = curr.next                 # Move to the next node
    
    print()
  
forward_traversal(head)


"""

Time Complexity: O(n), where n is the number of nodes in the linked list
Auxiliary Space: O(1)

"""



# -------------------------------------------------------------------------------------------- #

# Recursive method

def forward_traversal(head):
    if head is None:
        return
    
    print(head.data, end=" ")          # Print current node's data
    
    forward_traversal(head.next)       # Recursive call with the next node

forward_traversal(head)

"""

Time Complexity: O(n), where n is the number of nodes in the linked list
Auxiliary Space: O(n)

"""

# -------------------------------------------------------------------------------------------- #

# b. Backward Traversal of Doubly Linked List

# Iterative method


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

def backward_traversal(tail):
    curr = tail
    
    while curr is not None:               # Traverse the list in backward direction
        print(curr.data, end=" ")         # Output data of the current node
        
        curr = curr.prev                  # Move to the previous node

if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list: 1 <-> 2 <-> 3
    head = Node(1)
    second = Node(2)
    third = Node(3)
    
    head.next = second
    second.prev = head
    second.next = third
    third.prev = second
    
    print("Backward Traversal: ", end="")
    backward_traversal(third)

"""

Time Complexity: O(n), where n is the number of nodes in the linked list
Auxiliary Space: O(1)

"""



# -------------------------------------------------------------------------------------------- #

# Recursive method - Backward Traversal 

# Doubly Linked List

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

def backward_traversal(node):
    if node is None:
        return

    print(node.data, end=" ")              # Print current node's data
      	
    backward_traversal(node.prev)          # Recursive call with the previous node

if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list: 1 <-> 2 <-> 3
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second

    backward_traversal(third)

"""

Time Complexity: O(n), where n is the number of nodes in the linked list
Auxiliary Space: O(n)


"""

# -------------------------------------------------------------------------------------------- #


 # Display List

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
      
    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# --------------- +  ==================================================== + --------------- #

# 2. Searching in doubly Linked List

def search_key(head, key):
    curr = head                # Start from the head of the doubly linked list

    while curr is not None:    # Traverse forward using the next pointer
        if curr.data == key:   # Check if current node matches the key
            return True
        curr = curr.next       # Move to the next node

    return False               # Reached end without finding the key


# -------------------------------------------------------------------------------------------- #

def searchKey(head, key):
    if head is None:                  # Base case: reached end of list
        return False

    if head.data == key:              # Check current node
        return True

    return searchKey(head.next, key)  # Move forward using .next

# --------------- +  ==================================================== + --------------- #

# 3. Length of  doubly Linked List


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

# This function returns the size of the linked list
def findSize(curr):
    size = 0
    while curr:
        size += 1
        curr = curr.next
    return size

if __name__ == "__main__":
  
    # Create a hard-coded doubly linked list: 1 <-> 2 <-> 3 <-> 4
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next

    print(findSize(head))

""" Approach - Using While Loop – O(n) Time and O(1) Space """
# -------------------------------------------------------------------------------------------- #


# Recursively count number of nodes in linked list
def findSize(head):
    if head is None:
        return 0
    return 1 + findSize(head.next)  # Recursive call

""" Using Recursion - O(n) Time and O(n) Space """
# -------------------------------------------------------------------------------------------- #
  
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
      
    def count_nodes(self):
        return self.length

# --------------- +  ==================================================== + --------------- #

"""

4. Insertion in doubly Linked List
        a.Insertion at the Beginning
        b.Insertion at the End 
        c.Insertion at a Specific Position
"""


# -------------------------------------------------------------------------------------------- #

# a.Insertion at the Beginning

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        self.prev = None

def insert_at_front(head, new_data):
  
    new_node = Node(new_data)                          # Create a new node

    new_node.next = head                               # Make next of new node as head

    if head is not None:                               # Change prev of head node to new node
        head.prev = new_node

    return new_node                                    # Return the new node as the head of the doubly linked list


if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list: 2 <-> 3 <-> 4 -> NULL
    head = Node(2)
    head.next = Node(3)
    head.next.prev = head
    head.next.next = Node(4)
    head.next.next.prev = head.next

    data = 1
    head = insert_at_front(head, data)

    print_list(head)                            # Print the updated list
  
""" 

Time Complexity: O(1)
Auxiliary Space: O(1)

"""


# Prepend (Insert at Beginning)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def prepend(self, data):
        new_node = Node(data)
        if self.head:  # If list is not empty
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        self.length += 1
      
# -------------------------------------------------------------------------------------------- #

# b.Insertion at the End 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insert_end(head, new_data):
  	
    new_node = Node(new_data)                                # Create a new node
    
    if head is None:                                         # If the linked list is empty, set the new node as the head
        head = new_node
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
      
        curr.next = new_node                                # Set the next of the last node to the new node
        
        new_node.prev = curr                                # Set the prev of the new node to the last node
    
    return head


if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list: 1 <-> 2 <-> 3
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next

    data = 4
    head = insert_end(head, data)

    print_list(head)                    # Print the updated list

 # Append (Insert at End)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
      
        new_node = Node(data)
      
        if not self.head:                # List is empty
            self.head = new_node
          
        else:
          
            current = self.head
          
            while current.next:          # Go to last node
                current = current.next
            current.next = new_node
            new_node.prev = current
          
        self.length += 1


"""

Time Complexity: O(N), where N is the number of nodes in the linked list.
Auxiliary Space: O(1)

"""

# -------------------------------------------------------------------------------------------- #
      
# c.Insertion at a Specific Position



def insert_pos(head, pos, data): # not 0-based index

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        self.prev = None

def insert_at_position(head, pos, new_data):
  
    new_node = Node(new_data)               # Create a new node

    if pos == 1:                            # Insertion at the beginning
        new_node.next = head

        if head is not None:                # If the linked list is not empty, set the prev of head to new node
            head.prev = new_node

        head = new_node
        return head                         # Set the new node as the head of the linked list
    
    # Traverse the list to find the node before the insertion point

    curr = head

    for _ in range(1, pos - 1):
        if curr is None:
            print("Position is out of bounds.")
            return head
        curr = curr.next

    if curr is None:                             # If the position is out of bounds
        print("Position is out of bounds.")
        return head

    new_node.prev = curr                        # Set the prev of new node to curr

    new_node.next = curr.next                   # Set the next of new node to next of curr

    curr.next = new_node                        # Update the next of current node to new node

    if new_node.next is not None:               # If the new node is not the last node, update prev of next node to new node
        new_node.next.prev = new_node

    return head

if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list: 1 <-> 2 <-> 4
  
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(4)
    head.next.next.prev = head.next

    # Insert new node with data 3 at position 3
    print("Inserting Node with data 3 at position 3: ", end="")
    data = 3
    pos = 3
    head = insert_at_position(head, pos, data)

    print_list(head)               # Print the updated list


  

# Insert at Position (0-based index)
  
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
      
    def insert_at_position(self, data, position):
      
        if position < 0 or position > self.length:
            print("Invalid position")
            return

        if position == 0:
            self.prepend(data)
          
        elif position == self.length:
            self.append(data)
          
        else:
            new_node = Node(data)
            current = self.head
          
            for _ in range(position - 1):
                current = current.next
              
            new_node.next = current.next
            new_node.prev = current
          
            current.next.prev = new_node
            current.next = new_node
          
            self.length += 1


"""
Time Complexity: O(N), where N is the number of nodes in doubly linked list
Auxiliary Space: O(1)

"""

# --------------- +  ==================================================== + --------------- #

"""

5. Deletion in doubly Linked List
        a. Deletion at the Beginning
        b. Deletion at the End 
        c. Deletion at a Specific Position
        d. Deleting by Value
        e. Delete by Node 
"""


# -------------------------------------------------------------------------------------------- #

# a. Deletion at the Beginning

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Function to delete the first node (head) of the list and return the second node as the new head

def del_head(head):
  
    if head is None:                              # If empty, return None
        return None

    temp = head                                   # Store in temp for deletion later

    head = head.next                              # Move head to the next node

    if head is not None:                          # Set prev of the new head
        head.prev = None

    return head                                   # Return new head


if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list: 1 <-> 2 <-> 3
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next

    head = del_head(head)

    print_list(head)
  
"""

Time Complexity: O(1)
Auxiliary Space: O(1)

"""


# Delete from Beginning

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
      
    def delete_from_beginning(self):
      
        if not self.head:
            print("List is empty")
            return
          
        temp = self.head
        self.head = self.head.next
      
        if self.head:
            self.head.prev = None
          
        del temp
        self.length -= 1


# -------------------------------------------------------------------------------------------- #

# b.Deletion at the End 

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def del_last(head):

    if head is None:                      # Corner cases
        return None
      
    if head.next is None:
        return None

    curr = head                          # Traverse to the last node
  
    while curr.next is not None:
        curr = curr.next

    if curr.prev is not None:            # Update the previous node's next pointer
        curr.prev.next = None

    return head                          # Return the updated head



if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list: 1 <-> 2 <-> 3
  
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next

    head = del_last(head)

    print_list(head)
  

 # Delete from End

class DoublyLinkedList:
  
    def __init__(self):
        self.head = None
        self.length = 0
      
    def delete_from_end(self):
      
        if not self.head:
            print("List is empty")
            return

        if not self.head.next:  # Only one node
            del self.head
            self.head = None
          
        else:
            current = self.head
          
            while current.next:
                current = current.next
              
            current.prev.next = None
            del current
          
        self.length -= 1
      
"""

Time Complexity: O(N), where N is the number of nodes in the linked list
Auxiliary Space: O(1)

"""

# -------------------------------------------------------------------------------------------- #
      
# c.Deletion at a Specific Position 

# Not 0-based index

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def del_pos(head, pos):

    if head is None:                    # If the list is empty
        return head

    curr = head

    for i in range(1, pos):
        if curr is None:
            break
        curr = curr.next

    if curr is None:
        return head

    if curr.prev is not None:           # If the list is empty
        curr.prev.next = curr.next

    if curr.next is not None:           # Update the next node's prev pointer
        curr.next.prev = curr.prev

    if head == curr:                    # If the node to be deleted is the head node
        head = curr.next

    del curr                            # Deallocate memory for the deleted node
    return head

if __name__ == "__main__":

    # Create a hardcoded doubly linked list: 1 <-> 2 <-> 3
  
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next

    head = del_pos(head, 2)

    print_list(head)
  
"""

Time Complexity: O(n), where n is the number of nodes in the doubly linked list.
Auxiliary Space: O(1)

"""

# Delete at Position (0-based index)

class DoublyLinkedList:
  
    def __init__(self):
        self.head = None
        self.length = 0
       
def delete_from_position(self, position):
  
    if position < 0 or position >= self.length:
        print("Invalid position")
        return

    if position == 0:
        self.delete_from_beginning()

    elif position == self.length - 1:
        self.delete_from_end()

    else:
      
        current = self.head
      
        for _ in range(position):
            current = current.next

        current.prev.next = current.next
        current.next.prev = current.prev

        # It's good practice to manually break links before deletion
        current.prev = None
        current.next = None
      
        del current

        self.length -= 1



# -------------------------------------------------------------------------------------------- #

# d. Deleting by Value

    def delete_by_value(self, value):
      
        if not self.head:
            print("List is empty")
            return

        current = self.head
      
        while current:
            if current.data == value:
              
                if current == self.head:
                    self.delete_from_beginning()
                  
                elif current.next is None:
                    self.delete_from_end()
                  
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    del current
                    self.length -= 1
                return
              
            current = current.next
        print("Value not found")

# -------------------------------------------------------------------------------------------- #

# e. Delete by Node 

    def delete_by_node(self, node_to_delete):
      
        if not self.head or not node_to_delete:
            print("List is empty or node is None")
            return

        if node_to_delete == self.head:
            self.delete_from_beginning()
          
        elif node_to_delete.next is None:
            self.delete_from_end()
          
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev
          
            del node_to_delete
          
            self.length -= 1


# --------------- +  ==================================================== + --------------- #
  
# 6. Reversing a Doubly Linked List


"""

-  a. [Naive Approach] Using Recursion - O(n) Time and O(n) Space
-  b. [Expected Approach] Using Two Pointers - O(n) Time and O(1) Space

"""


# -------------------------------------------------------------------------------------------- #


# a. [Naive Approach] Using Recursion - O(n) Time and O(n) Space

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

# Recursive function to reverse a doubly linked list

def reverse(curr):
  
    if curr is None:                          # Base case: if the list is empty or we reach the end of the list
        return None

    temp = curr.prev                          # Swap the next and prev pointers
    curr.prev = curr.next
    curr.next = temp

    if curr.prev is None:                     # If the previous node (after swap) is null, this is the new head
        return curr

    return reverse(curr.prev)                 # Recurse for the next node

if __name__ == "__main__":
  
    # Create a hard-coded doubly linked list: 1 <-> 2 <-> 3 <-> 4
  
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next

    head = reverse(head)
    print_list(head)
  
  # -------------------------------------------------------------------------------------------- #


# b. [Expected Approach] Using Two Pointers - O(n) Time and O(1) Space

# Python code to Reverse a doubly linked list, using two pointers

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        self.prev = None

def reverse(head):
  	
    if head is None or head.next is None:              # If the list is empty or has only one node, return the head as is
        return head

    prevNode = None
    currNode = head

    while currNode is not None:                        # Traverse the list and reverse the links
      
        prevNode = currNode.prev                       # Swap the next and prev pointers
        currNode.prev = currNode.next
        currNode.next = prevNode
        
        # Move to the next node in the original list (which is now previous due to reversal)
      
        currNode = currNode.prev

    return prevNode.prev                              # The final node in the original list becomes the new head after reversal

if __name__ == "__main__":
  	
    # Create a doubly linked list: 1 <-> 2 <-> 3 <-> 4
  
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next

    head = reverse(head)
  
    printList(head)
  

# ___________________________________________________________________________________________________________________________#

# Reverse the Linked List

# Reversing both Sll and Dll (iteratively and recursively)

# DLL Node
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Reverse DLL - Iterative
def reverse_dll_iterative(head):
    current = head
    prev = None
    while current:
        current.prev, current.next = current.next, current.prev
        prev = current
        current = current.prev
    return prev

# Reverse DLL - Recursive
def reverse_dll_recursive(head):
    if head is None:
        return None
    head.prev, head.next = head.next, head.prev
    if head.prev is None:
        return head
    return reverse_dll_recursive(head.prev)

if __name__ == "__main__":


    # DLL Creation: 10 <-> 20 <-> 30 <-> None
    dll_head = DLLNode(10)
    dll_second = DLLNode(20)
    dll_third = DLLNode(30)
  
    dll_head.next = dll_second
    dll_second.prev = dll_head
    dll_second.next = dll_third
    dll_third.prev = dll_second

    print("\nOriginal DLL:")
    print_dll(dll_head)

    dll_head = reverse_dll_iterative(dll_head)
    print("DLL Reversed Iteratively:")
    print_dll(dll_head)

    dll_head = reverse_dll_recursive(dll_head)
    print("DLL Reversed Recursively:")
    print_dll(dll_head)

# +_________________________________________________________________________________________________________________+

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

  
    # Reverse DLL - Iterative
    def reverse_iterative(self):
      
        current = self.head
        prev = None
      
        while current:
            current.prev, current.next = current.next, current.prev
            prev = current
            current = current.prev
          
        self.head = prev

  
    # Reverse DLL - Recursive

    def _reverse_dll_recursive(self, head):
      
      if head is None:
          return None
        
      head.prev, head.next = head.next, head.prev
      
      if head.prev is None:
          return head
        
      return self._reverse_dll_recursive(head.prev)


    def reverse_recursive(self):
        self.head = self._reverse_dll_recursive(self.head)




# --------------- +  ==================================================== + --------------- #

# 7. Delete Entire List

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
      
    def clear(self):
        self.head = None
        self.length = 0
        print("List has been cleared.")

# --------------- +  ==================================================== + --------------- #

