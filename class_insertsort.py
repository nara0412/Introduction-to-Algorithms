class insertion_sort:
    def __init__(self,arr):
        self.array = arr
    
    def sort(self):
        n = len(self.array)
        for i in range(n):
            key = self.array[i]
            j = i -1
            while j >= 0 and self.array[j] > key:
                self.array[j+1] = self.array[j]
                j = j - 1
            self.array[j+1] = key
        return(self.array)
    
    def inv(self):
        n = len(self.array)
        for i in range(n):
            key = self.array[i]
            j = i -1
            while j >= 0 and self.array[j] < key:
                self.array[j+1] = self.array[j]
                j = j - 1
            self.array[j+1] = key
        return(self.array)
    
a = [2,5,3,8,9,1,0,4,6,7]
insert = insertion_sort(a)
print(insert.sort())
print(insert.inv())