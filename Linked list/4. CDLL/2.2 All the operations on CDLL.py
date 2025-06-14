
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

# 1. Append
  
    def append(self, data):
      
        new_node = Node(data)
      
        if not self.head:
            new_node.next = new_node.prev = new_node
            self.head = new_node
          
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
          
        self.length += 1

# 2. Prepend
  
    def prepend(self, data):
        new_node = Node(data)
      
        if not self.head:
            new_node.next = new_node.prev = new_node
            self.head = new_node
          
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = new_node
            self.head.prev = new_node
            self.head = new_node
          
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
          
            for _ in range(position):
                current = current.next
              
            prev_node = current.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = current
            current.prev = new_node
          
            self.length += 1

# 4. Delete from beginning
  
    def delete_from_beginning(self):
      
        if not self.head:
            print("List is empty")
            return
          
        if self.length == 1:
            self.head = None
          
        else:
            tail = self.head.prev
            self.head = self.head.next
            self.head.prev = tail
            tail.next = self.head
          
        self.length -= 1

# 5. Delete from end
  
    def delete_from_end(self):
      
        if not self.head:
            print("List is empty")
            return
          
        if self.length == 1:
            self.head = None
          
        else:
            tail = self.head.prev
            new_tail = tail.prev
            new_tail.next = self.head
            self.head.prev = new_tail
          
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
          
            for _ in range(position):
                current = current.next
              
            current.prev.next = current.next
            current.next.prev = current.prev
          
            self.length -= 1

  
# 7. Delete by value

  
    def delete_by_value(self, value):
      
        if not self.head:
            print("List is empty")
            return
          
        current = self.head
        for _ in range(self.length):
          
            if current.data == value:
                if current == self.head:
                    self.delete_from_beginning()
                  
                elif current == self.head.prev:
                    self.delete_from_end()
                  
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                  
                    self.length -= 1
                return
              
            current = current.next
        print("Value not found")

  
# 8. Count nodes
  
    def count_nodes(self):
        return self.length

# 9. Display

    def display(self):
      
        if not self.head:
            print("DCLL is empty")
            return
          
        current = self.head
      
        while True:
            print(current.data, end=" <-> ")
          
            current = current.next
          
            if current == self.head:
                break
        print("(head)")
      

# 10. Search
  
    def search(self, value):
      
        if not self.head:
            print("DCLL is empty")
            return -1
          
        current = self.head
        index = 0
      
        while True:
          
            if current.data == value:
                print(f"[DCLL] Value {value} found at position {index}")
                return index
              
            current = current.next
            index += 1
          
            if current == self.head:
                break
        print(f"[DCLL] Value {value} not found")
        return -1

  
# 11. Delete entire list
  
    def delete_entire_list(self):
        self.head = None
        self.length = 0
        print("List has been cleared.")

  
# 12. Delete by node reference
  
    def delete_by_node(self, node_to_delete):
      
        if not self.head:
            print("List is empty")
            return
          
        if node_to_delete == self.head:
            self.delete_from_beginning()
            return
          
        current = self.head.next
      
        while current != self.head:
          
            if current == node_to_delete:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.length -= 1
                return
              
            current = current.next
          
        print("Node not found in the list")


  
# 13. Reverse Iterative
  
    def reverse_iterative(self):
      
        if not self.head or self.length == 1:
            return
          
        current = self.head
      
        for _ in range(self.length):
            current.prev, current.next = current.next, current.prev
            current = current.prev
          
        self.head = self.head.prev

  
# 14. Reverse Recursive
  
    def reverse_recursive_util(self, current, count):
      
        current.prev, current.next = current.next, current.prev
      
        if count == self.length - 1:
            self.head = current
            return
          
        self.reverse_recursive_util(current.prev, count + 1)

    def reverse_recursive(self):
      
        if not self.head or self.length == 1:
            return
          
        self.reverse_recursive_util(self.head, 0)
