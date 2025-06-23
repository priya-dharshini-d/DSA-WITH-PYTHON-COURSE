def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# ---------------- MAX HEAP FUNCTIONS ----------------
def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def insert_into_max_heap(arr, value):
    arr.append(value)
    i = len(arr) - 1
    while i > 0 and arr[(i - 1) // 2] < arr[i]:
        swap(arr, i, (i - 1) // 2)
        i = (i - 1) // 2

def delete_even_elements_from_max_heap(arr):
    filtered = [x for x in arr if x % 2 != 0]
    build_max_heap(filtered)
    return filtered

def print_max_heap(arr):
    print("Max Heap:", ' '.join(map(str, arr)))

# ---------------- MIN HEAP FUNCTIONS ----------------
def min_heapify(heap, size, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and heap[left] < heap[smallest]:
        smallest = left
    if right < size and heap[right] < heap[smallest]:
        smallest = right

    if smallest != i:
        swap(heap, i, smallest)
        min_heapify(heap, size, smallest)

def build_min_heap(heap):
    size = len(heap)
    for i in range((size // 2) - 1, -1, -1):
        min_heapify(heap, size, i)

def insert_into_min_heap(heap, value):
    heap.append(value)
    i = len(heap) - 1
    while i > 0 and heap[(i - 1) // 2] > heap[i]:
        swap(heap, i, (i - 1) // 2)
        i = (i - 1) // 2

def print_min_heap(heap):
    print("Min Heap:", ' '.join(map(str, heap)))

# ---------------- MAIN FUNCTION ----------------
def main():
    # Input and build max heap
    n = int(input("Enter number of elements: "))
    values = list(map(int, input("Enter the elements: ").split()))

    max_heap = []
    for value in values:
        insert_into_max_heap(max_heap, value)

    print_max_heap(max_heap)

    # Insert a new element into max heap
    new_val = int(input("Enter new element to insert into max heap: "))
    insert_into_max_heap(max_heap, new_val)
    print("After insertion:")
    print_max_heap(max_heap)

    # Delete even elements
    max_heap = delete_even_elements_from_max_heap(max_heap)
    print("After deleting even elements:")
    print_max_heap(max_heap)

    # Now build min heap from new user input
    m = int(input("Enter number of elements for min heap: "))
    min_values = list(map(int, input("Enter the elements: ").split()))
    min_heap = []

    for value in min_values:
        insert_into_min_heap(min_heap, value)

    build_min_heap(min_heap)
    print_min_heap(min_heap)

if __name__ == "__main__":
    main()
