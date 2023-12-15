# def Shell(list):
#     l = len(list)
#     inter = l // 2
#     while inter > 0:
#         for i in range(inter, l):
#             temp = list[i]
#             j = i
#             while j >= inter and list[j-inter] > temp:
#                 list[j] = list[j - inter]
#                 list[j - inter] = temp
#                 j -= inter
#         inter //= 2
#     return list
# a = [8,15,6,81,48,5,54,89,11]
# b = Shell(a)
# print(b)

def Quick(list):
    if list != []:
        k = len(list) - 1
        list, pivot_index = partition(list, 1, k)
        list[:pivot_index] = Quick(list[:pivot_index])
        list[pivot_index + 1:] = Quick(list[pivot_index + 1:])
    return list

def partition(list, i, j):
    pivot = list[0]
    while i < j:
        if list[i] > pivot:
            while j > i:
                if list[j] < pivot:
                    list[i], list[j] = list[j], list[i]
                    j -= 1
                    break
                j -= 1
        i += 1
    while list[j] > pivot:
        j -= 1
    list[0], list[j] = list[j], list[0]
    pivot = j
    return list,pivot
a = [33,31,4,8,12,17,51,42,3,9]
b = Quick(a)
print(b)