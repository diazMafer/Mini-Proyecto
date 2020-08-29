import math
from random import random , uniform
import numpy as np

def integral(x,y):
	return (math.exp(-(x+y)))

#no recuerdo como lo hizo samuel pero creo que no esta bien, en todo caso esta seria la segunda parte que utiliza montecarlo

def MonteCarlo(integral, iteraciones):
    for i in range(iteraciones):
        decision = np.random.uniform(0,1) 
        calcular = 0
        decision1 = np.random.random() + 1
        calcular += calcular + integral(decision1, decision1) 
        calcular = calcular / iteraciones
    return  calcular + decision

print("MonteCarlo:")
print("100: " + str(MonteCarlo(integral, 100)))       
print("10,000: " + str(MonteCarlo(integral, 10000)))    
print("1,000,000: " + str(MonteCarlo(integral, 1000000)))   