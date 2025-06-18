# Insertion in an AVL Tree

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# A utility function to get the height of the tree
def height(node):
    if not node:
        return 0
    return node.height

# A utility function to right rotate subtree rooted with y
def right_rotate(y):
    x = y.left
    T2 = x.right

    # Perform rotation
    x.right = y
    y.left = T2

    # Update heights
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    # Return new root
    return x

# A utility function to left rotate subtree rooted with x
def left_rotate(x):
    y = x.right
    T2 = y.left

    # Perform rotation
    y.left = x
    x.right = T2

    # Update heights
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    # Return new root
    return y

# Get balance factor of node N
def get_balance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

# Recursive function to insert a key in the subtree rooted with node
def insert(node, key):
  
    # Perform the normal BST insertion
    if not node:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node   # Equal keys are not allowed in BST

    # Update height of this ancestor node
    node.height = 1 + max(height(node.left), height(node.right))

    # Get the balance factor of this ancestor node
    balance = get_balance(node)

    # If this node becomes unbalanced, then there are 4 cases

    # Left Left Case
    if balance > 1 and key < node.left.key:
        return right_rotate(node)

    # Right Right Case
    if balance < -1 and key > node.right.key:
        return left_rotate(node)

    # Left Right Case
    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # Right Left Case
    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    # Return the (unchanged) node pointer
    return node


def pre_order(root):
    if root:
        print(root.key, end=" ")
        pre_order(root.left)
        pre_order(root.right)

root = None

# Constructing tree given in the above figure
root = insert(root, 10)
root = insert(root, 20)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 25)

# The constructed AVL Tree would be
#        30
#       /  \
#      20   40
#     /  \    \
#    10  25   50

print("Preorder traversal :")
pre_order(root)

"""
Time Complexity: O(log(n)), For Insertion
Auxiliary Space: O(Log n) for recursion call stack as we have written a recursive method to insert.
"""

#+___________________________________________________________________________________________________________________+


# Deletion in an AVL Tree

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(N):
    if N is None:
        return 0
    return N.height

def right_rotate(y):
    x = y.left
    T2 = x.right

    # Perform rotation
    x.right = y
    y.left = T2

    # Update heights
    y.height = max(height(y.left), 
                   height(y.right)) + 1
    x.height = max(height(x.left), 
                   height(x.right)) + 1

    # Return new root
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    # Perform rotation
    y.left = x
    x.right = T2

    # Update heights
    x.height = max(height(x.left), 
                   height(x.right)) + 1
    y.height = max(height(y.left), 
                   height(y.right)) + 1

    # Return new root
    return y

def get_balance(N):
    if N is None:
        return 0
    return height(N.left) - height(N.right)

def insert(node, key):
  
    # 1. Perform the normal BST insertion
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:  # Duplicate keys not allowed
        return node

    # 2. Update height of this ancestor node
    node.height = max(height(node.left), height(node.right)) + 1

    # 3. Get the balance factor of this node to check whether this node became unbalanced
    balance = get_balance(node)

    # If this node becomes unbalanced, then there are 4 cases

    # Left Left Case
    if balance > 1 and key < node.left.key:
        return right_rotate(node)

    # Right Right Case
    if balance < -1 and key > node.right.key:
        return left_rotate(node)

    # Left Right Case
    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # Right Left Case
    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

def min_value_node(node):
    current = node

    # loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current

def delete_node(root, key):
    # STEP 1: PERFORM STANDARD BST DELETE
    if root is None:
        return root

    # If the key to be deleted is smaller than the root's key, then it lies in left subtree
    if key < root.key:
        root.left = delete_node(root.left, key)

    # If the key to be deleted is greater than the root's key, then it lies in right subtree
    elif key > root.key:
        root.right = delete_node(root.right, key)

    # if key is same as root's key, then this is the node to be deleted
    else:
        # node with only one child or no child
        if root.left is None or root.right is None:
            temp = root.left if root.left else root.right

            # No child case
            if temp is None:
                root = None
            else:  # One child case
                root = temp

        else:
            # node with two children: Get the inorder successor (smallest in the right subtree)
            temp = min_value_node(root.right)

            # Copy the inorder successor's data to this node
            root.key = temp.key

            # Delete the inorder successor
            root.right = delete_node(root.right, temp.key)

    # If the tree had only one node then return
    if root is None:
        return root

    # STEP 2: UPDATE HEIGHT OF THE CURRENT NODE
    root.height = max(height(root.left), height(root.right)) + 1

    # STEP 3: GET THE BALANCE FACTOR OF THIS 
    # NODE (to check whether this node became unbalanced)
    balance = get_balance(root)

    # If this node becomes unbalanced, then there are 4 cases

    # Left Left Case
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)

    # Left Right Case
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right Right Case
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)

    # Right Left Case
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def pre_order(root):
    if root is not None:
        print("{0} ".format(root.key), end="")
        pre_order(root.left)
        pre_order(root.right)

# Driver Code
if __name__ == "__main__":
    root = None

    root = insert(root, 9)
    root = insert(root, 5)
    root = insert(root, 10)
    root = insert(root, 0)
    root = insert(root, 6)
    root = insert(root, 11)
    root = insert(root, -1)
    root = insert(root, 1)
    root = insert(root, 2)

    print("Preorder traversal of the constructed AVL tree is")
    pre_order(root)

    root = delete_node(root, 10)

    print("\nPreorder traversal after deletion of 10")
    pre_order(root)

"""
Time Complexity: The rotation operations (left and right rotate) take constant time as only few pointers are being changed there. 

Updating the height and getting the balance factor also take constant time. 

So the time complexity of AVL delete remains same as BST delete which is O(h) where h is height of the tree. 

Since AVL tree is balanced, the height is O(log n). So time complexity of AVL delete is O(log n).

Auxiliary Space: O(log n) for recursion call stack as we have written a recursive method to delete
"""

#+___________________________________________________________________________________________________________________+

