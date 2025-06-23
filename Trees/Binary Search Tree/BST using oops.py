class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        self._insert_recursive(self.root, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def _insert_recursive(self, node, key):
        if key < node.data:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.data:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)
              
        # if key == node.data: do nothing (ignore duplicates)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=' ')
        self.inorder(node.right)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)
      
    def delete(self, key):
        self.root = self._delete(self.root, key)
      
    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Node with 0 or 1 child
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # Node with 2 children: get inorder successor
            succ = self._get_successor(root)
            root.key = succ.key
            root.right = self._delete(root.right, succ.key)

        return root

    def _get_successor(self, node):
        curr = node.right
        while curr and curr.left:
            curr = curr.left
        return curr

  """
  https://youtu.be/gcULXE7ViZw?si=R4CuVAnMwl7huAsM
  
 Case - 1  Deleting a leaf Node is easy

  What if we want to delete non-leaf node - Case - 2: When we have one child - We can link its parent to its only child ( node being deleted will be detached ).
                                          - Case - 3: When we have two child - minimum in right sub tree ( it will not have any left child since it is minimum ).

                                CASE - 3
                                          1. FIND min in right-subtree
                                          2. COPY the value in targetted node
                                          3. DELETE duplicate from right-subtree
                                          
                                          We can also find max in left sub tree and do the steps 2 and 3 ( it will not have any right child since it is maximum )

🔹 Inorder Predecessor:

The largest value node in the left subtree of the node to be deleted.

It is the node that comes just before the given node in inorder traversal.

📌 To find it:

# Go one step left, then all the way right
pred = node.left
while pred.right:
    pred = pred.right


🔹 Inorder Successor:

The smallest value node in the right subtree of the node to be deleted.

It is the node that comes just after the given node in inorder traversal.

📌 To find it:

# Go one step right, then all the way left
succ = node.right
while succ.left:
    succ = succ.left
    
"""

#+_______________________________________________________________________________________________________________________________+

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return

        curr = self.root
        parent = None

        while curr:
            parent = curr
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return  # Duplicate key; do not insert

        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def search(self, x):
        curr = self.root
        while curr:
            if curr.key == x:
                return True
            elif x < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def delete(self, key):
        curr = self.root
        parent = None

        # Find the node and its parent
        while curr and curr.key != key:
            parent = curr
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None:
            return  # Key not found

        # Case 1 & 2: Node has 0 or 1 child
        if curr.left is None or curr.right is None:
            new_curr = curr.left if curr.left else curr.right

            if parent is None:
                self.root = new_curr
            elif parent.left == curr:
                parent.left = new_curr
            else:
                parent.right = new_curr

        # Case 3: Node has 2 children
        else:
            succ_parent = curr
            succ = curr.right
            while succ.left:
                succ_parent = succ
                succ = succ.left

            curr.key = succ.key  # Replace value

            if succ_parent != curr:
                succ_parent.left = succ.right
            else:
                curr.right = succ.right
#+_______________________________________________________________________________________________________________________________+

# Recursive Implementation

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)
        
    # If key == root.val, do nothing (no duplicates in BST)

    return root


# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def search(root, key):
  
    # Base Cases: root is null or key is present at root
    if root is None or root.key == key:
        return root
    
    # Key is greater than root's key
    if root.key < key:
        return search(root.right, key)
    
    # Key is smaller than root's key
    return search(root.left, key)

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

#+_______________________________________________________________________________________________________________________________+

# Iterative implementation

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

#+_______________________________________________________________________________________________________________________________+
