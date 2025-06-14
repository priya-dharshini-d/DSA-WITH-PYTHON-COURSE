# 2: Find Maximum Element in Binary Tree (Without Recursion)

"""
🔹 Approach:
Use level order traversal (BFS) and keep track of the maximum value while visiting each node.

"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_max_level_order(root):
    if root is None:
        return float('-inf')  # no node present, return negative infinity

    queue = []  # simple list to act as queue
    queue.append(root)
    maxElement = root.data

    while queue:
        node = queue.pop(0)  # dequeue from front (FIFO)
        maxElement = max(maxElement, node.data)

        if node.left:
            queue.append(node.left)   # enqueue left child
        if node.right:
            queue.append(node.right)  # enqueue right child

    return maxElement

# 🔸 Example usage
if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(20)
    root.right = TreeNode(5)
    root.left.left = TreeNode(40)
    root.left.right = TreeNode(15)

    print("Maximum element in the binary tree (level-order):", find_max_level_order(root))


# or

from collections import deque

def find_max_level_order(root):
    if root is None:
        return float('-inf')

    q = deque()
    q.append(root)
    maxElement = root.data

    while q:
        node = q.popleft()
        maxElement = max(maxElement, node.data)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return maxElement

+_____________________________________________________________________________________________+

"""

✅ Problem 3: Search Element in Binary Tree (Recursive)

🔹 Approach:

Recursively check:

If current node is the value

If not, search left subtree

If not found, search right subtree

This function searches for a specific value (target) in a binary tree, using recursive depth-first traversal.

"""

def find_recursive(root, target):
    if root is None:
        return False
    if root.data == target:
        return True
    return find_recursive(root.left, target) or find_recursive(root.right, target)

#+_____________________________________________________________________________________________+

"""

Problem 4: Search Element in Binary Tree (Without Recursion)

🔹 Approach:
Use BFS and check if any node matches the target value during traversal.

"""
from collections import deque

def find_using_level_order(root, target):
    if root is None:
        return False

    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        if node.data == target:
            return True
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return False

#+_____________________________________________________________________________________________+

"""
✅ Problem-5: Insert an Element into a Binary Tree

🔹 Concept:
Since this is a general binary tree (not BST), we insert the new element at the first available position in level order.

That is, we traverse the tree level by level and insert the node as the left or right child where a spot is free.

"""

from collections import deque

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_in_binary_tree(root, data):
    new_node = BinaryTree(data)
    
    if root is None:
        return new_node                          # new node becomes the root

    q = deque()
    q.append(root)

    while q:
        node = q.popleft()

        if node.left is None:
            node.left = new_node
            return root
        else:
            q.append(node.left)

        if node.right is None:
            node.right = new_node
            return root
        else:
            q.append(node.right)

#+_____________________________________________________________________________________________+

"""

✅ Problem 6: Find Size of Binary Tree (Recursive)

Logic:
The size of a binary tree is the total number of nodes. 

We compute:

size of left subtree,

size of right subtree, and

add 1 (for the current node).

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_size_recursive(root):
    if root is None:
        return 0
    return 1 + find_size_recursive(root.left) + find_size_recursive(root.right)

# Example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Size of tree:", find_size_recursive(root))  # Output: 5

#+_____________________________________________________________________________________________+

"""
✅ Problem 7: Find Size of Binary Tree (Level Order / Iterative)

Logic:

This approach uses level order traversal (Breadth-First Search) with a queue:

- Start from the root and push it into a queue.

- While the queue is not empty:

        - Remove (dequeue) a node.

        - Count it.

        - Enqueue its left and right children (if they exist).

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_size_level_order(root):
    if root is None:
        return 0

    queue = []
    queue.append(root)
    count = 0

    while len(queue) > 0:
        node = queue.pop(0)  # dequeue (FIFO)
        count += 1

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return count

# Example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Size of tree:", find_size_level_order(root))  # Output: 5

#+_____________________________________________________________________________________________+

"""

✅ Problem 8: Print Binary Tree in Reverse Level Order

Objective:
Print all nodes from bottom to top and left to right within each level.

🔁 Logic (Iterative Approach):

We perform level order traversal, but instead of printing nodes directly:

- Push each visited node’s data onto a stack.

- Enqueue the right child first, then left child – this reverses the level order.

- At the end, pop from the stack and print.

This gives the effect of reverse level order.


🧠 Why right first, then left?
Because stack reverses the order. 

So to print left to right at each level when popped, we must push right first.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def reverse_level_order(root):
    if root is None:
        return

    queue = []
    stack = []

    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)  # dequeue from front
        stack.append(node.data)

        # Enqueue right before left (reversed for stack)
        if node.right is not None:
            queue.append(node.right)
        if node.left is not None:
            queue.append(node.left)

    # Print stack (which gives reverse level order)
    while len(stack) > 0:
        print(stack.pop(), end=' ')

# Example Tree:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
# Output: 4 5 6 7 2 3 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Reverse Level Order Traversal:")
reverse_level_order(root)

