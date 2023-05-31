import numpy as np
import random as rd

# arreglo = [] esto es una lista (culquier tipo de dato)
arreglo = np.zeros(10) # esto es un arreglo (solo de un mismo tipo de dato "numeros")
#print(arreglo)

for i in range(len(arreglo)):
    arreglo[i] = rd.randint(1,100)
print(arreglo)

arregloDos = arreglo[:].copy()

print("El número mayor del arregloDos :",arregloDos.max())
print("El número menor del arregloDos :",arregloDos.min())
print("la suma de los elementos del arregloDos :",arregloDos.sum())
print("El promedio de sus elementos del arregloDos es: ",arregloDos.mean())
print(arregloDos)