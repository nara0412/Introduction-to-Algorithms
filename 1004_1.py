from numpy import arange
import matplotlib.pyplot as plt
import math 

def o_1(n):
    x = []
    y = []
    for i in arange(0,n,0.1):
        x.append(i)
        y.append(1)
    return x,y

def o_n(n):
    x = []
    y = []
    for i in arange(0,n,0.1):
        x.append(i)
        y.append(i)
    return x,y
    
def o_n2(n):
    x = []
    y = []
    for i in arange(0,n,0.1):
        x.append(i)
        y.append(i*i)
    return x,y

def o_n3(n):
    x = []
    y = []
    for i in arange(0,n,0.1):
        x.append(i)
        y.append(i*i*i)
    return x,y

def o_2n(n):
    x = []
    y = []
    for i in arange(0,n,0.1):
        x.append(i)
        y.append(2**i)
    return x,y

def o_lg(n):
    x = []
    y = []
    for i in arange(1,n,0.1):
        x.append(i)
        y.append(math.log2(i))
    return x,y
    
def o_nlgn(n):
    x = []
    y = []
    for i in arange(1,n,0.1):
        x.append(i)
        y.append(i * math.log2(i))
    return x,y

plt.xlim(0,1000)
plt.ylim(0,1000)
plt.xlabel('x')
plt.ylabel('y')

k = 1000
a,b = o_1(k)
plt.plot(a,b,label='O(1)')
a,b = o_n(k)
plt.plot(a,b,label='O(n)')
a,b = o_n2(k)
plt.plot(a,b,label='O(n^2)')
a,b = o_n3(k)
plt.plot(a,b,label='O(n^3)')
a,b = o_2n(k)
plt.plot(a,b,label='O(2^n)')
a,b = o_lg(k)
plt.plot(a,b,label='O(lg n)')
a,b = o_nlgn(k)
plt.plot(a,b,label='O(nlgn)')
plt.legend()
plt.show()
