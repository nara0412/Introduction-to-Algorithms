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
            
a = Stack()
b = Stack()
c = Stack()

def hnt(num ,start ,mid ,end):
    # print(num)
    # a.traverse()
    # b.traverse()
    # c.traverse()
    # print("="*16)
    if num == 0:
        return
    hnt(num-1, start, end, mid)
    end.stack_push(start.stack_pop())
    hnt(num-1, mid, start, end)

if __name__ == '__main__':
    a.stack_push(5)
    a.stack_push(4)
    a.stack_push(3)
    a.stack_push(2)
    a.stack_push(1)
    print("-----移動前-----")
    a.traverse()
    b.traverse()
    c.traverse()
    
    hnt(5,a,b,c)
    print("-----移動後-----")
    a.traverse()
    b.traverse()
    c.traverse()
