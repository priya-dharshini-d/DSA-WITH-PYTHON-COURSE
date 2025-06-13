# Definition of a Node in a singly linked list

class Node:
    def __init__(self, data):
       # Data part of the node
        self.data = data   
        self.next = None    
      
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0  # initialize length
      
"""
1. Traversal of Singly Linked List
2. Searching in Singly Linked List
3. Length of Singly Linked List
4. Insertion in Singly Linked List
        a.Insertion at the Beginning
        b.Insertion at the End 
        c.Insertion at a Specific Position
5. Deletion in Singly Linked List
        a. Deletion at the Beginning
        b. Deletion at the End 
        c. Deletion at a Specific Position
        d. Deleting by Value
        e. Delete by Node 
6. Modify a Singly Linked List
7. Reversing a Singly Linked List
8. Delete Entire List
 
"""

# --------------- +  ==================================================== + --------------- #


# 1. Traversal of Singly Linked List


def traverseList(head):             # or define it as print_list(head) for printing the data

    while head is not None:         # A loop that runs till head is nullptr

        print(head.data, end=" ") 	# Printing data of current node
        
        head = head.next 		        # Moving to the next node
      
    print()

"""

Time Complexity: O(n), where n is the number of nodes in the linked list.
Auxiliary Space: O(1)

"""



# -------------------------------------------------------------------------------------------- #



def traverseList(head):
  
    if head is None:  # Base condition is when the head is nullptr
        print()
        return
      
    print(head.data, end=" ")
    
    traverseList(head.next)     # Moving to the next node

"""

Time Complexity: O(n), where n is number of nodes in the linked list.
Auxiliary Space: O(n) because of recursive stack space.

"""


# -------------------------------------------------------------------------------------------- #


 # Display List
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0  # initialize length
      
    def display(self):
        current = self.head
        if not current:
            print("List is empty")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# --------------- +  ==================================================== + --------------- #

# 2. Searching in Singly Linked List

def search_key(head, key):
  
    curr = head                 # Initialize curr with the head of linked list

    while curr is not None:     # Iterate over all the nodes

        if curr.data == key:    # If the current node's value is equal to key, return true
            return True

        curr = curr.next        # Move to the next node

    return False                # If there is no node with value as key, return false

# -------------------------------------------------------------------------------------------- #

def searchKey(head, key):
  
    if head is None:         # Base case
        return False

    if head.data == key:     # If key is present in current node, return true
        return True

    return searchKey(head.next, key)     # Recur for remaining list




# --------------- +  ==================================================== + --------------- #

# 3. Length of Singly Linked List


def count_nodes(head):

    count = 0   # Counts number of nodes in linked list

    curr = head    # Initialize curr with head of Linked List

    while curr is not None: # Traverse till we reach None
       
        count += 1

        curr = curr.next  # Move pointer to next node

    return count
  
# -------------------------------------------------------------------------------------------- #


# Recursively count number of nodes in linked list
def count_nodes(head):

    if head is None:     # Base Case
        return 0

    return 1 + count_nodes(head.next)     # Count this node plus the rest of the list

# -------------------------------------------------------------------------------------------- #
  
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0  # initialize length
   
    def count_nodes(self):
        return self.length

# --------------- +  ==================================================== + --------------- #

"""

4. Insertion in Singly Linked List
        a.Insertion at the Beginning
        b.Insertion at the End 
        c.Insertion at a Specific Position
"""


# -------------------------------------------------------------------------------------------- #

# a.Insertion at the Beginning

def insert_at_front(head, new_data): 

    new_node = Node(new_data)
    new_node.next = head     # Make the next of the new node point to the current head
    return new_node     # Return the new node as the new head of the list

if __name__ == "__main__":  # Create the linked list 2->3->4->5
   
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)

    # Insert a new node at the front of the list

    data = 1
    head = insert_at_front(head, data) # Update the head pointer to point to the new node.
  
    print_list(head)  # Traversing the linked list from head and printing each node's data  i,e., use traverseList(head) here

