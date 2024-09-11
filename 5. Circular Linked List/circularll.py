class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def append(self, data):
        new_node = Node(data=data)
        if self.is_empty():
            self.head = new_node
            new_node.next = new_node
            self.size += 1
            return
        curr = self.head.next
        while curr.next != self.head:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1
        return

    def peek(self):
        if self.is_empty():
            return
        return self.head.data

    def get_size(self):
        return self.size

    def get_head(self):
        if self.is_empty():
            return
        return self.head.data

    def insert_at_head(self, data):
        new_node = Node(data=data)
        if self.is_empty():
            self.head = new_node
            new_node.next = new_node
            self.size += 1
            return
        curr = self.head.next
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return

    def insert_at_position(self, data, position):
        if position < 0:
            return
        elif position == 0:
            self.insert_at_head(data=data)
            return
        new_node = Node(data=data)
        curr = self.head
        prev = None
        count = 0
        while count < position-1:
            prev = curr
            curr = curr.next
            if curr == self.head:
                break
            count += 1
        prev.next = new_node
        new_node.next = curr
        self.size += 1

    def delete(self, key):
        if self.is_empty():
            print("Circular Linked List is already empty!")
            return
        curr = self.head
        if self.head.data == key:
            while curr.next != self.head:
                curr = curr.next
            self.head = self.head.next
            curr.next = self.head
            if self.size == 1:
                self.head = None
            self.size -= 1
            return
        prev = None
        while curr.next != self.head:
            prev = curr
            curr = curr.next
            if curr.data == key:
                prev.next = curr.next
                curr.next = None
                self.size -= 1
                return
        print("Data not found")
        return

    def update(self, key, new_data):
        if self.is_empty():
            print("Circular Linked List is already empty!")
            return
        curr = self.head
        if self.head.data == key:
            self.head.data = new_data
            return
        while curr.next != self.head:
            curr = curr.next
            if curr.data == key:
                curr.data = new_data
                return
        print("Data not found")
        return

    def display(self):
        if self.is_empty():
            print("Circular Linked List is empty. Append some data to view it.")
            return
        print(self.head.data, end="->")
        curr = self.head.next
        while curr != self.head:
            print(curr.data, end="->")
            curr = curr.next


def main():
    print("Welcome to Circular Linked List in python")
    flag = True
    cir_ll = CircularLinkedList()
    while flag:
        print("\n1. Append")
        print("2. Insert At Head")
        print("3. Insert At position")
        print("4. Delete")
        print("5. Update")
        print("6. Get Size")
        print("7. Get Head")
        print("8. Display")
        user_input = input("Select from 1-8 OR Press 0 to exit ")

        if user_input == "0":
            flag = False
            break
        elif user_input == "1":
            new_node = input("Enter data for new node: ")
            cir_ll.append(new_node)
        elif user_input == "2":
            new_node = input("Enter data for new node: ")
            cir_ll.insert_at_head(new_node)
        elif user_input == "3":
            new_data = input("Enter data for new node: ")
            position = input("Enter the position to insert at")
            cir_ll.insert_at_position(data=new_data, position=position)
        elif user_input == "4":
            key = input("Enter the node key to delete: ")
            cir_ll.delete(key=key)
        elif user_input == "5":
            key = input("Enter the node to update: ")
            new_data = input("Enter the new value: ")
            cir_ll.update(key=key, new_data=new_data)
        elif user_input == "6":
            print("\nThe size of the Circular linked List is:", cir_ll.get_size())
        elif user_input == "7":
            print("\nThe head of the Circular Linked List is:", cir_ll.get_head())
        elif user_input == "8":
            cir_ll.display()
        else:
            print("Please select proper option")


if __name__ == "__main__":
    main()
