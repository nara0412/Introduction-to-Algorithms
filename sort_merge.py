class m:
    def merge(self,l_arr,r_arr):
        sort_array = []
        i = j = 0
        l = len(l_arr)
        r = len(r_arr)

        while i < l and j < r:
            if l_arr[i] <= r_arr[j]:
                sort_array.append(l_arr[i])
                i += 1
            else:
                sort_array.append(r_arr[j])
                j += 1
        while i < l:
            sort_array.append(l_arr[i])
            i += 1
        while j < r:
            sort_array.append(r_arr[j])
            j += 1
        return sort_array
    
    def invert(self,l_arr,r_arr):
        sort_array = []
        i = j = 0
        l = len(l_arr)
        r = len(r_arr)

        while i < l and j < r:
            if l_arr[i] >= r_arr[j]:
                sort_array.append(l_arr[i])
                i += 1
            else:
                sort_array.append(r_arr[j])
                j += 1
        while i < l:
            sort_array.append(l_arr[i])
            i += 1
        while j < r:
            sort_array.append(r_arr[j])
            j += 1
        return sort_array

    def merge_sort(self,arr,invert=False):
    
        if len(arr) < 2:
            return arr
        q = len(arr) // 2
        left_array = arr[:q]
        right_array = arr[q:]

        if invert == False:
            l = self.merge_sort(left_array)
            r = self.merge_sort(right_array)
            return self.merge( l , r )
        else:
            l = self.merge_sort(left_array,invert=True)
            r = self.merge_sort(right_array,invert=True)
            return self.invert(l , r)

if __name__ == '__main__':
    a = [0,9,5,6,8,7,3,4,2,1]
    b = m()
    print(b.merge_sort(a))
    print(b.merge_sort(a,invert=True))