class Node():
    def __init__(self, data):
        self.data = data
        self.child = []

class Linkedlist():
    def __init__(self):
        self.list = []

    def adjacency(self):
        num = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        print(" ",'a b c d e f g h')
        for i in self.list:
            print(i.data,end=" ")
            for j in range(len(num)):
                flag = 0
                for k in i.child:
                    if num[j] == k.data:
                        flag = 1
                print(flag,end=" ")
            print()
    
    def BFS(self):
        queue = [self.list[0]]
        temp = set()
        while queue:
            for i in queue:
                print(i.data,end=" ")
                temp.add(i)
            l = len(queue)
            for i in range(l):
                for j in queue[i].child:
                    if j not in queue and j not in temp:
                        queue.append(j)
            queue = list(set(queue) - temp)
                
if __name__ =='__main__':
    l = Linkedlist()
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    b = [(0,1),(0,2),
         (1,0),(1,2),
         (2,0),(2,1),(2,3),(2,4),(2,5),
         (3,2),(3,5),(3,6),
         (4,2),(4,5),
         (5,2),(5,3),(5,4),(5,6),
         (6,3),(6,5),(6,7),
         (7,6)]
    for i in a:
        l.list.append(Node(i))
    for i in b:
        l.list[i[0]].child.append(l.list[i[1]])
    print('==========adjacency matrix==========')
    l.adjacency()
    print('==========queue進行Breadth-first search==========')
    l.BFS()