"""

- Finding the middle element.

- Merging two sorted linked lists into one sorted list.

- Finding the nth node from the end.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node


    def display(self):
        current_node = self.head
        if not current_node:
            print("List is empty")
            return
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Find the Middle Element (Using Two Pointers)
  
    def find_middle(self):
        current_node = self.head
        node_count = 0

        # Count the number of nodes in the list
        while current_node:
            node_count += 1
            current_node = current_node.next

        # Find the middle node by going to the (node_count // 2)th node
      
        if node_count == 0:
            print("List is empty")
            return
          
        middle_index = node_count // 2
        current_node = self.head
      
        for _ in range(middle_index):
            current_node = current_node.next
          
        print(f"Middle Element: {current_node.data}")


 #  Merge Two Sorted Lists into One Sorted List
  
    @staticmethod
    def merge_sorted_lists(first_list, second_list):
        merged_head = None
        merged_tail = None

        # Iterate through both lists and merge them in sorted order
        while first_list and second_list:
            if first_list.data < second_list.data:
                next_node = first_list
                first_list = first_list.next
            else:
                next_node = second_list
                second_list = second_list.next

            if not merged_head:
                merged_head = next_node
                merged_tail = merged_head
            else:
                merged_tail.next = next_node
                merged_tail = merged_tail.next

        # If one of the lists is not exhausted, link the rest
        if first_list:
            merged_tail.next = first_list
        if second_list:
            merged_tail.next = second_list

        return merged_head

#  Find the Nth Node from the End
  
    def find_nth_from_end(self, n):
        current_node = self.head
        node_count = 0

        # Count the total number of nodes in the list
        while current_node:
            node_count += 1
            current_node = current_node.next

        if node_count < n:
            print(f"The list has less than {n} nodes.")
            return

        # Traverse again to the (node_count - n)th node
      
        target_index = node_count - n
        current_node = self.head
        for _ in range(target_index):
            current_node = current_node.next

        print(f"The {n}th node from the end is: {current_node.data}")


# Testing the Linked List Operations
if __name__ == "__main__":
    # Creating two sorted linked lists for merging example
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)

    print("List 1:")
    list1.display()

    print("List 2:")
    list2.display()

    print("\nMerging two sorted lists...")
    merged_head = LinkedList.merge_sorted_lists(list1.head, list2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head
    merged_list.display()

    print("\nOriginal List 1:")
    list1.display()

    print("\nOriginal List 2:")
    list2.display()

    # Finding the middle element
    print("\nFinding the middle element of List 1:")
    list1.find_middle()

    # Finding the nth node from the end
    print("\nFinding the 2nd node from the end in List 1:")
    list1.find_nth_from_end(2)

"""
Output:

List 1:
1 -> 3 -> 5 -> None
List 2:
2 -> 4 -> 6 -> None

Merging two sorted lists...
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

Original List 1:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

Original List 2:
2 -> 3 -> 4 -> 5 -> 6 -> None

Finding the middle element of List 1:
Middle Element: 4

Finding the 2nd node from the end in List 1:
The 2th node from the end is: 2

"""
