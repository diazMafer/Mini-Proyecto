import random
import sys
import matplotlib.pyplot as plt
from matplotlib import animation


#Declaramos variables
seed = 0.05
it = 100 
generados = [seed]
saltos = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]

def generador1(x):
    xn = (5**5*x)%(2**35-1)
    generados.append(xn%1)

def generador2(x):
    yn = (7**5*x)%(2**31-1)
    generados.append(yn%1)

def histograma(lista, inf, sup):
    cont = 0
    hist = []
    for x in lista:
        if x >= inf and x <= sup:
            cont +=1
            if(cont%100 == 0):
                hist.append("*")
    cont -= 1
    if cont < 0:
        cont = 0
    print(str(inf)+'-'+str(sup)+': '+' '.join(map(str, hist))+" total:" + str(cont))

def genHist1():
    for x in range(it):
        generador1(generados[x])
    
    for x in range(10):
        histograma(generados, saltos[x], saltos[x+1])

def genHist2():
    for x in range(it):
        generador2(generados[x])
    
    for x in range(10):
        histograma(generados, saltos[x], saltos[x+1])

def genHist3():
    for x in range(it):
        generados.append(random.randrange(1))
    
    for x in range(10):
        histograma(generados, saltos[x], saltos[x+1])

for x in range(3):
    if x == 0:
        genHist1()
        genHist2()
        genHist3()
    elif x == 1:
        it = 5000
        genHist1()
        genHist2()
        genHist3()
    else:
        it = 100000
        genHist1()
        genHist2()
        genHist3()

