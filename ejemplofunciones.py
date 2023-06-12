import funciones as fn

#llamando a la función
fn.saludo("juan")
nom = input("Ingrese su nombre: ")
fn.saludo(nom)

aActual = 2023
aNac = int(input("Ingrese su año Nacimiento: "))
fn.calcularEdad(aActual,aNac)

print("hola 1")

print("hola 2")

print("Funciones con retorno")
suma = fn.sumar(2,3)
print(suma)
print(fn.sumar(4,6))
print()
areaC = fn.areaCirculo(3)
print(areaC)



