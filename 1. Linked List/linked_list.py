class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data=data)
        # If the linked list is empty
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_head(self, data):
        new_node = Node(data=data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data=data)
        # If the linked list is empty
        if self.head == None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self, key):
        temp = self.head
        # If the head node is to be deleted
        if temp != None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.next != None and temp.next.data == key:
                to_delete = temp.next
                temp.next = to_delete.next
                to_delete = None
                return
            temp = temp.next
        print("Key Not Found")
        return

    def update(self, key, new_data):
        temp = self.head

        # If the head node is to be updated
        if temp.data == key:
            temp.data = new_data
            return

        while temp is not None:
            if temp.next != None and temp.next.data == key:
                to_update = temp.next
                to_update.data = new_data
                return
            temp = temp.next
        print("Key Not Found")
        return

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="-> ")
            temp = temp.next
        print()


def main():
    print("Welcome to Linked List in python")
    flag = True
    llist = LinkedList()
    while flag:
        print("\n\n1. Append")
        print("2. Insert At Head")
        print("3. Insert At End")
        print("4. Delete")
        print("5. Update")
        print("6. Display")
        user_input = input("Select from 1-6 OR Press 0 to exit ")

        if user_input == "0":
            flag = False
            break
        elif user_input == "1":
            new_node = input("Enter your node ")
            llist.append(new_node)
        elif user_input == "2":
            new_node = input("Enter new node: ")
            llist.insert_at_head(new_node)
        elif user_input == "3":
            new_node = input("Enter new node: ")
            llist.insert_at_end(new_node)
        elif user_input == "4":
            key = input("Enter the node to delete: ")
            llist.delete(key)
        elif user_input == "5":
            key = input("Enter the node to update: ")
            new_data = input("Enter the new value: ")
            llist.update(key, new_data=new_data)
        elif user_input == "6":
            llist.display()
        else:
            print("Please select proper option")


if __name__ == "__main__":
    main()
