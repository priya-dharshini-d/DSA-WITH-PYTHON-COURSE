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

#+____________________________________________________________________________+

# A Python program to demonstrate common binary heap operations

# Import the heap functions from python library
from heapq import heappush, heappop, heapify 

"""
# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintainin heap invarient
# heapify - transform list into heap, in place, in linear time
"""

# A class for Min Heap
class MinHeap:
    
    # Constructor to initialize a heap
    def __init__(self):
        self.heap = [] 

    def parent(self, i):
        return (i-1)/2
    
    # Inserts a new key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)           

    # Decrease value of key at index 'i' to new_val It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self, i, new_val):
        self.heap[i]  = new_val 
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i] , self.heap[self.parent(i)] = (
            self.heap[self.parent(i)], self.heap[i])
            
    # Method to remove minimum element from min heap
    def extractMin(self):
        return heappop(self.heap)

    # This function deletes key at index i. It first reduces value to minus infinite and then calls extractMin()
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]


heapObj = MinHeap()
heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.deleteKey(1)
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(45)

print heapObj.extractMin(),
print heapObj.getMin(),
heapObj.decreaseKey(2, 1)
print heapObj.getMin()

