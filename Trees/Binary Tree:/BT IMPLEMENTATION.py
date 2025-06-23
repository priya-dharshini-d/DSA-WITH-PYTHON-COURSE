class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# In-order DFS: Left, Root, Right
def in_order_dfs(node):
    if node is None:
        return
    in_order_dfs(node.left)
    print(node.data, end=' ')
    in_order_dfs(node.right)

# Pre-order DFS: Root, Left, Right
def pre_order_dfs(node):
    if node is None:
        return
    print(node.data, end=' ')
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)

# Post-order DFS: Left, Right, Root
def post_order_dfs(node):
    if node is None:
        return
    post_order_dfs(node.left)
    post_order_dfs(node.right)
    print(node.data, end=' ')

# BFS: Level order traversal
def bfs(root):
    if root is None:
        return
    queue = [root]                      # Start with the root in the queue
    while queue:                        # Repeat until queue is empty
        node = queue.pop(0)             # Remove the front node
        print(node.data, end=' ')       # Print its value
        if node.left:                   # If left child exists, add to queue
            queue.append(node.left)
        if node.right:                  # If right child exists, add to queue
            queue.append(node.right)


if __name__ == "__main__":
    # Creating the tree
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    print("In-order DFS: ", end='')
    in_order_dfs(root)
    print("\nPre-order DFS: ", end='')
    pre_order_dfs(root)
    print("\nPost-order DFS: ", end='')
    post_order_dfs(root)
    print("\nLevel order: ", end='')
    bfs(root)

#+______________________________________________________________________________________________________________________________+

# This function builds a Binary Tree from a list of values assuming the tree is stored in level-order (like a binary heap).

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def build_Tree(values):
    nodes = [Node(val) for val in values]
  
    for i in range(len(nodes)):
      
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
    return nodes[0]  # root of the tree


#+______________________________________________________________________________________________________________________________+

# Constructing BT if preorder is given (null pointers are also given)
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def build_from_preorder(self, preorder):
  
        if self.index >= len(preorder) or preorder[self.index] is None:
            self.index += 1
            return None

        node = TreeNode(preorder[self.index])
        self.index += 1
        node.left = self.build_from_preorder(preorder)
        node.right = self.build_from_preorder(preorder)
        return node

    def create(self, preorder):
        self.index = 0
        self.root = self.build_from_preorder(preorder)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=' ')
            self.inorder_traversal(node.right)

# 🔸 Example usage:
preorder = [1, 2, 4, None, None, 5, None, None, 3, None, 6]  # preorder with None as null
tree = BinaryTree()
tree.create(preorder)

tree.inorder_traversal(tree.root)

#+______________________________________________________________________________________________________________________________+

"""
✅ 1. Binary Tree from Inorder + Preorder

📌 Logic:
Preorder: [Root, Left, Right]
Inorder: [Left, Root, Right]

"""

class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class TreeBuilder:
    def build_tree_from_in_pre(self, inorder, preorder):

        self.pre_index = 0                                             # Index to keep track of current node in preorder list

        in_map = {val: idx for idx, val in enumerate(inorder)}         # Map value to its index in inorder for fast lookup

        def build(start, end):
            if start > end:
                return None                                            # No subtree in this range

            root_val = preorder[self.pre_index]                        # Get the current root value from preorder
            self.pre_index += 1

            root = TreeNode(root_val)                                  # Create the root node

            in_index = in_map[root_val]                                # Find this root in the inorder sequence

            root.left = build(start, in_index - 1)                     # Recursively build left and right subtrees
            root.right = build(in_index + 1, end)

            return root

        return build(0, len(inorder) - 1)                              # Start building from the full inorder range
      
inorder =  [4, 2, 5, 1, 6, 3]
preorder = [1, 2, 4, 5, 3, 6]
builder = TreeBuilder()
tree_root = builder.build_tree_from_in_pre(inorder, preorder)

#+______________________________________________________________________________________________________________________________+

"""
✅ 2. Binary Tree from Inorder + Postorder
📌 Logic:
Postorder: [Left, Right, Root]

Inorder: [Left, Root, Right]

"""

class TreeBuilder:
    def build_tree_from_in_post(self, inorder, postorder):
        self.post_index = len(postorder) - 1
      
        in_map = {val: idx for idx, val in enumerate(inorder)}

        def build(start, end):
            if start > end:
                return None
              
            root_val = postorder[self.post_index]
            self.post_index -= 1
          
            root = TreeNode(root_val)
            in_index = in_map[root_val]
          
            # Build right subtree before left (postorder goes backward)
            root.right = build(in_index + 1, end)
            root.left = build(start, in_index - 1)
          
            return root

        return build(0, len(inorder) - 1)
        
#+__________________________________________________________________________________________________+

#To find max element in BT

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def find_max(self, node):
        """Returns the maximum value in the binary tree rooted at `node`."""
        if node is None:
            return float('-inf')  # return minimum possible value if node is null

        left_max = self.find_max(node.left)
        right_max = self.find_max(node.right)

        return max(node.data, left_max, right_max)

# 🔹 Example usage
if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = TreeNode(10)
    bt.root.left = TreeNode(20)
    bt.root.right = TreeNode(5)
    bt.root.left.left = TreeNode(40)
    bt.root.left.right = TreeNode(15)

    max_value = bt.find_max(bt.root)
    print("Maximum element in the binary tree:", max_value)

