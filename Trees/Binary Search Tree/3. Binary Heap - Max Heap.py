class MaxHeap:
    def __init__(self):
        self.heap = [0]  # Dummy at index 0 for easier index math
        self.size = 0

    def get_parent_index(self, index):
        return index // 2

    def get_left_child_index(self, index):
        return 2 * index

    def get_right_child_index(self, index):
        return 2 * index + 1

    def get_max(self):
        return None if self.size == 0 else self.heap[1]

    def bubble_up(self, index):
        while index > 1:
            parent = self.get_parent_index(index)
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.bubble_up(self.size)

    def bubble_down(self, index):
        while index * 2 <= self.size:
            larger_child = self.get_larger_child_index(index)
            if self.heap[index] < self.heap[larger_child]:
                self.heap[index], self.heap[larger_child] = self.heap[larger_child], self.heap[index]
            index = larger_child

    def get_larger_child_index(self, index):
        left = self.get_left_child_index(index)
        right = self.get_right_child_index(index)
        if right > self.size:
            return left
        
        if self.heap[left] > self.heap[right]:
            return left 
        else:
            return right

    def delete_max(self):
        if self.size == 0:
            return None
        max_value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        
        self.bubble_down(1)
        return max_value

    def build_from_list(self, nums):
        self.size = len(nums)
        self.heap = [0] + nums[:]
        for i in range(self.size // 2, 0, -1):
            self.bubble_down(i)

# ------------------ Test Code ------------------

heap = MaxHeap()
heap.build_from_list([9, 5, 6, 2, 3])
print("Max Heap:", heap.heap[1:])

heap.insert(10)
print("After insert(10):", heap.heap[1:])

print("Peek max:", heap.get_max())

print("Deleted max:", heap.delete_max())
print("After delete_max():", heap.heap[1:])


"""
 Why is it helpful?
 
In a binary heap, for any element at index i:

Parent is at i // 2

Left child is at 2 * i

Right child is at 2 * i + 1

These formulas work only if indexing starts at 1 (not 0). So by adding a dummy at index 0:

The actual heap starts from index 1

Index math becomes clean and avoids needing special cases



"""
