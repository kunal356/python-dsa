class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isempty(self):
        return self.size == 0

    def append(self, data):
        new_node = Node(data=data)
        if self.isempty():
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
        self.size += 1

    def delete(self, key):
        temp = self.head
        if temp == key:
            self.head = temp.next
            temp.next = None
            self.size -= 1
            return
        while temp.next is not None:
            if temp.data == key:
                next_node = temp.next
                prev_node = temp.prev
                next_node.prev = prev_node
                prev_node.next = next_node
                self.size -= 1
                return
            temp = temp.next
        if temp.data == key:
            prev_node = temp.prev
            prev_node.next = None
            temp.prev = None
            self.size -= 1
            return
        else:
            print("Key not found")
            return

    def insert_at_head(self, data):
        new_node = Node(data=data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data=data)
        if self.isempty():
            self.head = new_node
            self.size += 1
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            self.size += 1

    def insert_after(self, data, key):
        new_node = Node(data=data)

        curr = self.head
        # If key matches with head data
        if curr == key:
            curr.prev = new_node
            new_node.next = curr
            self.head = new_node
            self.size += 1
            return
        while curr.next is not None:
            if curr.data == key:
                next_node = curr.next
                prev_node = curr

                prev_node.next = new_node
                new_node.prev = prev_node

                next_node.prev = new_node
                new_node.next = next_node
                self.size += 1
                return
            curr = curr.next

        # Checking if key matches the last node data
        if curr.data == key:
            curr.next = new_node
            new_node.prev = curr
            self.size += 1
        else:
            print("Key Not Found")

    def update(self, key, new_data):
        curr = self.head
        while curr:
            if curr.data == key:
                curr.data = new_data
                return
            curr = curr.next

    def get_size(self):
        return self.size

    def get_head(self):
        return self.head.data

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end="<->")
            curr = curr.next
        print("None")


def main():
    print("Welcome to Doubly Linked List in python")
    flag = True
    dly_ll = DoublyLinkedList()
    while flag:
        print("\n\n1. Append")
        print("2. Insert At Head")
        print("3. Insert At End")
        print("4. Insert After")
        print("5. Delete")
        print("6. Update")
        print("7. Get Size")
        print("8. Get Head")
        print("9. Display")
        user_input = input("Select from 1-9 OR Press 0 to exit ")

        if user_input == "0":
            flag = False
            break
        elif user_input == "1":
            new_node = input("Enter data for new node: ")
            dly_ll.append(new_node)
        elif user_input == "2":
            new_node = input("Enter data for new node: ")
            dly_ll.insert_at_head(new_node)
        elif user_input == "3":
            new_node = input("Enter data for new node: ")
            dly_ll.insert_at_end(new_node)
        elif user_input == "4":
            new_data = input("Enter data for new node: ")
            key = input("Enter the node key to update after")
            dly_ll.insert_after(data=new_data, key=key)
        elif user_input == "5":
            key = input("Enter the node key to delete: ")
            dly_ll.delete(key=key)
        elif user_input == "6":
            key = input("Enter the node to update: ")
            new_data = input("Enter the new value: ")
            dly_ll.update(key, new_data=new_data)
        elif user_input == "7":
            print(dly_ll.get_size())
        elif user_input == "8":
            print(dly_ll.get_head())
        elif user_input == "9":
            dly_ll.display()
        else:
            print("Please select proper option")
        


if __name__ == "__main__":
    main()