#+_____________________________________________________________________________________________+

"""
✅ Problem 9: Delete a Binary Tree

❓Objective:
Delete all nodes of a binary tree.

🧠 Key Idea:

You must delete children nodes first, then the parent.
This naturally fits Postorder Traversal (Left → Right → Root).

We’ll visit all nodes, and as we go back up, delete them.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def delete_binary_tree(root):
    if root is None:
        return

    # Postorder: delete left, then right, then root
    delete_binary_tree(root.left)
    delete_binary_tree(root.right)

    # Simulate deletion by removing references
    print(f"Deleting node: {root.data}")
    root.left = None
    root.right = None
    root.data = None

# Example Tree:
#         1
#       /   \
#      2     3
#     / \
#    4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Deleting Binary Tree:")
delete_binary_tree(root)


"""
In Python, the keyword del root does not actually delete the object itself — it just deletes the name (or reference) root in the current scope.

👑 Summary:
del root just deletes the variable, not the actual Node object.

Python manages memory automatically — just clear references (left, right, data), 
and the garbage collector will delete the object when it's no longer used.

"""


#+_____________________________________________________________________________________________+

"""
✅ Problem 10: Find the Height (or Depth) of a Binary Tree (Recursive)

🔍 Definition
The height (or maximum depth) of a binary tree is the number of nodes on the longest path from the root node down to the farthest leaf node.

Approach (Recursive DFS)

- If tree is empty, return 0.
- Recursively compute the height of left and right subtree.
- The height is max(left, right) + 1.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_depth(root):
    if root is None:
        return 0

    left_height = max_depth(root.left)
    right_height = max_depth(root.right)

    return max(left_height, right_height) + 1

#+_____________________________________________________________________________________________+

"""
Problem 11: Find the Height (or Depth) of a Binary Tree Without Recursion

💡 Approach: BFS (Queue)

Use a queue to do level-order traversal.

Keep track of level depth.

At each level, count nodes and enqueue their children.

Increase depth after each full level is processed.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_depth_iterative(root):
    if root is None:
        return 0

    queue = []
    queue.append(root)
    depth = 0

    while queue:
        level_size = len(queue)  # number of nodes at current level

        # Process all nodes at the current level
        for _ in range(level_size):
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        depth += 1  # increment depth after finishing each level

    return depth


#+_____________________________________________________________________________________________+

"""

Problem 12: Find the Deepest Node in a Binary Tree

🔍 Goal
Return the deepest node in a binary tree (i.e., the last node encountered in a level-order traversal).

🌳 Example Tree
        1
       / \
      2   3
     / \
    4   5
    
Level order: 1 → 2, 3 → 4, 5

Deepest node = 5

💡 Approach: Level Order Traversal (BFS)

Use a queue to perform level-order traversal. The last node processed is the deepest node.

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_deepest_node(root):
    if root is None:
        return None

    queue = []
    queue.append(root)
    node = None

    while queue:
        node = queue.pop(0)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return node.data  # Last node processed

#+_____________________________________________________________________________________________+
  
"""
✅ Problem 14: Find the Number of Leaf Nodes in a Binary Tree (Without Recursion)

🌳 Definition
A leaf node is a node with no left or right child.

💡 Approach: Level Order Traversal (Breadth-First Search)
Use a queue to traverse the tree. For each node, check if both left and right are None. If so, it's a leaf.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_leaf_nodes(root):
    if root is None:
        return 0

    queue = [root]
    count = 0

    while queue:
        node = queue.pop(0)

        # Check if it's a leaf node
        if node.left is None and node.right is None:
            count += 1
        else:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return count



#+_____________________________________________________________________________________________+

"""

✅ Problem 15: Find the Number of Full Nodes in a Binary Tree Without Using Recursion

🔸 Definition:
      A full node is a node that has both left and right children.

🔸 Approach:

 Use level-order traversal (BFS) to visit all nodes. For each node:

- If it has both left and right children → it's a full node.

- Count it.

Example:
        1
       / \
      2   3
     / \   \
    4   5   6

Full nodes: 1 (has both left and right), 2 (has both left and right)

Nodes 3 and 5 are not full (missing one child or leaf)

🟢 Output: 2

"""

from collections import deque

def count_full_nodes(root):
    if not root:
        return 0

    q = deque([root])
    count = 0

    while q:
        node = q.popleft()

        # Check if it is a full node
        if node.left and node.right:
            count += 1

        # Enqueue children
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return count


#+_____________________________________________________________________________________________+

"""
✅ Problem 16: Find the Number of Half Nodes in a Binary Tree Without Recursion

🔸 Definition:
A half node is a node that has exactly one child (either left or right, but not both).

🔸 Approach:
Use level-order traversal (BFS):

Traverse each node in the tree.

If a node has only one child, count it.

Example:

        1
       / \
      2   3
         /
        4
         \
          5

Let’s find half nodes:

2 → no children → ❌

3 → has only left → ✅

4 → has only right → ✅

