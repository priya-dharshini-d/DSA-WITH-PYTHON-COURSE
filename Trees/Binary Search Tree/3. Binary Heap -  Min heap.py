class MinHeap:
    def __init__(self):
        self.heap = [0]  # Dummy at index 0
        self.size = 0

    def get_parent_index(self, index):
        return index // 2

    def get_left_child_index(self, index):
        return 2 * index

    def get_right_child_index(self, index):
        return 2 * index + 1

    def get_min(self):
        return None if self.size == 0 else self.heap[1]

    def bubble_up(self, index):
        while index > 1:
            parent = self.get_parent_index(index)
            if self.heap[index] < self.heap[parent]:  # < for MinHeap
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.bubble_up(self.size)

    def bubble_down(self, index):
        while index * 2 <= self.size:
            smaller_child = self.get_smaller_child_index(index)
            if self.heap[index] > self.heap[smaller_child]:  # > for MinHeap
                self.heap[index], self.heap[smaller_child] = self.heap[smaller_child], self.heap[index]
            index = smaller_child

    def get_smaller_child_index(self, index):
        left = self.get_left_child_index(index)
        right = self.get_right_child_index(index)
        if right > self.size:
            return left
        
        if self.heap[left] < self.heap[right]:  # < for MinHeap
            return left 
        else:
            return right

    def delete_min(self):
        if self.size == 0:
            return None
        min_value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        
        self.bubble_down(1)
        return min_value

    def build_from_list(self, nums):
        self.size = len(nums)
        self.heap = [0] + nums[:]
        for i in range(self.size // 2, 0, -1):
            self.bubble_down(i)
