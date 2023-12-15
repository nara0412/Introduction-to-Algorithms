class Stack(object):
    def __init__(self, data):
        self.data = list(data)
        self.stack = []
        self.ans = []
    
    def post(self):
        x = ('+','-','*','/','(')
        for i in self.data:
            if i in x:
                self.stack.append(i)
            elif i == ')':
                j = self.stack.pop()
                while j != '(':
                    self.ans.append(j)
                    j = self.stack.pop()
                if '(' not in self.stack:
                    while self.stack != []:
                        self.ans.append(self.stack.pop())
            else:
                self.ans.append(i)
            #print(self.ans)
            #print(self.stack)


if __name__ == '__main__':
    a = Stack('3*((7+1)/4)+(17-5)')
    b = Stack('8/2*3+(8-(16*18))')
    c = Stack('5+(8/2)-(8*(20+(2-1)*8))')
    a.post()
    b.post()
    c.post()
    print(a.ans)
    print(b.ans)
    print(c.ans)
    