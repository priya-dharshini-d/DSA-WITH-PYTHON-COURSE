class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0  # initialize length

    # 1. Append (Insert at End)
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    # 2. Prepend (Insert at Beginning)
    def prepend(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # 3. Insert at Position (0-based index)
    def insert_at_position(self, data, position):
        if position > self.length or position < 0:
            print("Invalid position")
            return

        if position == 0:
            self.prepend(data)
        elif position == self.length:
            self.append(data)
        else:
            new_node = Node(data)
            count = 0
            current = self.head
            while count < position - 1:
                count += 1
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.length += 1

    # 4. Delete from Beginning
    def delete_from_beginning(self):
        if self.length == 0:
            print("List is empty")
        else:
            temp = self.head
            self.head = self.head.next
            del temp
            self.length -= 1

    # 5. Delete from End
    def delete_from_end(self):
        if self.length == 0:
            print("List is empty")
            return

        if self.head.next is None:
            del self.head
            self.head = None
            self.length -= 1
            return

        current = self.head
        while current.next.next:
            current = current.next

        temp = current.next
        current.next = None
        del temp
        self.length -= 1

    # 6. Delete from Position (0-based index)
    def delete_from_position(self, position):
        if position < 0 or position >= self.length:
            print("Invalid position. Please enter a position between 0 and", self.length - 1)
            return

        if position == 0:
            self.delete_from_beginning()
            return

        if position == self.length - 1:
            self.delete_from_end()
            return

        current = self.head
        count = 0
        while count < position - 1:
            current = current.next
            count += 1

        temp = current.next
        current.next = temp.next
        del temp
        self.length -= 1

    # 7. Delete by Value (simplified and corrected)
    def delete_by_value(self, value):
        if self.length == 0 or not self.head:
            print("List is empty")
            return

        if self.head.data == value:
            self.delete_from_beginning()
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                temp = current.next
                current.next = temp.next
                del temp
                self.length -= 1
                return
            current = current.next

        print("Value not found")

    # 8. Count Nodes
    def count_nodes(self):
        return self.length

    # 9. Display List
    def display(self):
        current = self.head
        if not current:
            print("List is empty")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # 10. Delete Entire List
    def delete_entire_list(self):
        self.head = None
        self.length = 0
        print("List has been cleared.")

    # 11. Delete by Node (corrected and indented)
    def delete_by_node(self, node_to_delete):
        if self.head is None or self.length == 0:
            print("List is empty")
            return

        if self.head == node_to_delete:
            self.delete_from_beginning()
            return

        current = self.head
        while current.next and current.next != node_to_delete:
            current = current.next

        if current.next == node_to_delete:
            current.next = node_to_delete.next
            del node_to_delete
            self.length -= 1
            return

        print("Node not found in the list")


# 🔍 Testing All Operations
if __name__ == "__main__":
    ll = LinkedList()

    print("\n--- Append 10, 20, 30 ---")
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.display()

    print("\n--- Prepend 5 ---")
    ll.prepend(5)
    ll.display()

    print("\n--- Insert 15 at position 2 ---")
    ll.insert_at_position(15, 2)
    ll.display()

    print("\n--- Delete from Beginning ---")
    ll.delete_from_beginning()
    ll.display()

    print("\n--- Delete from End ---")
    ll.delete_from_end()
    ll.display()

    print("\n--- Delete from Position 1 ---")
    ll.delete_from_position(1)
    ll.display()

    print("\n--- Delete by Value 10 ---")
    ll.delete_by_value(10)
    ll.display()

    print("\n--- Append 100 and 200 for node deletion test ---")
    ll.append(100)
    ll.append(200)
    ll.display()

    print("\n--- Delete by Node (100) ---")
    node_to_delete = ll.head.next  # This should be node with data 100
    ll.delete_by_node(node_to_delete)
    ll.display()

    print("\n--- Count Nodes ---")
    print("Total nodes:", ll.count_nodes())

    print("\n--- Delete Entire List ---")
    ll.delete_entire_list()
    ll.display()



"""
Output:


--- Append 10, 20, 30 ---
10 -> 20 -> 30 -> None

--- Prepend 5 ---
5 -> 10 -> 20 -> 30 -> None

--- Insert 15 at position 2 ---
5 -> 10 -> 15 -> 20 -> 30 -> None

--- Delete from Beginning ---
10 -> 15 -> 20 -> 30 -> None

--- Delete from End ---
10 -> 15 -> 20 -> None

--- Delete from Position 1 ---
10 -> 20 -> None

--- Delete by Value 10 ---
20 -> None

--- Append 100 and 200 for node deletion test ---
20 -> 100 -> 200 -> None

--- Delete by Node (100) ---
20 -> 200 -> None

--- Count Nodes ---
Total nodes: 2

--- Delete Entire List ---
List has been cleared.
List is empty

"""
