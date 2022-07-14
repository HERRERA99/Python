# Funciones 
"""
def saludar():
    print("Hola muy buenas")

saludar()
saludar()
"""

# Funciones con argumento
"""
def saludar2(nombre):
    print("Hola " + nombre)

saludar2("Aitor")
"""

# Funciones con retorno
"""
def suma(numero1, numero2):
    return numero1 + numero2

print(suma(10, 20))

def sonIguales(num1, num2):
    return num1 == num2

print(sonIguales(1,10))
"""

# Funciones con valor por defecto
"""
def saludarPoDefecto(nombre="Aitor"):
    print("Hola " + nombre + " ¿Que tal?")

saludarPoDefecto("PEPE")
saludarPoDefecto()
"""

# Funciones que retornan dos cosas
"""
def sumaYresta(a,b):
    return a+b, a-b

resultado1, resultado2 = sumaYresta(10,20)
print("Los resultados son: \nSuma: " + str(resultado1) + "\nResta: " + str(resultado2))
"""

# Ejercicio 1
"""
def maximo(num1, num2):
    if (num1 > num2):
        return num1
    elif(num2 > num1):
        return num2
    else:
        return False

num1 = input("Introduce el primer num: ")
num2 = input("Introduce el segundo num: ")

if(not(num1.isnumeric()) or not(num2.isnumeric())):
    print("Alguno de los argumentos no es un numero")
else:
    num1 = int(num1)
    num2 = int(num2)
    resultado = maximo(num1,num2)
    if(resultado == False):
        print("Son iguales")
    else:
        print(str(resultado))
"""