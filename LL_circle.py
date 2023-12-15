class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class linklist:
    def __init__(self):
        self.head = None
        self.back = None

    def add(self, data):
        if self.head == None:
            self.head = node(data)
            self.head.next = self.head
            self.head.prev = self.head
        else:
            currentNode = self.head
            while currentNode.next != self.head:
                currentNode = currentNode.next
            
            self.back = node(data)
            currentNode.next = self.back
            self.back.prev = currentNode.next
            self.head.prev = self.back
            self.back.next = self.head
            
    
    def traverse(self):
        if self.head == None:
            print("No data") 
        else:
            currentNode = self.head
            while currentNode.next != self.head:
                print(f'{currentNode.data} -> ',end="")
                currentNode = currentNode.next
            print(f'{self.back.data} -> END')
            print(self.back.next.data)
            print(self.head.prev.data)

    def search(self, data):
        currentNode = self.head
        index = 0
        while currentNode.data != data and currentNode.next != self.head:
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
                self.head.next = self.head
                self.head.prev = self.head
            else:
                print("Error")
        else:
            if index == 0: #插入第0個 判斷所有節點有幾個
                if self.head.next == self.head:
                    self.back = self.head
                    self.head = node(data)
                    self.head.next = self.back
                    self.head.prev = self.back
                    self.back.next = self.head
                    self.back.prev = self.head
                else:    
                    currentNode = self.head
                    self.head = node(data)
                    currentNode.prev = self.head
                    self.back.next = self.head
                    self.head.next = currentNode
                    self.head.prev = self.back
            else:
                currentNode = self.head
                tempIndex = 1
                while tempIndex != index:
                    currentNode = currentNode.next
                    tempIndex += 1
                
                #currentNode指向tempIndex前一個節點
                if tempIndex == index:
                    if currentNode == self.back: #若currentNode是最後一個
                        currentNode = self.back
                        self.back = node(data)
                        currentNode.next = self.back
                        self.back.prev = currentNode
                        self.back.next = self.head
                        self.head.prev = self.back
                    else:    
                        temp = currentNode.next
                        currentNode.next = node(data)
                        currentNode.next.next = temp
                        currentNode.next.prev = currentNode
                        temp.prev = currentNode.next
                else:
                    print("Index Error")

    def delete(self, index):
        if self.head == None:
            print("No data can delete")
        else:
            currentNode = self.head
            tempIndex = 0
            #temp指標指向index前的節點
            while tempIndex != index and currentNode != self.back:
                currentNode = currentNode.next
                tempIndex += 1
            #cu=4 tempIndex=2
            if tempIndex == index:
                if tempIndex == 0:  #要刪除第0筆 判斷節點是否1筆以上
                    if currentNode.next != self.head:
                        self.head = self.head.next
                        self.head.prev = self.back
                        self.back.next = self.head
                    else:
                        self.head = None
                #判斷是否刪除最後一筆
                else:
                    if currentNode != self.back:
                        currentNode.prev.next = currentNode.next
                        currentNode.next.prev = currentNode.prev
                    else:
                        self.back = self.back.prev
                        self.back.next = self.head
                        self.head.prev = self.back

                currentNode = self.head
                while currentNode.next != self.head:
                    print(f'{currentNode.data} -> ',end="")
                    currentNode = currentNode.next
                print(f'{currentNode.data} -> END')
            else:
                print("Wrong Index")

    def update(self, index, data):
        if self.head == None:
            if index == 0:
                self.head = node(data)
                self.head.next = self.head
                self.head.prev = self.head
            else:
                print("Error")
        else:
            currentNode = self.head
            tempIndex = 0
            while tempIndex != index:
                #判斷index是否超出
                if currentNode.next != self.head:
                    currentNode = currentNode.next
                    tempIndex += 1
                else:
                    print('Index Overflow')
                    break
            if tempIndex == index:
                currentNode.data = data

                currentNode = self.head
                while currentNode.next != self.head:
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

print("--search 9--")
print(l.search(9))

print("--delete 0--")
l.delete(0)

print("update 3,9")
l.update(3,9)
