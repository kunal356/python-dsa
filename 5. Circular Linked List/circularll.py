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
        curr.next = new_node
        new_node.next = self.head
        self.size += 1
        return

    def peek(self):
        return self.head.data

    def get_size(self):
        return self.size

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

    def display(self):
        print(self.head.data, end="->")
        curr = self.head.next
        while curr != self.head:
            print(curr.data, end="->")
            curr = curr.next


c1 = CircularLinkedList()
c1.append(10)
c1.append(20)
c1.append(30)
c1.append(40)
c1.display()
print("Linked List size is: ", c1.get_size())
print("Head of the Linked List is: ", c1.peek())
