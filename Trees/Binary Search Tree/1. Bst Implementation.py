# Insertion in Binary Search Tree using Recursion:

# Python program to demonstrate insert operation in binary search tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:         #🔸 Duplicate key — BSTs usually don't allow duplicates.🔸 So we return the current node unchanged, without inserting anything.
        return root
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root


# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


# Creating the following BST
#      50
#     /  \
#    30   70
#   / \   / \
#  20 40 60 80
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

inorder(r)              # Print inorder traversal of the BST


"""
Time Complexity: 

The worst-case time complexity of insert operations is O(h) where h is the height of the Binary Search Tree. 

In the worst case, we may have to travel from the root to the deepest leaf node. 

The height of a skewed tree may become n and the time complexity of insertion operation may become O(n).

Auxiliary Space: The auxiliary space complexity of insertion into a binary search tree is O(h), due to recursive stack.
"""

#+________________________________________________________________________________________________________________________+

# Insertion in Binary Search Tree using Iterative approach:

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def insert(root, key):
    temp = Node(key)

    # If tree is empty
    if root is None:
        return temp

    # Find the node who is going to have the new node temp as its child
    parent = None
    curr = root
    while curr is not None:
        parent = curr
        if curr.key > key:
            curr = curr.left
        elif curr.key < key:
            curr = curr.right
        else:
            return root                           # Key already exists

    # If key is smaller, make it left child, else right child
  
    if parent.key > key:
        parent.left = temp
    else:
        parent.right = temp

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Creating the following BST
#      50
#     /  \
#    30   70
#   / \   / \
#  20 40 60 80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

inorder(r)


""" 
The time complexity of inorder traversal is O(h), where h is the height of the tree.
The Auxiliary space is O(1)
"""

#+________________________________________________________________________________________________________________________+

# Recursive Program to implement search in BST:

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def search(root, key):
  
    # Base Cases: root is null or key is present at root
    if root is None or root.key == key:
        return root
    
    # Key is greater than root's key
    if root.key < key:
        return search(root.right, key)
    
    # Key is smaller than root's key
    return search(root.left, key)


 # Creating a hard coded tree for keeping the length of the code small. 
 # We need to make sure that BST properties are maintained if we try some other cases.

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

# Searching for keys in the BST
print("Found" if search(root, 19) else "Not Found")
print("Found" if search(root, 80) else "Not Found")

""" 
Time complexity: O(h), where h is the height of the BST.
Auxiliary Space: O(h) This is because of the space needed to store the recursion stack.
"""

#+________________________________________________________________________________________________________________________+

# Iterative searching in Binary Search Tree

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def search(root, x):
    
    curr = root
    
    while curr is not None:
        
        if curr.data == x:                   # If curr node is x
            return True
            
        elif curr.data < x:                  # Search in right subtree
            curr = curr.right
            
        else:                                # Search in left subtree
            curr = curr.left
    
    return False                             # If x is not found.


if __name__ == "__main__":
    
    # Create a hard coded BST.
    #        20
    #       /  \
    #      8   22
    #     / \
    #   4   12
    #       /  \
    #     10   14
  
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    
    x = 12
    print(search(root, x))


""" 
Time Complexity: O(h), where h is the height of the BST.
Auxiliary Space: O(1)
"""

#+________________________________________________________________________________________________________________________+

#Recursive Implementation of Deletion operation in a BST

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Note that it is not a generic inorder successor function. 
# It mainly works when the right child is not empty, which is  the case we need in BST delete.

def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

# This function deletes a given key x from the given BST and returns the modified root of the BST (if it is modified).

def del_node(root, x):
  
    # Base case
    if root is None:
        return root

    # If key to be searched is in a subtree
    if root.key > x:
        root.left = del_node(root.left, x)
    elif root.key < x:
        root.right = del_node(root.right, x)
        
    else:
        # If root matches with the given key

        # Cases when root has 0 children or only right child
        if root.left is None:
            return root.right

        # When root has only left child
        if root.right is None:
            return root.left

        # When both children are present
        succ = get_successor(root)
        root.key = succ.key
        root.right = del_node(root.right, succ.key)
        
    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.right = Node(18)
    x = 15

    root = del_node(root, x)
    inorder(root)
    print()

""" 
Time Complexity: O(h), where h is the height of the BST. 
Auxiliary Space: O(h).

The above recursive solution does two traversals across height when both the children are not NULL.

We can avoid extra O(h) space and recursion call overhead with iterative solution. 

The iterative solution has same time complexity but works more efficiently.
"""

#+________________________________________________________________________________________________________________________+

# Iterative approach to delete 'key' from the BST.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def del_iterative(root, key):
    curr = root
    prev = None

    # First check if the key is actually present in the BST.
    # the variable prev points to the parent of the key to be deleted

    while (curr != None and curr.key != key):
        prev = curr
        if curr.key < key:
            curr = curr.right
        else:
            curr = curr.left

    if curr == None:
        return root

    if curr.left == None or curr.right == None:     # Check if the node to be deleted has atmost one child

        newCurr = None               # newCurr will replace the node to be deleted.

        if curr.left == None:        # if the left child does not exist.
            newCurr = curr.right
        else:
            newCurr = curr.left


        if prev == None:             # check if the node to be deleted is the root.
            return newCurr

        # Check if the node to be deleted is prev's left or right child and then replace this with newCurr
      
        if curr == prev.left:
            prev.left = newCurr
        else:
            prev.right = newCurr

        curr = None

    else:                      # node to be deleted has two children.
        p = None
        temp = None

        # Compute the inorder successor of curr.
        temp = curr.right
        while(temp.left != None):
            p = temp
            temp = temp.left

        # check if the parent of the inorder successor is the root or not.
        # if it isn't, then make the left child of its parent equal to the
        # inorder successor's right child.

        if p != None:
            p.left = temp.right

        else:

            # if the inorder successor was the root, then make the right child
            # of the node to be deleted equal to the right child of the inorder successor.
          
            curr.right = temp.right

        curr.data = temp.key

    return root



