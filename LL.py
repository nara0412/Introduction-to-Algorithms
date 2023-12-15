class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

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
        index = 1
        while currentNode.data != data and currentNode.next != None:
            currentNode = currentNode.next
            index += 1
        if currentNode.data == data:
            return(index)
        else:
            return("-1")
    
    def insert(self, index, data):
        if self.head == None and index == 1:
            self.head = node(data)
        elif self.head == None and index >= 1:
            print("Error")
        else:
            currentNode = self.head
            tempIndex = 2
            while tempIndex != index:
                currentNode = currentNode.next
                tempIndex += 1
            if tempIndex == index:
                temp = currentNode.next
                currentNode.next = node(data)
                currentNode = currentNode.next
                currentNode.next = temp
                    
    def delete(self, data):
        currentNode = self.head
       
        #節點的資料不等於要刪除的資料(指標往後 temp為前一個節點)
        while currentNode.data != data and currentNode.next != None:
            temp = currentNode
            currentNode = currentNode.next
        #如果刪除資料 用temp銜接到刪除後的下一個節點
        if currentNode.data == data:
            temp.next = currentNode.next
            currentNode = self.head
            while currentNode.next != None:
                print(f'{currentNode.data} -> ',end="")
                currentNode = currentNode.next
            print(f'{currentNode.data} -> END')
        else:
            print("No same data here")

    def update(self, index, data):
        if self.head == None and index == 1:
            self.data = node(data)
        else:
            currentNode = self.head
            tempIndex = 1
            while tempIndex != index:
                #判斷index是否超出全部節點的數量
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

    def Count(self,data):
        currentNode = self.head
        tempCount = 0
        while currentNode != None:
            if currentNode.data == data:
                tempCount += 1
            currentNode = currentNode.next
        return(tempCount)

    def Addsort(self,data):
        #沒有任何節點
        if self.head == None:
            self.head = node(data)
        
        #有節點時
        else:
            currentNode = self.head
            frontNode = None #判斷目前節點的前一筆
            
            #節點有1個以上 且 節點資料比要加入的資料小(指標向後移)
            while currentNode.next != None and currentNode.data < data:
                frontNode = currentNode
                currentNode = currentNode.next                
            
            #當加入的資料前面有節點時
            if currentNode.data >= data and frontNode != None:
                    if currentNode.data >= data:
                        frontNode.next = node(data)
                        frontNode = frontNode.next
                        frontNode.next = currentNode
                    else:
                        currentNode.next = node(data)
            
            #加入的資料前面前面沒有節點
            else:
                #判斷該節點比資料大或小 決定加入的資料要放在節點的右邊或左邊
                if currentNode.data >= data:
                    self.head = node(data)
                    self.head.next = currentNode 
                else:
                    currentNode.next = node(data)

        currentNode = self.head
        while currentNode.next != None:
            print(f'{currentNode.data} -> ',end="")
            currentNode = currentNode.next
        print(f'{currentNode.data} -> END')

#加入Queue的pop    
    # def pop(self):
    #     currentNode = self.head
    #     print(f'pop -> {currentNode.data}')
    #     self.head = currentNode.next
    #     currentNode = self.head
        
    #     if self.head == None:
    #         print("No data") 
    #     else:
    #         currentNode = self.head
    #         while currentNode.next != None:
    #             print(f'{currentNode.data} -> ',end="")
    #             currentNode = currentNode.next
    #         print(f'{currentNode.data} -> END')


if __name__ == '__main__':
    l = linklist()
    print("--add--")
    l.add(10)
    l.traverse()
    l.add(7)
    l.traverse()
    l.add(12)
    l.traverse()

    print("--search--")
    print(l.search(10))

    print("--add--")
    l.add(13)
    l.add(14)
    l.add(15)
    l.add(16)
    l.traverse()
    
    print("--insert--")
    l.insert(3,11)
    l.traverse()
    
    print("--delete--")
    l.delete(12)

    print("--update--")
    l.update(2,11)

    print("--Count--")
    print(f'count 11 = {l.Count(11)}\ncount 20 = {l.Count(20)}')

    a = linklist()
    a.Addsort(8)
    a.Addsort(4)
    a.Addsort(5)
    a.Addsort(1)
    a.Addsort(2)
    a.Addsort(5)
    a.Addsort(10)
