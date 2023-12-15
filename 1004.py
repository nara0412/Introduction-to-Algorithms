import matplotlib.pyplot as plt
import numpy as np
import math
def o_n(n):
    x = []
    y = []

    for i in range(n):
        x.append(i)
        y.append(i)
    return x,y

def o_nn(n):
    x = []
    y = []

    for i in range(n):
        x.append(i)
        y.append(i*i)
    return x,y

def o_lg(n):
    x = []
    y = []

    for i in range(n):
        x.append(i)
        y.append(np.log(i))
    return x,y

def o_2n(n):
    x = []
    y = []

    for i in range(n):
        x.append(i)
        y.append(pow(2,i))
    return x,y
plt.axis([0,10000,0,10000])
a,b = o_n(10000)
plt.plot(a,b)
a,b = o_nn(10000)
plt.plot(a,b)
a,b = o_lg(10000)
plt.plot(a,b)
a,b = o_2n(100)
plt.plot(a,b)
plt.show()

