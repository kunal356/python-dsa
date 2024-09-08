class Stack:
    def __init__(self) -> None:
        self.stack = []

    def isempty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def peek(self):
        if not self.isempty():
            return self.stack[-1]

    def display(self):
        print(self.stack)


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
            print(stack.peek())
        elif user_input == "4":
            stack.display()
        else:
            print("Please select proper option")


if __name__ == "__main__":
    main()
