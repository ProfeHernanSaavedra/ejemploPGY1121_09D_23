import numpy as np

arreglo = np.array([13,43,12,4,6])
print(arreglo)
print(arreglo.ndim)
largo = len(arreglo)
print(largo)
estruc = arreglo.shape
print(estruc)
intervalo = arreglo[1:3]
print(intervalo)
intervalo2 = arreglo[1:4:2]
print(intervalo2)
intervalo3 = arreglo[::2]
print(intervalo3)
