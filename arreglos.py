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
intervalo4 = arreglo[2::1]
print(intervalo4)
print(arreglo[-2])

for i in range(len(arreglo)):
    print("arreglo [",i,"] = ",arreglo[i])


arreglo2 = [ i for i in range(0,5)]
print(arreglo2)

#copia de arreglos
print("\nCOPIA DE ARREGLOS")
arreglo3 = np.array([1,2,3])
arreglo4 = arreglo3[:] # esta linea "clono" el arreglo3 ...NO COPIO
print(arreglo4)
arreglo4[0] = 100
print(arreglo4)
print(arreglo3)

#ahora vamos a copiar
print("\nAhora si")
arreglo3 = np.array([1,2,3])
arreglo4 = arreglo3[:].copy() # ahora si copio
print(arreglo4)
arreglo4[0] = 100
print(arreglo4)
print(arreglo3)
suma = arreglo3.sum()
print(suma)