def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.right = Node(18)
    x = 15

    root = del_iterative(root, x)
    inorder(root)

""" 
Time Complexity : O(h) where h is height of the BST
Auxiliary Space: O(1)

"""

#+________________________________________________________________________________________________________________________+

# Binary Search Tree (BST) Traversals – Inorder, Preorder, Post Order

# Preorder Traversal
class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v

def printInorder(root):
    if root:
        printInorder(root.left)                      # Traverse left subtree
        print(root.data,end=" ")                     # Visit node
        printInorder(root.right)                     # Traverse right subtree


if __name__ == "__main__":

    root = Node(100)
    root.left = Node(20)
    root.right = Node(200)
    root.left.left = Node(10)
    root.left.right = Node(30)
    root.right.left = Node(150)
    root.right.right = Node(300)

    print("Inorder Traversal:",end=" ")
    printInorder(root)

""" 
Time complexity: O(N), Where N is the number of nodes.
Auxiliary Space: O(h), Where h is the height of tree.
"""

#+________________________________________________________________________________________________________________________+

# Preorder Traversal

class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

def printPreOrder(node):
    if node is None:
        return
    print(node.data, end = " ")            # Visit Node

    printPreOrder(node.left)               # Traverse left subtree

    printPreOrder(node.right)              # Traverse right subtree


if __name__ == "__main__":

    root = Node(100)
    root.left = Node(20)
    root.right = Node(200)
    root.left.left = Node(10)
    root.left.right = Node(30)
    root.right.left = Node(150)
    root.right.right = Node(300)

    print("Preorder Traversal: ", end = "")
    printPreOrder(root)

""" 
Time complexity: O(N), Where N is the number of nodes.
Auxiliary Space: O(H), Where H is the height of the tree
"""

#+________________________________________________________________________________________________________________________+

# Post order Traversal
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

def printPostOrder(node):
    if node is None:
        return

    printPostOrder(node.left)                # Traverse left subtree

    printPostOrder(node.right)               # Traverse right subtree
    
    print(node.data, end = " ")              # Visit Node

if __name__ == "__main__":
    root = Node(100)
    root.left = Node(20)
    root.right = Node(200)
    root.left.left = Node(10)
    root.left.right = Node(30)
    root.right.left = Node(150)
    root.right.right = Node(300)

    print("Postorder Traversal: ", end = "")
    printPostOrder(root)
  
""" 
Time complexity: O(N), Where N is the number of nodes.
Auxiliary Space: O(H), Where H is the height of the tree
"""

#+________________________________________________________________________________________________________________________+

# Balance a Binary Search Tree
# Python program to convert a left unbalanced BST to a balanced BST

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Inorder traversal to store elements of the tree in sorted order
def storeInorder(root, nodes):
    if root is None:
        return

    storeInorder(root.left, nodes)            # Traverse the left subtree

    nodes.append(root.data)                   # Store the node data

    storeInorder(root.right, nodes)           # Traverse the right subtree

# Function to build a balanced BST from a sorted array

def buildBalancedTree(nodes, start, end):
    if start > end:                                      # Base case
        return None

    # Get the middle element and make it the root
    mid = (start + end) // 2
    root = Node(nodes[mid])

    # Recursively build the left and right subtrees
    root.left = buildBalancedTree(nodes, start, mid - 1)
    root.right = buildBalancedTree(nodes, mid + 1, end)

    return root

# Function to balance a BST
def balanceBST(root):
    nodes = []

    storeInorder(root, nodes)                                 # Store the nodes in sorted order

    return buildBalancedTree(nodes, 0, len(nodes) - 1)        # Build the balanced tree from the sorted nodes


# Print tree as level order

from collections import deque

def printLevelOrder(root):
    if root is None:
        print("N", end=" ")
        return

    queue = deque([root])
    nonNull = 1

    while queue and nonNull > 0:
        curr = queue.popleft()

        if curr is None:
            print("N", end=" ")
            continue
        nonNull -= 1

        print(curr.data, end=" ")
        queue.append(curr.left)
        queue.append(curr.right)
      
        if curr.left:
            nonNull += 1
        if curr.right:
            nonNull += 1

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.left.left = Node(1)
    root.right = Node(5)
    root.right.right = Node(6)
    root.right.right.right = Node(7)

    balancedRoot = balanceBST(root)
    printLevelOrder(balancedRoot)

  
""" 
Time Complexity: O(n), as we are just traversing the tree twice.

Once in inorder traversal and then in construction of the balanced tree.

Auxiliary space: O(n), as extra space is used to store the nodes of the inorder traversal in the vector.

Also the extra space taken by recursion call stack is O(h) where h is the height of the tree.
"""

#+________________________________________________________________________________________________________________________+


