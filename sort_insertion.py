def insertSort(a_list,inver=False):
    n = len(a_list)
    for i in range(2,n):
        key = a_list[i]
        j = i - 1
        if inver == False :
            while j >= 0 and a_list[j] > key:
                a_list[j+1] = a_list[j]
                j -= 1
        else:
            while j >= 0 and a_list[j] < key:
                a_list[j+1] = a_list[j]
                j -= 1
        a_list[j+1] = key
    return(a_list)

a_list = [2,5,3,8,9,1,0,4,6,7]


print(insertSort(a_list))
print(insertSort(a_list,inver=True))