"""
| Complexity        | Value                         |
| ----------------- | ----------------------------- |
| Time              | **O(n)**                      |
| Space (recursion) | **O(h)** (h = height of tree) |

| Tree Type     | Height (h) | Space Complexity |
| ------------- | ---------- | ---------------- |
| Skewed Tree   | h = n      | O(n)             |
| Balanced Tree | h = log n  | O(log n)         |
| General Tree  | h          | O(h)             |

"""


#+___________________________________________________________________________________+

"""
 Delete a Node from a Binary Tree (Not BST)

 
🧠 Concept:

In a normal binary tree (not BST), to delete a node with a given value:

    Find the node to be deleted.

    Find the deepest and rightmost node in the tree.

    Replace the target node's value with that deepest node’s value.

    Delete the deepest node.

    This ensures the structure of the binary tree remains intact.

🧾 Algorithm Steps

    Do a level order traversal to find:

           - The node to delete (target).

           - The deepest node.

           - The parent of the deepest node.

    Replace target.data = deepest.data.

    Remove the deepest node by setting its parent's left or right to None.

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def delete_node(root, key):
    
    if root is None:
        return None

    if root.left is None and root.right is None:
        if root.data == key:
            return None
        else:
            return root

    # Level order traversal
    queue = [root]
    target = None
    last = None
    parent_of_last = None

    while queue:
        last = queue.pop(0)
        if last.data == key:
            target = last

        if last.left:
            parent_of_last = last
            queue.append(last.left)
        if last.right:
            parent_of_last = last
            queue.append(last.right)

    if target:
        # Replace target data with deepest node data
        target.data = last.data

        # Delete deepest node
        if parent_of_last.right == last:
            parent_of_last.right = None
        elif parent_of_last.left == last:
            parent_of_last.left = None

    return root
    

#+___________________________________________________________________________________+

"""
🌳 Binary Tree Representation Using Array (List)

The list tree = [None] * 10 represents a binary tree with 10 possible positions (indices 0–9).

In this layout:

Index i is a node

Its left child is at 2*i + 1

Its right child is at 2*i + 2

This structure is commonly used for heap implementations.

"""

# Python3 implementation of tree using array
# numbering starting from 0 to n-1.
tree = [None] * 10


def root(key):
    if tree[0] != None:
        print("Tree already had root")
    else:
        tree[0] = key


def set_left(key, parent):
    if tree[parent] == None:
        print("Can't set child at", (parent * 2) + 1, ", no parent found")
    else:
        tree[(parent * 2) + 1] = key


def set_right(key, parent):
    if tree[parent] == None:
        print("Can't set child at", (parent * 2) + 2, ", no parent found")
    else:
        tree[(parent * 2) + 2] = key


def print_tree():
    for i in range(10):
        if tree[i] != None:
            print(tree[i], end="")
        else:
            print("-", end="")
    print()


# Driver Code
root('A')
set_left('B', 0)
set_right('C', 0)
set_left('D', 1)
set_right('E', 1)
set_right('F', 2)
print_tree()


#+___________________________________________________________________________________+
# Check whether a given binary tree is perfect or not

"""

Given a Binary Tree, the task is to check whether the given Binary Tree is a perfect Binary Tree or not.

Note:

A Binary tree is a Perfect Binary Tree in which all internal nodes have two children and all leaves are at the same level.

A Perfect Binary Tree of height h has 2h – 1 nodes.


# [Expected Approach - 1] Using Recursive Method - O(n) Time and O(h) Space

The idea is to find the depth of the tree (lets say d) 
and then check that all the internal nodes have two child nodes and all leaf nodes are at depth d. 

If not, then return false.

"""


# Recursive function

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def depth(root):        # Function to find depth of tree.
    if root is None:
        return 0
    return 1 + max(depth(root.left), depth(root.right))

def isPerfectRecur(root, d):
    
    if root is None:         # Empty tree is also perfect 
        return True
    
    # If node is leaf, check if it is at depth d.
    if root.left is None and root.right is None:
        return d == 1
    
    # If internal node does not have left or right node, return false.
    if root.left is None or root.right is None:
        return False
    
    # Check left and right subtree
    return isPerfectRecur(root.left, d-1) and isPerfectRecur(root.right, d-1)

def isPerfect(root):
    
    # Find depth of tree 
    d = depth(root)
    
    return isPerfectRecur(root, d)

if __name__ == "__main__":
    
    # Binary tree 
    #           10
    #        /     \  
    #      20       30  
    #     /  \     /  \
    #   40    50  60   70
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)

    if isPerfect(root):
        print("True")
    else:
        print("False")



#+______________________________________________________________________________________________________________________________+

"""
[Expected Approach - 2] Using level order traversal - O(n) Time and O(n) Space

The idea is to perform a level-order traversal of the binary tree using a queue. 

By traversing the tree level by level, we can check if the tree satisfies the conditions of a perfect binary tree.
"""


from collections import deque

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def isPerfect(root):
    
    if root is None:
        return True
    
    q = deque([root])
    
    # to store the expected node count at a given level.
    nodeCnt = 1
    
    while q:
        size = len(q)
        
        # If number of expected nodes is not same, return False.
        if size != nodeCnt:
            return False
        
        while size > 0:
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            size -= 1
        
        # Next level will contain twice number of nodes.
        nodeCnt *= 2
    
    return True

if __name__ == "__main__":
    
    # Binary tree 
    #           10
    #        /     \  
    #      20       30  
    #     /  \     /  \
    #   40    50  60   70
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)

    if isPerfect(root):
        print("True")
    else:
        print("False")


#+___________________________________________________________________________________+
