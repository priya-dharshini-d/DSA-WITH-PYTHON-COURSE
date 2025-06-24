class Heap:
    def __init__(self):
        self.heapList = [0]  # Index 0 is dummy
        self.size = 0

    def parent(self, index):
        return index // 2

    def left_child(self, index):
        return 2 * index

    def right_child(self, index):
        return 2 * index + 1

    def get_min(self):
        if self.size == 0:
            return None
        return self.heapList[1]

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:  # < for min-heap
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def insert(self, item):
        self.heapList.append(item)
        self.size += 1
        self.percolate_up(self.size)

    def percolate_down(self, i):
        while (i * 2) <= self.size:
            min_child = self.min_child(i)
            if self.heapList[i] > self.heapList[min_child]:  # > for min-heap
                self.heapList[i], self.heapList[min_child] = self.heapList[min_child], self.heapList[i]
            i = min_child

    def min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:  # < for min-heap
                return i * 2
            else:
                return i * 2 + 1

    def delete_min(self):
        if self.size == 0:
            return None
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size -= 1
        self.heapList.pop()
        self.percolate_down(1)
        return retval

    def build_heap_from_array(self, A):                #O(n) build-heap is faster than inserting elements one-by-one (O(n log n)).
        i = len(A) // 2
        self.size = len(A)
        self.heapList = [0] + A[:]
        while i > 0:
            self.percolate_down(i)
            i -= 1
h = Heap()
h.build_heap_from_array([9, 5, 6, 2, 3])
print("Min Heap array:", h.heapList[1:])  # Ignore dummy at index 0

h.insert(1)
print("After insert(1):", h.heapList[1:])

print("Min element (peek):", h.get_min())

print("Deleted min:", h.delete_min())
print("After delete_min():", h.heapList[1:])
