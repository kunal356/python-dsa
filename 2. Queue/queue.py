class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def is_queue_empty(self)->bool:
        return self.front == self.rear == None
    
    def enqueue(self, data):
        new_node = Node(data=data)
        if self.is_queue_empty():               
            self.front = self.rear = new_node
            return
        else:
            self.rear.next = new_node
            self.rear = new_node
        
    def dequeue(self):
        if self.is_queue_empty():
            print("Queue is empty")
            return
        else:
            to_delete = self.front
            self.front = to_delete.next
            if self.front == None:
                self.rear = self.front
            to_delete.next = None

    def display(self):
        curr = self.front
        while curr:
            print(curr.data, end="->")
            curr = curr.next

    def peek(self):
        if not self.is_queue_empty():
            return self.front.data
        else:
            return "Queue is empty"

def main():
    print("Welcome to Queue in python")
    flag = True
    queue = Queue()
    while flag:
        print("\n\n1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        user_input = input("Select from 1-4 OR Press 0 to exit ")

        if user_input == "0":
            flag = False
            break
        elif user_input == "1":
            new_node = input("Enter your node ")
            queue.enqueue(new_node)
        elif user_input == "2":
            queue.dequeue()
        elif user_input == "3":
            print(queue.peek())
        elif user_input == "4":
            queue.display()
        else:
            print("Please select proper option")


if __name__ == "__main__":
    main()

