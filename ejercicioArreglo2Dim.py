import random as rd
import numpy as np

arreglo = np.zeros((3,3))

for f in range(3):
    for c in range(3):
        arreglo[f][c] = rd.randint(0,100)

print(arreglo)

print("El promedio de sus elementos es: ",arreglo.mean())
print("La suma de sus elementos es: ",arreglo.sum())
print("El número mayor del arreglo es : ",arreglo.max())
print("El número menor del arreglo es : ",arreglo.min())
print("los elementos de la diagonal es: ", arreglo.diagonal())

arregloDos = np.diag([1,2,3])
print(arregloDos)

print(type(arreglo))