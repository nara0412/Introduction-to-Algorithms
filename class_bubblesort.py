class bubble_sort:
    def __init__(self,arr):
        self.array = arr
    
    def sort(self):
        n = len(self.array)
        for i in range(n-1):
            for j in range(n-i-1):
                if self.array[j] > self.array[j+1]:
                    storage = self.array[j]
                    self.array[j] = self.array[j+1]
                    self.array[j+1] = storage
        return(self.array)
    
a = [2,5,3,8,9,1,0,4,6,7]
bubble = bubble_sort(a)
print(bubble.sort())