class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class linklist:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head == None:
            self.head = node(data)
        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next
            
            currentNode.next = node(data)
            currentNode.next.prev = currentNode
    
    def traverse(self):
        if self.head == None:
            print("No data") 
        else:
            currentNode = self.head
            while currentNode.next != None:
                print(f'{currentNode.data} -> ',end="")
                currentNode = currentNode.next
            print(f'{currentNode.data} -> END')

    def search(self, data):
        currentNode = self.head
        index = 0
        while currentNode.data != data and currentNode.next != None:
            currentNode = currentNode.next
            index += 1
        if currentNode.data == data:
            return(index)
        else:
            return("-1")
    
    def insert(self, index, data):
        if self.head == None:
            if index == 0:
                self.head = node(data)
            else:
                print("Error")

        else:
            if index == 0:
                currentNode = self.head
                self.head = node(data)
                currentNode.prev = self.head
                self.head.next = currentNode
            else:    
                currentNode = self.head
                tempIndex = 1
                while tempIndex != index and currentNode.next != None:
                    currentNode = currentNode.next
                    tempIndex += 1
                
                if tempIndex == index:
                    if currentNode.next != None:
                        temp = currentNode.next
                        currentNode.next = node(data)
                        currentNode.next.next = temp
                        currentNode.next.prev = currentNode
                        temp.prev = currentNode.next
                    else:
                        currentNode.next = node(data)
                        currentNode.next.prev = currentNode
                else:
                    print("Index Error")

    def delete(self, index):
        if self.head == None:
            print("No data can delete")          
        else:
            currentNode = self.head
            tempIndex = 0
            #temp指標指向index前的節點
            while tempIndex != index and currentNode.next != None:
                currentNode = currentNode.next
                tempIndex += 1

            if tempIndex == index:
                if tempIndex == 0: #要刪除第0筆 判斷節點是否1筆以上
                    if currentNode.next != None:
                        self.head = self.head.next
                        self.head.prev = None
                    else:
                        self.head = None
                #判斷是否刪除最後一筆
                else:
                    if currentNode.next != None:
                        currentNode.prev.next = currentNode.next
                        currentNode.next.prev = currentNode.prev
                    else:
                        currentNode.prev.next = None

                currentNode = self.head
                while currentNode.next != None:
                    print(f'{currentNode.data} -> ',end="")
                    currentNode = currentNode.next
                print(f'{currentNode.data} -> END')
            else:
                print("Wrong Index")

    def update(self, index, data):
        if self.head == None:
            if index == 0:
                self.head = node(data)
            else:
                print("Error")
        else:
            currentNode = self.head
            tempIndex = 0
            while tempIndex != index:
                #判斷index是否超出
                if currentNode.next != None:
                    currentNode = currentNode.next
                    tempIndex += 1
                else:
                    print('Error')
                    break
            if tempIndex == index:
                currentNode.data = data

                currentNode = self.head
                while currentNode.next != None:
                    print(f'{currentNode.data} -> ',end="")
                    currentNode = currentNode.next
                print(f'{currentNode.data} -> END')



l = linklist()
print("--add--")
l.add(9)
l.add(16)
l.add(4)
l.add(1)
l.traverse()

print("--insert 4,10--")
l.insert(4,10)
l.traverse()

print("--search 10--")
print(l.search(10))

print("--delete index(4)--")
l.delete(4)

print("update 2,10")
l.update(2,10)