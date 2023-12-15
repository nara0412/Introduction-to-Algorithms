class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head == None:
            print('No data')
        else:
            currentNode = self.head
            while currentNode.next != None:
                print(f'{currentNode.data} -> ',end="")
                currentNode = currentNode.next
            print(f'{currentNode.data} -> END')

    def stack_push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = Node(data)
    
    def stack_pop(self):
        if self.head == None:
            print('No data')
        else:
            prevNode = None
            currentNode = self.head
            while currentNode.next != None:
                prevNode = currentNode
                currentNode = currentNode.next
            
            if currentNode == self.head:
                self.head = None
                return(currentNode.data)
                
            else:
                prevNode.next = None
                return(currentNode.data)
class Queue:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head == None:
            print('No data')
        else:
            currentNode = self.head
            while currentNode.next != None:
                print(f'{currentNode.data} -> ',end="")
                currentNode = currentNode.next
            print(f'{currentNode.data} -> END')

    def enqueue(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = Node(data)
    
    def dequeue(self):
        if self.head == None:
            print('No data')
        elif self.head.next == None:
            currentNode = self.head
            self.head = None
            return(currentNode.data)
        else:
            currentNode = self.head
            self.head = self.head.next
            return(currentNode.data)


if __name__ == '__main__':               
    a = Stack()
    a.stack_push(2)
    a.stack_push(4)
    a.stack_push(6)
    a.traverse()
    print(a.stack_pop())
    a.triverse()
    a.stack_push(8)
    a.traverse()
    print('----------------')
    b = Queue()
    b.enqueue(2)
    b.enqueue(4)
    b.enqueue(6)
    b.traverse()
    print(b.dequeue())
    b.traverse()
    b.enqueue(8)
    b.traverse()