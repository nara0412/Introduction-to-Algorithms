class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None
        self.level = 0
    
    def addNode(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.insert(data, self.root)
    
    def insert(self, data, node):
        currentNode = node
        if data <= currentNode.data:
            if currentNode.left == None:
                currentNode.left = Node(data)
            else:
                self.insert(data, currentNode.left)
        else:
            if currentNode.right == None:
                currentNode.right = Node(data) 
            else:
                self.insert(data, currentNode.right)

    def in_order(self):
        if self.root == None:
            print('No data')
        else:
            self.Inorder(self.root)

    def Inorder(self, node):
        currentNode = node
        if currentNode.left != None:
            self.Inorder(currentNode.left)
            print(' -> ',end="")
        print(f'{currentNode.data}',end="")
        if currentNode.right != None:
            print(' -> ',end="")
            self.Inorder(currentNode.right)
        return
            
    def pre_order(self):
        if self.root == None:
            print('No data')
        else:
            self.Preorder(self.root)

    def Preorder(self, node):
        currentNode = node
        print(f'{currentNode.data}',end="")
        if currentNode.left != None:
            print(' -> ',end="")
            self.Preorder(currentNode.left)
        if currentNode.right != None:
            print(' -> ',end="")
            self.Preorder(currentNode.right)
        return

    def post_order(self):
        if self.root == None:
            print('No data')
        else:
            self.Postorder(self.root)
    def Postorder(self, node):
        currentNode = node
        if currentNode.left != None:
            self.Postorder(currentNode.left)
            print(' -> ',end="")
        if currentNode.right != None:
            self.Postorder(currentNode.right)
            print(' -> ',end="")
        print(f'{currentNode.data}',end="")
        return
    
    def findLevel(self, data):
        if self.root == data:
            print('Level = 0')
        else:
            self.find(data, self.root)
    
    def find(self, data, node):
        currentNode = node
        if data < currentNode.data:
            self.level += 1
            self.find(data, currentNode.left)
        elif data > currentNode.data:
            self.level += 1
            self.find(data, currentNode.right)
        else:
            print(self.level)

if __name__ == '__main__':
    a = tree()
    b = [11,6,13,5,9,31,3,7,29,1,4]
    for i in b:
        a.addNode(i)
    a.in_order()
    print('\n'+'='*15)
    a.pre_order()
    print('\n'+'='*15)
    a.post_order()
    print('\n'+'='*15)
    a.findLevel(1)
    
    # test = [12,6,20,10,15,24,7,11,21,8,22]
    # t = tree()
    # for i in test:
    #     t.addNode(i)
    # t.post_order()