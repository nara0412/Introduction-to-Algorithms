def main(arr):
    left_index = 0
    right_index = len(arr) - 1

    quick_sort(arr,left_index,right_index)
    return(arr)

def quick_sort(arr,l,r):
   if l < r:
        pivot_index = partition(arr,l,r)
        quick_sort(arr,l,pivot_index - 1)
        quick_sort(arr,pivot_index + 1 , r)

def partition(arr,l,r):
    pivot = arr[r]
    i = l - 1
    for j in range(l,r):
        if arr[j] < pivot :
            i = i + 1
            arr[i] , arr[j] = arr[j] , arr[i]
   
    # print(f'i={i},j={j},arr[i]={arr[i]},arr[r]={arr[r]}')
    # print(f'arr={arr}')
    arr[i + 1] , arr[r] = arr[r] , arr[i + 1]
    # print(f'switch={arr}\n')
    return i + 1

if __name__ == '__main__':
    a = [1,9,6,8,5,3,0,7,4,2]
    print(main(a))