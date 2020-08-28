from random import choice
from matplotlib import pyplot as plt
from numpy import array

v1 = (0.,0.)
v2 = (1.,0.)
v3 = (0.5, 1.0)

V = [v1, v2, v3]
p0 = (0.5, 0.)
T = [p0]

#Encuentra el punto medio 
def puntoMedio(x, y):
    xf = (x[0]+y[0])/2
    yf =  (x[1]+y[1])/2
    return xf,yf

iters = 1000000

for i in range(iters):
    idx = choice([0,1,2])
    vact = V[idx]
    pact = T[-1]
    psig = puntoMedio(pact,vact)
    T.append(psig)

T = array(T)
plt.scatter(T[:,0], T[:,1], s=0.1)
plt.show()