✅ So the half nodes are: 3 and 4

🟢 Output: 2


"""

from collections import deque

def count_half_nodes(root):
    if not root:
        return 0

    q = deque([root])
    count = 0

    while q:
        node = q.popleft()

        # Check for half node (exactly one child)
        if (node.left is None and node.right is not None) or \
           (node.left is not None and node.right is None):
            count += 1

        # Enqueue children if they exist
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return count

#+_____________________________________________________________________________________________+

"""
✅ Problem 17: Check if Two Binary Trees Are Structurally Identical

🔸 Definition:

Two binary trees are structurally identical if:

Their shapes are exactly the same.
Each corresponding node has the same data.

The left and right children of each node are arranged the same way.

🔸 Approach (Recursive):

- If both nodes are None, return True.

- If one is None and the other isn't, return False.

- If data is not equal, return False.

- Recursively compare:

           - Left subtree of both trees.

           - Right subtree of both trees.

"""

def are_structurally_same(root1, root2):
    # Base case: both are None
    if root1 is None and root2 is None:
        return True
    
    # One is None and the other is not
    if root1 is None or root2 is None:
        return False

    # Check current node data and recurse on left and right
    return (root1.data == root2.data and
            are_structurally_same(root1.left, root2.left) and
            are_structurally_same(root1.right, root2.right))

#+_____________________________________________________________________________________________+

"""
✅ Problem 18: Find the Diameter of a Binary Tree
🔸 Definition:
The diameter (or width) of a binary tree is the length of the longest path between any two nodes in the tree.

This path may or may not pass through the root.

The length is usually measured in number of nodes (or edges – specify clearly which; we'll use number of nodes here).

🔸 Key Insight:
At any node, the longest path that passes through it is:

css
Copy
Edit
height of left subtree + height of right subtree + 1
To find the diameter:

Compute the height of left and right subtrees.

Track the maximum diameter found so far (globally).

Return the height to parent, and update diameter as needed.

Example:

       1
      / \
     2   3
    / \     
   4   5   
   
Longest path: 4 → 2 → 1 → 3 → total 4 nodes

So, diameter = 4

"""

class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.max_diameter = 0  # to store result globally

    def diameter(self, root):
        def height(node):
            if not node:
                return 0
            # Recurse on left and right subtrees
            left = height(node.left)
            right = height(node.right)
            # Update diameter at current node
            self.max_diameter = max(self.max_diameter, left + right + 1)
            # Return height of current node
            return max(left, right) + 1

        height(root)
        return self.max_diameter

#+_____________________________________________________________________________________________+

"""
✅ Problem 19: Find the Width of a Binary Tree

🔸 Definition:
The width of a binary tree at a given level is the number of nodes at that level.

The maximum width is the maximum number of nodes among all levels.

🔸 Algorithm (Level Order Traversal):
We use a queue (BFS) and process level-by-level, tracking the number of nodes per level.

Example:

        1
      /   \
     2     3
    / \   / \
   4  5  6   7

Level 1: 1 → width = 1

Level 2: 2, 3 → width = 2

Level 3: 4, 5, 6, 7 → width = 4 (maximum)


"""

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def max_width(root):
    if not root:
        return 0

    max_width = 0
    queue = deque([root])

    while queue:
        level_width = len(queue)  # Number of nodes at this level
        max_width = max(max_width, level_width)

        for _ in range(level_width):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return max_width

#+_____________________________________________________________________________________________+

"""

✅ Problem 20: Mirror a Binary Tree

🔸 Definition:

To mirror a binary tree, you swap the left and right children of every node.

Original Tree:

     1
   /   \
  2     3
 / \   /
4   5 6

Mirrored Tree:

     1
   /   \
  3     2
   \   / \
    6 5   4

"""


def mirror_tree(node):
    if node is None:
        return None

    # Swap left and right
    node.left, node.right = mirror_tree(node.right), mirror_tree(node.left)
    return node

#+_____________________________________________________________________________________________+


"""
✅ Problem 21: Find the Lowest Common Ancestor (LCA) in a Binary Tree

🔸 Definition:

The Lowest Common Ancestor (LCA) of two nodes p and q in a binary tree is the lowest (deepest) node 
that has both p and q as descendants (where a node can be a descendant of itself).

🔸 Algorithm (Recursive Traversal):

1. If root is None, return None.
2. If root is either p or q, return root.
3. Recur on the left and right subtree.
4. If both sides return a node, current root is LCA.
5. If only one side returns a node, return that node.
6. If neither returns, return None.

Example:
        1
      /   \
     2     3
    / \   / \
   4   5 6   7

LCA of 4 and 5 is → 2

LCA of 4 and 6 is → 1

LCA of 3 and 7 is → 3

"""

class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def find_LCA(root, p, q):
    if root is None:
        return None

    if root.data == p or root.data == q:
        return root

    left_lca = find_LCA(root.left, p, q)
    right_lca = find_LCA(root.right, p, q)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca else right_lca

#+_____________________________________________________________________________________________+
