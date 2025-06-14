# Convert a Binary Tree to a Circular Doubly Link List

# Without classes

# A python program for in-place conversion of Binary Tree to DLL A binary tree node has data, left pointers and right pointers
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# head --> Pointer to head node of created doubly linked list
head = None

# Initialize previously visited node as NULL. This is so that the same value is accessible in all recursive calls
prev = None

# A simple recursive function to convert a given Binary tree to Doubly Linked List root --> Root of Binary Tree

def BinaryTree2DoubleLinkedList(root):

    # Base case
    if (root == None):
        return

    # Recursively convert left subtree
    BinaryTree2DoubleLinkedList(root.left)

    # Now convert this node
    global prev, head
  
    if (prev == None):
        head = root
    else:
        root.left = prev
        prev.right = root
    prev = root

    BinaryTree2DoubleLinkedList(root.right)                 # Finally convert right subtree



# Function to print nodes in a given doubly linked list


def printList(node):
    while (node != None):
        print(node.data)
        node = node.right


# Driver program to test above functions
# Let us create the tree as shown in above diagram

root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)

# convert to DLL
BinaryTree2DoubleLinkedList(root)

# Print the converted List
printList(head)


"""
Time Complexity: O(N), As every node is visited at most once.
Auxiliary space: O(log N), The extra space is used in the recursive function call stack which can grow upto a maximum size of logN.

"""



# Convert an Array to a Circular Doubly Linked List

# Node of the doubly linked list 
class Node: 
    
    def __init__(self, data): 
        self.data = data 
        self.prev = None
        self.next = None

# Utility function to create a node in memory
def getNode():
    return (Node(0))

# Function to display the list
def displayList(temp):

    t = temp
  
    if(temp == None):
        return 0
      
    else:
        
        print("The list is: ", end = " ")
        
        while(temp.next != t):
        
            print(temp.data, end = " ")
            temp = temp.next
        
        print(temp.data)
        
        return 1
    

def createList(arr, n, start):                                        # Function to convert array into list

    newNode = None                                                    # Declare newNode and temporary pointer
    temp = None
    i = 0
    
    while(i < n):                                                     # Iterate the loop until array length
    
        newNode = getNode()                                           # Create new node
        
        newNode.data = arr[i]                                         # Assign the array data
        
        # If it is first element Put that node prev and next as start as it is circular
      
        if(i == 0):
        
            start = newNode
            newNode.prev = start
            newNode.next = start
        
        else:
            
            temp = (start).prev                                # Find the last node
            
            temp.next = newNode                                # Add the last node to make them in circular fashion
            newNode.next = start
            newNode.prev = temp
            temp = start
            temp.prev = newNode
          
        i = i + 1
    return start

# Driver Code
if __name__ == "__main__": 

    arr = [1, 2, 3, 4, 5]                     # Array to be converted
    n = len(arr)
    
    start = None                              # Start Pointer
    
    start = createList(arr, n, start)         # Create the List
    
    displayList(start)                        # Display the list
    
"""
 
Time Complexity: O(n), as we are using a loop to traverse n times. Where n is the number of nodes in the linked list.

Auxiliary Space: O(1), as we are not using any extra space.


"""


#+_________________________________________________________________________________________________________________________+




# Node class for Binary Tree / Doubly Linked List
class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None   # For DLL: points to previous
        self.right = None  # For DLL: points to next


class BinaryTreeToCDLLConverter:
    def __init__(self):
        self.head = None          # Head of the resulting CDLL
        self.prev = None          # Previous visited node in in-order traversal

    def convert_to_cdll(self, root):
        """
        Recursively performs in-order traversal of the binary tree
        and links nodes to form a doubly linked list.
        """
        if root is None:
            return

        # Convert left subtree
        self.convert_to_cdll(root.left)

        # Link current node
        if self.prev is None:
            self.head = root
        else:
            root.left = self.prev
            self.prev.right = root

        self.prev = root  # Move prev pointer to current node

        # Convert right subtree
        self.convert_to_cdll(root.right)

    def make_circular(self):
        """
        Connects head and tail to make the doubly linked list circular.
        """
        if not self.head or not self.prev:
            return
        self.head.left = self.prev
        self.prev.right = self.head

    def display_cdll(self):
        """
        Prints the circular doubly linked list starting from head.
        """
        if not self.head:
            print("CDLL is empty")
            return

        print("Circular Doubly Linked List from Binary Tree:")
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.right
            if current == self.head:
                break
        print("(head)")

# ---------- 🔍 Example Usage ----------

if __name__ == "__main__":
  
    # Constructing the binary tree:
    #         10
    #       /    \
    #     12      15
    #    /  \     /
    #  25   30   36

    root = TreeNode(10)
    root.left = TreeNode(12)
    root.right = TreeNode(15)
    root.left.left = TreeNode(25)
    root.left.right = TreeNode(30)
    root.right.left = TreeNode(36)

    converter = BinaryTreeToCDLLConverter()
    converter.convert_to_cdll(root)
  
    converter.make_circular()
    converter.display_cdll()

"""
Time Complexity: O(N)

- Each node is visited exactly once during the in-order traversal.

Space Complexity: O(H)

- Where H is the height of the binary tree.
- Space used is due to the recursion stack (in-place conversion).
- H = log N for balanced, H = N for skewed trees.
"""




#+_______________________________________________________________________________________________________________________________+

# Node class for CDLL
class CDLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Class to convert array to CDLL
class ArrayToCircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Inserts a new node at the end of the CDLL."""
        new_node = CDLLNode(data)

        if not self.head:
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def convert_array_to_cdll(self, arr):
        """Converts an array to a circular doubly linked list."""
        for value in arr:
            self.insert_at_end(value)

    def display_cdll(self):
        """Displays the circular doubly linked list."""
        if not self.head:
            print("CDLL is empty")
            return

        print("Circular Doubly Linked List from Array:")
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

# ---------- 🔍 Example Usage ----------
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]

    converter = ArrayToCircularDoublyLinkedList()
    converter.convert_array_to_cdll(arr)
    converter.display_cdll()
