def cut(n):
    if n > 2:
        return(cut(n-1) + n)
    else:
        return(n+2)

a = int(input("輸入整數:"))
print(cut(a))
