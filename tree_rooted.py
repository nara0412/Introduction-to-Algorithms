class Node:
    def __init__(self ,data = None):
        self.data = data
        self.left = None
        self.right = None
    def add_left(self,data):
        if self.left == None:
            self.left = Node(data)
        else:
            self.left.add_left(data)
    def add_right(self,data):
        if self.right == None:
             self.right = Node(data)
        else:
            self.right.add_right(data)

def traverse(tree, parent=None):
    if tree != None:
        print("data:", tree.data)
        if parent != None:
            print("parent:", parent.data)
        else:
            print("parent: None")
        if tree.left != None:
            print("left:", tree.left.data)
        else:
            print("left: None")
        if tree.right != None:
            print("right:", tree.right.data)
        else:
            print("right: None")
        print("========================")
        
        traverse(tree.left, parent=tree)
        traverse(tree.right, parent=tree)



tree = Node(12)
tree.add_left(13)
tree.add_left(6)
tree.left.add_right(7)
tree.add_right(14)
tree.right.add_left(16)
tree.right.left.add_left(11)
tree.right.left.add_right(13)

traverse(tree)