"""

Time Complexity: 

O(1), We have a pointer to the head and we can directly attach a node and update the head pointer. 

So, the Time complexity of inserting a node at the head position is O(1).

Auxiliary Space: O(1)

"""


# Prepend (Insert at Beginning)

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0  # initialize length

    def prepend(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

# -------------------------------------------------------------------------------------------- #

# b.Insertion at the End 

def append(head, new_data):

    new_node = Node(new_data)

    if head is None:         # If the Linked List is empty, make the new node as the head and return
        return new_node

    last = head              # Store the head reference in a temporary variable
  
    while last.next:         # Traverse till the last node
        last = last.next

    last.next = new_node     # Change the next pointer of the last node to point to the new node

    return head              # Return the head of the list



# Driver code
if __name__ == "__main__":

    # Create a hard-coded linked list: 2 -> 3 -> 4 -> 5 -> 6
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(6)


    # Example of appending a node at the end
    head = append(head, 1)

    print_list(head)



 # Append (Insert at End)

class LinkedList:
  
    def __init__(self):
        self.head = None
        self.length = 0  

   
    def append(self, data):
      
        new_node = Node(data)
      
        if not self.head:
            self.head = new_node
          
        else:
            current = self.head
          
            while current.next:
                current = current.next
            current.next = new_node
          
        self.length += 1

"""

Time Complexity: O(N) where N is the length of the linked list
Auxiliary Space: O(1)

"""

# -------------------------------------------------------------------------------------------- #
      
# c.Insertion at a Specific Position



def insert_pos(head, pos, data): # not 0-based index
    
    # This condition to check whether the position given is valid or not.
    if pos < 1:
        return head

    if pos == 1:     # head will change if pos=1
        new_node = Node(data)
        new_node.next = head
        return new_node
    
    curr = head
    
    for _ in range(1, pos - 1):     # Traverse to the node that will be present just before the new node
        if curr == None:
            break
        curr = curr.next
        
    if curr is None:                # if position is greater number of nodes
        return head
    
    new_node = Node(data)
    
    new_node.next = curr.next       # update the next pointers
    curr.next = new_node
    
    return head
    


if __name__ == "__main__":  # Creating the list 3->5->8->10  
    
    head = Node(3)
    head.next = Node(5)
    head.next.next = Node(8)
    head.next.next.next = Node(10)

    data = 12
    pos = 3
  
    head = insert_pos(head, pos, data)
  
    print_list(head) # Output: 3 5 12 8 10 


    # Insert at Position (0-based index)
  
    def insert_at_position(self, data, position):
      
        if position > self.length or position < 0:
            print("Invalid position")
            return

        if position == 0:
            self.prepend(data)
          
        elif position == self.length:
            self.append(data)
          
        else:
          
            new_node = Node(data)
            count = 0
            current = self.head
          
            while count < position - 1:
                count += 1
                current = current.next
            new_node.next = current.next
            current.next = new_node
          
            self.length += 1


"""

new_node = Node(data)
current = self.head

for _ in range(position - 1):
    current = current.next

new_node.next = current.next
current.next = new_node

self.length += 1

"""



"""

Time Complexity: O(n), where n is the number of nodes in the linked list.
Auxiliary Space: O(1)

"""

# --------------- +  ==================================================== + --------------- #

"""

5. Deletion in Singly Linked List
        a. Deletion at the Beginning
        b. Deletion at the End 
        c. Deletion at a Specific Position
        d. Deleting by Value
        e. Delete by Node 
"""


# -------------------------------------------------------------------------------------------- #

# a. Deletion at the Beginning

# Delete the head node and return the new head
def delete_head(head):

    if head is None:             # Check if the list is empty
        return None

    temp = head                  # Store the current head in a temporary variable

    head = head.next             # Move the head pointer to the next node

    del temp                     # Delete the old head by removing the reference

    return head


if __name__ == "__main__":
   
    # Create a hard-coded linked list:  3 -> 12 -> 15 -> 18
    head = Node(3)
    head.next = Node(12)
    head.next.next = Node(15)
    head.next.next.next = Node(18)
  
    head = delete_head(head)
  
    print_list(head)
  
"""

Time Complexity: 

Time Complexity: O(1), because the operation to delete the head node is performed in constant time.
Space Complexity: O(1)

"""


# Delete from Beginning

class LinkedList:
  
    def __init__(self):
        self.head = None
        self.length = 0 

    def delete_from_beginning(self):
      
        if self.length == 0:
            print("List is empty")
          
        else:
          
            temp = self.head
            self.head = self.head.next
          
            del temp
            self.length -= 1


# -------------------------------------------------------------------------------------------- #

# b.Deletion at the End 


def remove_last_node(head):
  
    if not head:   # If the list is empty, return None
        return None

    if not head.next:  # If the list has only one node, delete it and return None
        return None

    second_last = head     # Find the second last node
  
    while second_last.next.next:
        second_last = second_last.next

    second_last.next = None     # Delete the last node

    return head

# Driver code
if __name__ == "__main__":

    # Creating a static linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)


    # Removing the last node
    head = remove_last_node(head)

    print_list(head)



 # Delete from End

class LinkedList:
  
    def __init__(self):
        self.head = None
        self.length = 0  

    def delete_from_end(self):
      
        if self.length == 0:
            print("List is empty")
            return

        if self.head.next is None:
            del self.head
            self.head = None
            self.length -= 1
            return

        current = self.head
        while current.next.next:
            current = current.next

        temp = current.next
        current.next = None
        del temp
      
        self.length -= 1

"""

Time Complexity: O(n), traversal of the linked list till its end, so the time complexity required is O(n).
Auxiliary Space: O(1)

"""

# -------------------------------------------------------------------------------------------- #
      
# c.Deletion at a Specific Position 


def deleteNode(head, position): # not 0-based index
    temp = head
    prev = None

    # Base case if linked list is empty
  
    if temp is None:
        return head

    # Case 1: Head is to be deleted
  
    if position == 1:
        head = temp.next
        return head

    # Case 2: Node to be deleted is in middle Traverse till given position
  
    for i in range(1, position):
        prev = temp
        temp = temp.next
      
        if temp is None:
            print("Data not present")
            return head

    # If given position is found, delete node
  
    if temp is not None:
        prev.next = temp.next

    return head


# Driver code
if __name__ == "__main__":
  
    # Creating a static linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
  
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Deleting node at position 2
    position = 2
    head = deleteNode(head, position)

    printList(head)  # List after deletion : 1 -> 3 -> 4 -> 5 -> nullptr

"""

Time Complexity: O(n), where n is the number of nodes in the list
Auxiliary Space: O(1)

"""

# Delete at Position (0-based index)

  class LinkedList:
  
    def __init__(self):
        self.head = None
        self.length = 0  

       
    def delete_from_position(self, position):
      
        if position < 0 or position >= self.length:
            print("Invalid position. Please enter a position between 0 and", self.length - 1)
            return

        if position == 0:
            self.delete_from_beginning()
            return

        if position == self.length - 1:
            self.delete_from_end()
            return

        current = self.head
        count = 0
        while count < position - 1:
            current = current.next
            count += 1

        temp = current.next
        current.next = temp.next
        del temp
        self.length -= 1


"""
current = self.head

for _ in range(position - 1):
    current = current.next
"""

# -------------------------------------------------------------------------------------------- #

# d. Deleting by Value

    def delete_by_value(self, value):
      
        if self.length == 0 or not self.head:
            print("List is empty")
            return

        if self.head.data == value:
            self.delete_from_beginning()
            return

        current = self.head
      
        while current.next:
          
            if current.next.data == value:
              
                temp = current.next
                current.next = temp.next
                del temp
              
                self.length -= 1
                return
              
            current = current.next

        print("Value not found")

# -------------------------------------------------------------------------------------------- #

# e. Delete by Node 

    def delete_by_node(self, node_to_delete):
      
        if self.head is None or self.length == 0:
            print("List is empty")
            return

        if self.head == node_to_delete:
            self.delete_from_beginning()
            return

        current = self.head
        while current.next and current.next != node_to_delete:
            current = current.next

        if current.next == node_to_delete:
            current.next = node_to_delete.next
            del node_to_delete
          
            self.length -= 1
            return

        print("Node not found in the list")

# --------------- +  ==================================================== + --------------- #
  
# 6. Modify a Singly Linked List

# Python program to modify a singly linked list By transferring it to an array

# Approach 1  Naive Approach Change Linked List to Array  - O(n) Time and O(n) Space

def countNodes(head):
    count = 0
    curr = head

    while curr is not None:
        count += 1
        curr = curr.next

    return count

def linkedListToArray(head, arr, n):
    curr = head

    for i in range(n):
        arr[i] = curr.data
        curr = curr.next

def arrayToLinkedList(arr, head, n):
    curr = head

    for i in range(n):
        curr.data = arr[i]
        curr = curr.next

def modifyArray(arr, n):  # Modify the array
  
    for i in range(n // 2):
        x = arr[i]
        arr[i] = arr[n - i - 1] - x
        arr[n - i - 1] = x

def modifyTheList(head):
    if head.next is None:
        return None

    n = countNodes(head)    # Count the number of nodes
    arr = [0] * n           # Create an array

    linkedListToArray(head, arr, n)  # Convert linked list to array
    modifyArray(arr, n)              # Modify the array

    arrayToLinkedList(arr, head, n) # Convert array back to linked list

    return head


if __name__ == "__main__":

    # Create a hard-coded linked list: 10 -> 4 -> 5 -> 3 -> 6 
    head = Node(10)
    head.next = Node(4)
    head.next.next = Node(5)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(6)

    head = modifyTheList(head)

    printList(head)

  # Output: -4 -1 5 4 10 


# -------------------------------------------------------------------------------------------- #

  
  # Approach 2: [Expected Approach] Reverse the 2nd Half Twice - O(n) Time and O(1) Space

# Python program to modify a singly linked list By Reversing the 2nd Half Twice 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to reverse a linked list iteratively

def reverse(head):
  
    prev = None
    curr = head

   
    while curr is not None:        # Traverse and reverse the linked list
        next_node = curr.next

        curr.next = prev           # Reverse the current node's pointer
        prev = curr
        curr = next_node

    return prev


def modifyTheList(head):
  
    if head.next is None:         # Returning head if list has only one node
        return head

    slow = head
    fast = head

   
    while fast.next is not None and fast.next.next is not None:  # Finding the middle node of the linked list
        slow = slow.next
        fast = fast.next.next

    mid = slow

    
    reversed_list = mid.next                     # Storing the second half of the list starting after the middle node

    mid.next = None                              # Splitting the list into two halves

    reversed_list = reverse(reversed_list)       # Reversing the second half of the list

    curr1 = head
    curr2 = reversed_list

    # Iterating over both halves of the list and modifying the values
  
    while curr2 is not None:
        x = curr1.data
        curr1.data = curr2.data - x
        curr2.data = x
        curr1 = curr1.next
        curr2 = curr2.next

    # Reversing the second half of the list again and connecting both halves
  
    mid.next = reverse(reversed_list)
    
    return head

if __name__ == "__main__":
  
    # Create a hard-coded linked list: 10 -> 4 -> 5 -> 3 -> 6
    head = Node(10)
    head.next = Node(4)
    head.next.next = Node(5)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(6)

    head = modifyTheList(head)

    print_list(head)

# --------------- +  ==================================================== + --------------- #
  
# 7. Reversing a Singly Linked List


"""

-  a. [Expected Approach]        Using Iterative Method - O(n) Time and O(1) Space
-  b. [Alternate Approach - 1]   Using Recursion - O(n) Time and O(n) Space
-  c. [Alternate Approach - 2]   Using Stack - O(n) Time and O(n) Space

"""


# -------------------------------------------------------------------------------------------- #


# a. [Expected Approach]        Using Iterative Method - O(n) Time and O(1) Space

# Iterative Python program to reverse a linked list

class Node:
    def __init__(self, newData):
        self.data = newData
        self.next = None

# Given the head of a list, reverse the list and return the head of reversed list

def reverseList(head):

    curr = head
    prev = None
 
    while curr is not None:    # Traverse all the nodes of Linked List

        nextNode = curr.next    # Store next
        curr.next = prev        # Reverse current node's next pointer
      
        prev = curr             # Move pointers one position ahead
        curr = nextNode

    return prev                 # Return the head of reversed linked list


if __name__ == "__main__":

    # Create a hard-coded linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = reverseList(head)

    printList(head) # Reversed Linked List: 5 4 3 2 1
  

  # -------------------------------------------------------------------------------------------- #


# b. [Alternate Approach - 1]   Using Recursion - O(n) Time and O(n) Space

# Recursive Python program to reverse a linked list

class Node:
    def __init__(self, newData):
        self.data = newData
        self.next = None

# Given the head of a list, reverse the list and return the head of reversed list

def reverseList(head):
  
    if head is None or head.next is None:
        return head
  
    rest = reverseList(head.next)    # reverse the rest of linked list and put the first element at the end
  
    head.next.next = head    # Make the current head as last node of remaining linked list
  
    head.next = None  # Update next of current head to NULL

    return rest       # Return the reversed linked list


if __name__ == "__main__":

    # Create a hard-coded linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = reverseList(head)
    printList(head)

  
    # -------------------------------------------------------------------------------------------- #
  
# c. [Alternate Approach - 2]   Using Stack - O(n) Time and O(n) Space

  # Python program to reverse linked list using Stack

class Node:
    def __init__(self, new_data):
      	
        self.data = new_data
        self.next = None

def reverseList(head):
  	
    stack = []  # Create a stack to store the nodes
  
    temp = head
  
    # Push all nodes except the last node into stack
  
    while temp.next is not None:
        stack.append(temp)
        temp = temp.next
  
    # Make the last node as new head of the linked list
  
    head = temp
  
    while stack:                         # Pop all the nodes and append to the linked list
      	
        temp.next = stack.pop()          # append the top value of stack in list
      
        temp = temp.next                 # move to the next node in the list
  
    temp.next = None                     # Update the next pointer of last node of stack to None
  
    return head




# Create a hard-coded linked list: 1 -> 2 -> 3 -> 4 -> 5

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)


head = reverseList(head)

printList(head)


# ___________________________________________________________________________________________________________________________#

# Reverse the Linked List

class LinkedList:
  
    def __init__(self):
        self.head = None
        self.length = 0  # initialize length
      
    def reverse(self):
      
        prev_node = None
        current_node = self.head
      
        while current_node:
          
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
          
        self.head = prev_node
        print("List reversed.")

    """ Prev_Node -> None     Current_Node -> 10 -> 20 -> 30 -> 40 -> None
        Prev_Node -> 10 -> None     Current_Node -> 20 -> 30 -> 40 -> None
        Prev_Node -> 20 -> 10 -> None     Current_Node -> 30 -> 40 -> None
        Prev_Node -> 30 -> 20 -> 10 -> None     Current_Node -> 40 -> None
        Prev_Node -> 40 -> 30 -> 20 -> 10 -> None     Current_Node -> None
        Head -> 40 -> 30 -> 20 -> 10 -> None
    """
  

# --------------- +  ==================================================== + --------------- #

# 8. Delete Entire List

class LinkedList:
  
    def __init__(self):
        self.head = None
        self.length = 0  # initialize length
    
    def delete_entire_list(self):
        self.head = None
        self.length = 0
        print("List has been cleared.")
