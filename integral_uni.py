import math # este se usa solo para usar la constante de Euler

# generador de randoms 
def pseudo_random_gen(a, m):
    def recursive_rand(x0, n):
        items = list(range(n))
        items[0] = x0
        for i in range(1,n):
            items[i] = (a * items[i-1]) % m
        return [ i / float(m) for i in items]
    return recursive_rand

pseudo_rand = pseudo_random_gen(m = 2**31 - 1, a =7**5)
# ejecución 1: 100 iteraciones 
random_nums100 = pseudo_rand(x0 = 3, n = 100)

# ejecución 2: 10000 iteraciones 
random_nums10K = pseudo_rand(x0 = 3, n = 10000)
# ejecución 3: 1000000 iteraciones 
random_nums1M = pseudo_rand(x0 = 3, n = 1000000)

# definición de función convertida para integral de 0 a 1
h = lambda x: 2*(math.exp(-((1.0/x) - 1.0)**2.0) / x**2.0)

# se obtiene promedio de todos la función evaluada en todos los valores random para la ejecución 1
result_100 = sum([h(y) for y in random_nums100]) / len(random_nums100)

result_10K = sum([h(y) for y in random_nums10K]) / len(random_nums10K)

result_1M = sum([h(y) for y in random_nums1M]) / len(random_nums1M)

print("Resultado para 100 iteraciones:", result_100)
print("Resultado para 10K iteraciones:", result_10K)
print("Resultado para 1M iteraciones:", result_1M)