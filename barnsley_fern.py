import matplotlib.pyplot as plt 
from random import randint 
  
# inicializar lista de coeficientes xn, yn
x = [] 
y = [] 
  
# set primer elemento a 0
x.append(0) 
y.append(0) 
  
nth_it = 0
N = 100000
# P = [0.01, 0.85, 0.07, 0.07]
# functions = {
#     "0.85": {
#         "x": [0.85, -0.04], "y": [0.04, 0.85], "c": [0.0, 1.6]
#     },
#     "0.07a": {
#         "x": [-0.15, 0.26], "y": [0.28, 0.24], "c": [0.0, 0.44]
#     },
#     "0.07b": {
#         "x": [0.2, 0.23], "y": [-0.26, 0.22], "c": [0.0, 1.6]
#     },
#     "0.01": {
#         "x": [0.0, 0.0], "y": [0.0, 0.16], "c": [0.0, 0.0]
#     },
# }

for i in range(1, N): 
  
    # generar numero random entre 1 y 100
    z = randint(1, 100) 
    # rango = 0.0
    # for prob in P:
    #     rango1 = rango+1
    #     rango2 = prob*100 + rango1 -1
    #     if z >= rango1 and z<=rango2:
    #         print("z", z, "rango1", rango1, "rango2", rango2)
    #         # x.append(functions[str(prob)]["x"])
    #         dic_key = str(prob) if prob != 0.7 else "0.07a" if prob == 0.7 and rango2 ==93 else "0.07b"
    #         matrix = np.vstack((
    #             functions[dic_key]["x"],
    #             functions[dic_key]["y"],
    #             functions[dic_key]["c"],
    #         ))
    #         vector = [nth_it, nth_it, nth_it]
    #         res = np.dot(matrix, vector)

    #     rango += prob*100

        
    # para la probabilidad de 0.01
    if z == 1: 
        x.append(0) 
        y.append(0.16*(y[nth_it])) 
      
    # para la probabilidad de 0.85  
    if z>= 2 and z<= 86: 
        x.append(0.85*(x[nth_it]) + 0.04*(y[nth_it])) 
        y.append(-0.04*(x[nth_it]) + 0.85*(y[nth_it])+1.6) 
      
    # para la probabilidad de 0.07a
    if z>= 87 and z<= 93: 
        x.append(-0.15*(x[nth_it]) + 0.28*(y[nth_it])) 
        y.append(0.26*(x[nth_it]) + 0.24*(y[nth_it])+0.44) 
      
    # para la probabilidad de 0.07b 
    if z>= 94 and z<= 100: 
        x.append(0.2*(x[nth_it]) - 0.26*(y[nth_it])) 
        y.append(0.23*(x[nth_it]) + 0.22*(y[nth_it])+1.6) 
          
    nth_it += 1
   
plt.scatter(x, y, s = 0.2, edgecolor ='red') 
  
plt.show() 