class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Previous node
        self.next = None  # Next node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    # 1. Append (Insert at End)
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # List is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Go to last node
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.length += 1

    # 2. Prepend (Insert at Beginning)
    def prepend(self, data):
        new_node = Node(data)
        if self.head:  # If list is not empty
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        self.length += 1

    # 3. Insert at Position (0-based)
    def insert_at_position(self, data, position):
        if position < 0 or position > self.length:
            print("Invalid position")
            return

        if position == 0:
            self.prepend(data)
        elif position == self.length:
            self.append(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
            self.length += 1

    # 4. Delete from Beginning
    def delete_from_beginning(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        del temp
        self.length -= 1

    # 5. Delete from End
    def delete_from_end(self):
        if not self.head:
            print("List is empty")
            return

        if not self.head.next:  # Only one node
            del self.head
            self.head = None
        else:
            current = self.head
            while current.next:
                current = current.next
            current.prev.next = None
            del current
        self.length -= 1

    # 6. Delete from Position
    def delete_from_position(self, position):
        if position < 0 or position >= self.length:
            print("Invalid position")
            return

        if position == 0:
            self.delete_from_beginning()
        elif position == self.length - 1:
            self.delete_from_end()
        else:
            current = self.head
            for _ in range(position):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            del current
            self.length -= 1

    # 7. Delete by Value
    def delete_by_value(self, value):
        if not self.head:
            print("List is empty")
            return

        current = self.head
        while current:
            if current.data == value:
                if current == self.head:
                    self.delete_from_beginning()
                elif current.next is None:
                    self.delete_from_end()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    del current
                    self.length -= 1
                return
            current = current.next

        print("Value not found")

    # 8. Delete by Node
    def delete_by_node(self, node_to_delete):
        if not self.head or not node_to_delete:
            print("List is empty or node is None")
            return

        if node_to_delete == self.head:
            self.delete_from_beginning()
        elif node_to_delete.next is None:
            self.delete_from_end()
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev
            del node_to_delete
            self.length -= 1

    # 9. Count Nodes
    def count_nodes(self):
        return self.length

    # 10. Display the List
    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # 11. Clear Entire List
    def clear(self):
        self.head = None
        self.length = 0
        print("List has been cleared.")


# 🔍 Testing All Operations
if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("\n--- Append 10, 20, 30 ---")
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.display()

    print("\n--- Prepend 5 ---")
    dll.prepend(5)
    dll.display()

    print("\n--- Insert 15 at position 2 ---")
    dll.insert_at_position(15, 2)
    dll.display()

    print("\n--- Delete from Beginning ---")
    dll.delete_from_beginning()
    dll.display()

    print("\n--- Delete from End ---")
    dll.delete_from_end()
    dll.display()

    print("\n--- Delete from Position 1 ---")
    dll.delete_from_position(1)
    dll.display()

    print("\n--- Delete by Value 10 ---")
    dll.delete_by_value(10)
    dll.display()

    print("\n--- Append 100 and 200 for delete_by_node test ---")
    dll.append(100)
    dll.append(200)
    dll.display()

    print("\n--- Delete by Node (100) ---")
    node_to_delete = dll.head.next  # Assuming it's the node with 100
    dll.delete_by_node(node_to_delete)
    dll.display()

    print("\n--- Count Nodes ---")
    print("Total nodes:", dll.count_nodes())

    print("\n--- Clear Entire List ---")
    dll.clear()
    dll.display()

"""

--- Append 10, 20, 30 ---
10 <-> 20 <-> 30 <-> None

--- Prepend 5 ---
5 <-> 10 <-> 20 <-> 30 <-> None

--- Insert 15 at position 2 ---
5 <-> 10 <-> 15 <-> 20 <-> 30 <-> None

--- Delete from Beginning ---
10 <-> 15 <-> 20 <-> 30 <-> None

--- Delete from End ---
10 <-> 15 <-> 20 <-> None

--- Delete from Position 1 ---
10 <-> 20 <-> None

--- Delete by Value 10 ---
20 <-> None

--- Append 100 and 200 for delete_by_node test ---
20 <-> 100 <-> 200 <-> None

--- Delete by Node (100) ---
20 <-> 200 <-> None

--- Count Nodes ---
Total nodes: 2

--- Clear Entire List ---
List has been cleared.
List is empty

"""



# Search for an element in a Doubly Linked List (DLL) in Python.

# Doubly Linked List Node
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Function to search in Doubly Linked List

def search_dll(head, key):
  
    current = head
  
    while current:
      
        if current.data == key:
            return True
          
        current = current.next
      
    return False

# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":

    # Create Doubly Linked List: 10 <-> 20 <-> 30
    dll_node1 = DLLNode(10)
    dll_node2 = DLLNode(20)
    dll_node3 = DLLNode(30)
  
    dll_node1.next = dll_node2
    dll_node2.prev = dll_node1
    dll_node2.next = dll_node3
    dll_node3.prev = dll_node2
  
    dll_head = dll_node1

    # Search in DLL
    print("\nSearching in Doubly Linked List:")
    print("Is 30 in DLL?", search_dll(dll_head, 30))  # True
    print("Is 100 in DLL?", search_dll(dll_head, 100))  # False


"""

Searching in Singly Linked List:
Is 2 in SLL? True
Is 5 in SLL? False

Searching in Doubly Linked List:
Is 30 in DLL? True
Is 100 in DLL? False

"""


# Reversing  Dll (iteratively and recursively)


# DLL Node
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Reverse DLL - Iterative

def reverse_dll_iterative(head):
  
    current = head
    prev = None
  
    while current:
      
        current.prev, current.next = current.next, current.prev
        prev = current
        current = current.prev
      
    return prev

# Reverse DLL - Recursive

def reverse_dll_recursive(head):
  
    if head is None:
        return None
      
    head.prev, head.next = head.next, head.prev
  
    if head.prev is None:
        return head
      
    return reverse_dll_recursive(head.prev)


#+___________________________________________________________________________________________________________________________________+



class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

  
    # Reverse DLL - Iterative
    def reverse_iterative(self):
      
        current = self.head
        prev = None
      
        while current:
            current.prev, current.next = current.next, current.prev
            prev = current
            current = current.prev
          
        self.head = prev

  
    # Reverse DLL - Recursive

    def _reverse_dll_recursive(self, head):
      
      if head is None:
          return None
        
      head.prev, head.next = head.next, head.prev
      
      if head.prev is None:
          return head
        
      return self._reverse_dll_recursive(head.prev)


    def reverse_recursive(self):
        self.head = self._reverse_dll_recursive(self.head)

#+___________________________________________________________________________________________________________________________________+
