class Tree:
    def __init__(self, data):
        self.data = data
        self.child = []

    def addNode(self,data):
        self.child.append(Tree(data))

def to_Binary_tree(tree):
    childlen  = len(tree.child)
    if childlen > 0:
        to_Binary_tree(tree.child[0])
    if childlen > 1:
        for i in range(childlen):
            if i < childlen - 1:
                if tree.child[i].child == []:
                    tree.child[i].child.append(None)
                tree.child[i].child.append(tree.child[i + 1])
                to_Binary_tree(tree.child[i + 1])
        del tree.child[1:]

def Forest_to_Binary_tree(tree1,tree2):
    tree1.child.append(tree2)
    return tree1

def in_order(tree):
    if tree == None:
        return -1
    childlen = len(tree.child)
    if childlen > 0:
        temp = in_order(tree.child[0])
        if temp != -1:
            print(' -> ',end="")
    print(tree.data,end="")
    if childlen > 1:
        for i in range(1,childlen):
            print(' -> ',end="")
            in_order(tree.child[i])

def pre_order(tree):
    if tree == None:
        return -1
    childlen = len(tree.child)
    print(tree.data,end="")
    if childlen > 0:
        print(' -> ',end="")
        temp = pre_order(tree.child[0])
    if childlen > 1:
        for i in range(1,childlen):
            if temp != -1:
                print(' -> ',end="")
            pre_order(tree.child[i])
            

def post_order(tree):
    if tree == None:
        return -1
    childlen = len(tree.child)
    if childlen > 0:     
        temp = post_order(tree.child[0])
        if temp != -1:
            print(' -> ',end="")
    if childlen > 1:
        for i in range(1,childlen):
            post_order(tree.child[i])
            print(' -> ',end="")
    print(tree.data,end="")

a = Tree('A')
a.addNode('B')
a.addNode('C')
a.addNode('D')
a.child[0].addNode('E')
a.child[1].addNode('F')
a.child[1].addNode('G')
a.child[1].addNode('H')
a.child[2].addNode('I')
a.child[0].child[0].addNode('J')
a.child[0].child[0].addNode('K')
a.child[1].child[0].addNode('L')
a.child[1].child[0].addNode('M')
a.child[1].child[2].addNode('N')

# print(a.child[0].data) #B
# print(a.child[0].child[0].data) #E
# print(a.child[0].child[0].child[0].child[0].data) 

#========== Tree to Binary Tree ==========
print('轉換前\nin-order')
in_order(a)
print('\npre-order')
pre_order(a)
print('\npost-order')
post_order(a)
print()
print('轉換後\nin-order')
to_Binary_tree(a)
in_order(a)
print('\npre-order')
pre_order(a)
print('\npost-order')
post_order(a)

#========== 否ㄖㄨㄧˇ斯特 吐 百內ㄖㄨㄧ ㄔㄨㄧˋ ==========
z = Tree('A')
z.addNode('B')
z.addNode('C')
z.addNode('D')
z.child[0].addNode('E')
z.child[1].addNode('F')
z.child[1].addNode('G')
z.child[1].addNode('H')
z.child[2].addNode('I')
z.child[0].child[0].addNode('J')
z.child[0].child[0].addNode('K')
z.child[1].child[0].addNode('L')
z.child[1].child[0].addNode('M')
z.child[1].child[2].addNode('N')

b = Tree('O')
b.addNode('P')
b.child[0].addNode('Q')
b.child[0].addNode('R')
b.child[0].addNode('S')

c = Tree('T')
c.addNode('U')
c.addNode('V')
c.child[1].addNode('W')

to_Binary_tree(z)
to_Binary_tree(b)
to_Binary_tree(c)
z = Forest_to_Binary_tree(z,b)
z = Forest_to_Binary_tree(z,c)

print()
print('否ㄖㄨㄧˇ斯特 吐 百內ㄖㄨㄧ ㄔㄨㄧˋ')
print('in-order')
in_order(z)
print('\npre-order')
pre_order(z)
print('\npost-order')
post_order(z)