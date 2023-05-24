import funciones as fn

#llamando a la función
fn.saludo("juan")
nom = input("Ingrese su nombre: ")
fn.saludo(nom)

aActual = 2023
aNac = int(input("Ingrese su año Nacimiento: "))
fn.calcularEdad(aActual,aNac)

print("hola 1")