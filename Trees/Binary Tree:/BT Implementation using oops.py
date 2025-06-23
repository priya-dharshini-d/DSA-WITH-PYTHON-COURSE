
#______________________________________________________________________________________________________________________________

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            if curr.left is None:
                curr.left = new_node
                return
            else:
                queue.append(curr.left)
            if curr.right is None:
                curr.right = new_node
                return
            else:
                queue.append(curr.right)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=' ')
        self.inorder(node.right)

    def preorder(self, node):
        if node is None:
            return
        print(node.data, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=' ')

    def level_order(self):
        if self.root is None:
            print("Tree is empty.")
          
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.data, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
              
    def search(self, key):
        if self.root is None:
            return False

        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            if curr.data == key:
                return True
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return False
      
    def delete(self, key):
        if self.root is None:
            return  "Nothing to delete. Binary Tree is empty."

        queue = deque([self.root])
        key_node = None
        last_node = None
        parent_of_last = None

        while queue:
            curr = queue.popleft()
            if curr.data == key:
                key_node = curr
            if curr.left:
                parent_of_last = curr
                queue.append(curr.left)
            if curr.right:
                parent_of_last = curr
                queue.append(curr.right)
            last_node = curr

        if key_node:
            key_node.data = last_node.data  # Copy last node's data
            # Delete deepest node
            if parent_of_last:
                if parent_of_last.right == last_node:
                    parent_of_last.right = None
                elif parent_of_last.left == last_node:
                    parent_of_last.left = None


  """

    if key_node: 
        key_node.data = last_node.data   # To be simple use this
        self.delete_deepest(last_node)
        
  """

  
    def delete_deepest(self, d_node):
        
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
          
            if curr.left:
                if curr.left == d_node:
                    curr.left = None
                    return
                queue.append(curr.left)
              
            if curr.right:
                if curr.right == d_node:
                    curr.right = None
                    return
                queue.append(curr.right)
                  


# ---------- Example usage ----------
if __name__ == "__main__":
    bt = BinaryTree()

    # Inserting values
    for val in [10, 20, 30, 40, 50, 60, 70]:
        bt.insert(val)

    # Tree structure will look like:
    #            10
    #         /     \
    #       20       30
    #     /   \     /   \
    #   40    50  60    70

    print("Inorder Traversal: ", end=''); bt.inorder(bt.root)
    print("\nPreorder Traversal: ", end=''); bt.preorder(bt.root)
    print("\nPostorder Traversal: ", end=''); bt.postorder(bt.root)
    print("\nLevel Order Traversal: ", end=''); bt.level_order()




"""
def inorder(self): 
    if self.head is None: 
        return
    self.inorder(self.head.left) 
    print(self.head.data, end=' ') 
    self.inorder(self.head.right)
    
❗ Issues:
self.head is never updated — it always refers to the same node, leading to infinite recursion or wrong logic.

So use node as parameter and

call like this bt.inorder(bt.root)  # Correct call
"""
#______________________________________________________________________________________________________________________________
















