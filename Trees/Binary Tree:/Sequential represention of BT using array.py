"""

✅ Binary Tree using Array (Sequential Representation)

💡 Concept:

Binary trees can be represented in arrays by indexing nodes level-wise from top to bottom, left to right. (Level order)


For any node at index i: (0-based index)

Left child → 2*i + 1

Right child → 2*i + 2

Parent → (i - 1) // 2

___________________________________________________________________________________________________________

(1-based index)

Left child → 2*i

Right child → 2*i + 1

Parent → i // 2


"""

class ArrayBinaryTree:
    def __init__(self, size):
        self.tree = [None] * size  # fixed size
        self.size = size
        self.last_index = -1  # track last inserted index

    # Insert element in next available position
    def insert(self, value):
        if self.last_index + 1 >= self.size:
            print("Tree is full")
            return
        self.last_index += 1
        self.tree[self.last_index] = value

    # Traverse: Inorder (Left - Root - Right)
    def inorder(self, index=0):
        if index > self.last_index or self.tree[index] is None:
            return
        self.inorder(2 * index + 1)
        print(self.tree[index], end=' ')
        self.inorder(2 * index + 2)

    # Traverse: Preorder (Root - Left - Right)
    def preorder(self, index=0):
        if index > self.last_index or self.tree[index] is None:
            return
        print(self.tree[index], end=' ')
        self.preorder(2 * index + 1)
        self.preorder(2 * index + 2)

    # Traverse: Postorder (Left - Right - Root)
    def postorder(self, index=0):
        if index > self.last_index or self.tree[index] is None:
            return
        self.postorder(2 * index + 1)
        self.postorder(2 * index + 2)
        print(self.tree[index], end=' ')

    # Display tree as array
    def display(self):
        print("Array Representation:", self.tree)

# Example usage
bt = ArrayBinaryTree(10)
for val in [10, 20, 30, 40, 50, 60]:
    bt.insert(val)

bt.display()
print("Inorder Traversal:")
bt.inorder()
print("\nPreorder Traversal:")
bt.preorder()
print("\nPostorder Traversal:")
bt.postorder()


"""
__________________________________________________________________________
Array Representation: [10, 20, 30, 40, 50, 60, None, None, None, None]

Inorder Traversal:
40 20 50 10 60 30 

Preorder Traversal:
10 20 40 50 30 60 

Postorder Traversal:
40 50 20 60 30 10 

"""
