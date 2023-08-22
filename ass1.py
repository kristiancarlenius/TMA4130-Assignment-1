import numpy as np
def L(x, p):
    return ((x-p[0])*(x-p[2]))/((p[1]-p[0])*(p[1]-p[2]))
x = np.linspace(0.5, 3.5, 51)
y = L(x, [1, 2, 3])
print(y)

#c)
import matplotlib.pyplot as pl
pl.plot(x, y)
pl.show()
pl.clf()

def L0(x, p):
    return ((x-p[1])*(x-p[2]))/((p[0]-p[1])*(p[0]-p[2]))
x = np.linspace(0.5, 3.5, 51)
y = L0(x, [1, 2, 3])
print(y)
pl.plot(x, y)
pl.show()
pl.clf()

def L2(x, p):
    return ((x-p[0])*(x-p[1]))/((p[2]-p[0])*(p[2]-p[1]))
x = np.linspace(0.5, 3.5, 51)
y = L2(x, [1, 2, 3])
print(y)
pl.plot(x, y)
pl.show()
pl.clf()