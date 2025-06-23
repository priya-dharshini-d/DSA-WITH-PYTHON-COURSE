


"""

insert() – Insert into BST

min_value() – Find minimum value

max_value() – Find maximum value

inorder_successor() – Find inorder successor

is_bst() – Check if tree is a valid BST

"""


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# -------------------------
# Insert into BST
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# -------------------------
# Find minimum value node
def min_value(root):
    """Returns the minimum value in a BST."""
    if root is None:
        return None
    while root.left:
        root = root.left
    return root.data
# -------------------------
# Find maximum value node
def max_value(root):
    """Returns the maximum value in a BST."""
    if root is None:
        return None
    while root.right:
        root = root.right
    return root.data

# -------------------------
# Find minimum node (for successor use)
def get_min_node(node):
    """Return the node with the minimum value in a subtree."""
    while node.left:
        node = node.left
    return node

def inorder_successor(root, key):
    """
    Return the inorder successor of a given key in a BST.
    If the key is not found or has no successor, return None.
    """
    successor = None
    current = root

    while current:
        if key < current.data:
            successor = current        # Potential successor
            current = current.left     # Try to find smaller candidate
        elif key > current.data:
            current = current.right
        else:
            # Node with the key is found
            if current.right:
                successor = get_min_node(current.right)
            break

    return successor.data if successor else None


# -------------------------
# Check if binary tree is BST

def is_bst_util(node, min_val, max_val):
    if node is None:
        return True
    if not (min_val < node.data < max_val):
        return False
    return (is_bst_util(node.left, min_val, node.data) and is_bst_util(node.right, node.data, max_val))

def is_bst(root):
    return is_bst_util(root, float('-inf'), float('inf'))

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def is_bst_inorder(root):
    prev = [None]  # Using list to keep reference in recursion

    def inorder(node):
        if not node:
            return True
        if not inorder(node.left):
            return False
        if prev[0] is not None and node.data <= prev[0]:
            return False
        prev[0] = node.data
        return inorder(node.right)

    return inorder(root)



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def is_bst_using_inorder_list(root):
    def inorder(node, result):
        if node is None:
            return
        inorder(node.left, result)
        result.append(node.data)
        inorder(node.right, result)

    values = []
    inorder(root, values)
    
    # Check if list is strictly increasing
    return values == sorted(values) and len(values) == len(set(values))

# So while it's valid and intuitive, it's less efficient than the min-max or recursive inorder methods (O(n) vs O(n log n)).


#+___________________________________________________________________________________________________________________+

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.data:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        return node

    def min_value(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current.data if current else None

    def max_value(self, node):
        current = node
        while current and current.right:
            current = current.right
        return current.data if current else None

    def inorder_successor(self, root, key):
        successor = None
        current = root

        while current:
            if key < current.data:
                successor = current
                current = current.left
            elif key > current.data:
                current = current.right
            else:  # Node found
                if current.right:
                    successor = self.get_min_node(current.right)
                break
        return successor.data if successor else None

    def get_min_node(self, node):
        while node and node.left:
            node = node.left
        return node

    def is_bst_util(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.data < max_val):
            return False
        return (self.is_bst_util(node.left, min_val, node.data) and
                self.is_bst_util(node.right, node.data, max_val))

    def is_bst(self):
        return self.is_bst_util(self.root, float('-inf'), float('inf'))
