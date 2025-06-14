class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
  
    def __init__(self):
        self.head = None
        self.length = 0

    # 1. Append
    def append(self, data):
        new_node = Node(data)
      
        if not self.head:
            self.head = new_node
            new_node.next = self.head
          
        else:
            current = self.head
          
            while current.next != self.head:
                current = current.next
              
            current.next = new_node
            new_node.next = self.head
          
        self.length += 1

    # 2. Prepend
    def prepend(self, data):
        new_node = Node(data)
      
        if not self.head:
            self.head = new_node
            new_node.next = new_node
          
        else:
            current = self.head
          
            while current.next != self.head:
                current = current.next
              
            new_node.next = self.head
            self.head = new_node
            current.next = self.head
          
        self.length += 1

    # 3. Insert at position
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
            current.next = new_node
          
            self.length += 1

    # 4. Delete from beginning
    def delete_from_beginning(self):
      
        if not self.head:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
          
        else:
            current = self.head
          
            while current.next != self.head:
                current = current.next
              
            temp = self.head
            self.head = self.head.next
            current.next = self.head
          
            del temp
          
        self.length -= 1

    # 5. Delete from end
    def delete_from_end(self):
      
        if not self.head:
            print("List is empty")
            return

        if self.head.next == self.head:
            del self.head
            self.head = None
          
        else:
          
            current = self.head
          
            while current.next.next != self.head:
                current = current.next
              
            temp = current.next
            current.next = self.head
          
            del temp
          
        self.length -= 1

    # 6. Delete from position
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
            for _ in range(position - 1):
                current = current.next
              
            temp = current.next
            current.next = temp.next
          
            del temp
            self.length -= 1

    # 7. Delete by value
    def delete_by_value(self, value):
      
        if not self.head:
            print("List is empty")
            return

        current = self.head
        prev = None

        while True:
            if current.data == value:
              
                if prev:
                    prev.next = current.next
                  
                else:
                    self.delete_from_beginning()
                    return

                if current == self.head:
                    self.head = current.next

                del current
                self.length -= 1
                return

            prev = current
            current = current.next
          
            if current == self.head:
                break

        print("Value not found")

    # 8. Count nodes
    def count_nodes(self):
        return self.length

    # 9. Display list
    def display(self):
      
        if not self.head:
            print("List is empty")
            return

        current = self.head
      
        while True:
          
            print(current.data, end=" -> ")
            current = current.next
          
            if current == self.head:
                break
              
        print("(head)")

    # 10. Delete entire list
  
    def delete_entire_list(self):
      
        if not self.head:
            print("List is already empty")
            return

        current = self.head.next
      
        while current != self.head:
            temp = current
            current = current.next
            del temp

        del self.head
        self.head = None
        self.length = 0
        print("List has been cleared.")

    # 11. Delete by node reference
    def delete_by_node(self, node_to_delete):
      
        if not self.head:
            print("List is empty")
            return

        if self.head == node_to_delete:
            self.delete_from_beginning()
            return

        current = self.head
      
        while current.next != self.head:
          
            if current.next == node_to_delete:
                current.next = node_to_delete.next
                del node_to_delete
                self.length -= 1
                return
              
            current = current.next

        print("Node not found in the list")


# 🔍 Testing All Operations
if __name__ == "__main__":
    cll = CircularLinkedList()

    print("\n--- Append 10, 20, 30 ---")
    cll.append(10)
    cll.append(20)
    cll.append(30)
    cll.display()

    print("\n--- Prepend 5 ---")
    cll.prepend(5)
    cll.display()

    print("\n--- Insert 15 at position 2 ---")
    cll.insert_at_position(15, 2)
    cll.display()

    print("\n--- Delete from Beginning ---")
    cll.delete_from_beginning()
    cll.display()

    print("\n--- Delete from End ---")
    cll.delete_from_end()
    cll.display()

    print("\n--- Delete from Position 1 ---")
    cll.delete_from_position(1)
    cll.display()

    print("\n--- Delete by Value 10 ---")
    cll.delete_by_value(10)
    cll.display()

    print("\n--- Append 100 and 200 for node deletion test ---")
    cll.append(100)
    cll.append(200)
    cll.display()

    print("\n--- Delete by Node (100) ---")
    node_to_delete = cll.head.next  # This should be node with data 100
    cll.delete_by_node(node_to_delete)
    cll.display()

    print("\n--- Count Nodes ---")
    print("Total nodes:", cll.count_nodes())

    print("\n--- Delete Entire List ---")
    cll.delete_entire_list()
    cll.display()

"""
--- Append 10, 20, 30 ---
10 -> 20 -> 30 -> (head)

--- Prepend 5 ---
5 -> 10 -> 20 -> 30 -> (head)

--- Insert 15 at position 2 ---
5 -> 10 -> 15 -> 20 -> 30 -> (head)

--- Delete from Beginning ---
10 -> 15 -> 20 -> 30 -> (head)

--- Delete from End ---
10 -> 15 -> 20 -> (head)

--- Delete from Position 1 ---
10 -> 20 -> (head)

--- Delete by Value 10 ---
20 -> (head)

--- Append 100 and 200 for node deletion test ---
20 -> 100 -> 200 -> (head)

--- Delete by Node (100) ---
20 -> 200 -> (head)

--- Count Nodes ---
Total nodes: 2

--- Delete Entire List ---
List has been cleared.
List is empty

"""


# Reversing the CSLL

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

  
    # ✅ Recursive Reverse
  
    def reverse_recursive_util(self, current, prev):
        next_node = current.next
        current.next = prev
      
        if next_node == self.head:
            self.head.next = current
            self.head = current
            return
          
        self.reverse_recursive_util(next_node, current)
    

    def reverse_recursive(self):
        if not self.head or self.head.next == self.head:
            return
        self.reverse_recursive_util(self.head, None)


    # ✅ Iterative Reverse
  
    def reverse_iterative(self):
      
        if not self.head or self.head.next == self.head:
            return
          
        prev = None
        current = self.head
        next_node = current.next

        while True:
          
            current.next = prev
            prev = current
            current = next_node
            next_node = next_node.next
          
            if current == self.head:
                break

        self.head.next = prev
        self.head = prev


# 🔍 Test Code
if __name__ == "__main__":
    cll = CircularLinkedList()

    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.append(4)

    print("Original list:")
    cll.display()

    print("\nReversed Recursively:")
    cll.reverse_recursive()
    cll.display()
    
    print("\nReversed Iteratively:")
    cll.reverse_iterative()
    cll.display()

"""

Original list:
1 -> 2 -> 3 -> 4 -> (head)

Reversed Recursively:
4 -> 3 -> 2 -> 1 -> (head)

Reversed Iteratively:
1 -> 2 -> 3 -> 4 -> (head)

"""


