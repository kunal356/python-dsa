# Stack Using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
        else:
            temp = self.top
            self.top = new_node
            self.top.next = temp

    def isempty(self):
        return self.top == None

    def pop(self):
        if not self.isempty():
            temp = self.top
            self.top = temp.next
            temp.next = None
        else:
            print("Stack is empty")

    def peek(self):
        if not self.isempty():
            return self.top.data
        else:
            return None

    def display(self):
        if self.isempty():
            print("Stack is empty")
            return
        curr = self.top
        while curr:
            print(curr.data, end="->")
            curr = curr.next
        print("Null")


def main():
    print("Welcome to Queue in python")
    flag = True
    stack = Stack()
    while flag:
        print("\n\n1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        user_input = input("Select from 1-4 OR Press 0 to exit ")

        if user_input == "0":
            flag = False
            break
        elif user_input == "1":
            new_node = input("Enter your node ")
            stack.push(new_node)
        elif user_input == "2":
            stack.pop()
        elif user_input == "3":
            if result:=stack.peek():
                print(result)
            else:
                print("Stack is empty")
        elif user_input == "4":
            stack.display()
        else:
            print("Please select proper option")


if __name__ == "__main__":
    main()
