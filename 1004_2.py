class array:
    def __init__(self,list):
        self.list = list
    def traverse(self):
        for i in range(len(self.list)):
            print(f'[ {i} ]: {self.list[i]}')
            i+=1

    def insert(self,index,num):
        l = len(self.list) + 1
        temp = [0]*l
        j = 0
        for i in range(l-1):

            if i == index:
                temp[j] = num
                j = j + 1
            temp[j] = self.list[i]
            j += 1      
        self.list = temp
        print(self.list)

    def remove(self,index):
        l = len(self.list) - 1
        temp = [0]*l
        j = 0
        for i in range(l):
            if i != index:
                temp[i] = self.list[j]
            else:
                j += 1
                temp[i] = self.list[j]
            j += 1
        self.list = temp
        print(self.list)
    
    def update(self,index,num):
        self.list[index] = num
        print(self.list)

    def search(self,num):
        temp = -1
        l = len(self.list)
        for i in range(l):
            if self.list[i] == num:
                temp = i
        print(f'index: {temp}')

a = [1,2,3,4,5]
test = array(a)
print('Traverse:')
test.traverse()
print('Insertion:')
test.insert(1,2)
print('Deletion:')
test.remove(2)
print('Update:')
test.update(3,8)
print('Search:')
test.search(8)
test.search(10)