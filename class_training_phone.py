#手機型號只有兩種 一隻有三種顏色 另一隻只有藍綠 各代表不同的記憶體容量
#藍色 16GB & 32GB 
#紅色 32GB & 64GB
#綠色 64GB & 128GB

class phone:
    def __init__(self,inputname) :
        self.name = inputname
    def show(self):
        print("The",self.name,"have")
        for i in range(len(self.name)) :
            print(self.name[i].colar)
        print("colars!")

class colar:
    def __init__(self,inputColarname,inputMemorysize) :
        self.colar = inputColarname
        self.memorysize = inputMemorysize
    def colarsize(self):
        print("The",self.colar,"have")
        for i in range(len(self.memorysize)) :
            print(self.memorysize[i],"\n")

iPhones = [None]*2
iPhones[0] = "iPhone87"
iPhones[1] = "iPhone88"
myphone = phone(iPhones[0])
notmyphone = phone(iPhones[1])



colars = [None]*3
colars[0] = colar("Blue",["16GB","32GB"])
colars[1] = colar("Red",["32GB","64GB"])
colars[2] = colar("Green",["64GB","128GB"])

iPhones[0].show()


