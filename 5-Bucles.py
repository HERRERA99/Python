# Bucles

numeros = [1, 2, 3, 4, 5]
print(numeros)
print(numeros[2])

# Longitud array
print(len(numeros))

nombres = ["Pepe", "Aitor", "Maria"]

variada = [1, "Taza", True, 1.2]

print(variada)
print(nombres)


# Bucle for

for i in range(10):
    print(i)

for i in range(10, 20):
    print(i)


# ejemplo 1

palabra = "ciclismo"

for letra in palabra:
    if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print(letra)


# ejemplo 2

numeros = [1, 20, 43, 2, 34, 4]
for num in numeros:
    print(num)
    num += 10
    print(num)
print(numeros)
# Se modifica solo dentro del bucle, después esta todo igual 


numeros = [1, 20, 43, 2, 34, 4]
for num in range(len(numeros)):
    numeros[num] += 10
print(numeros)


# Bucle while

contador = 0
while(contador <= 10):
    print(contador)
    contador += 1



# ejemplo 3

frase = "Hola me llamo Aitor y tengo 19 años"
letraEncontrada = False
letra = input("Intorduce la letra a encontrar: ")
i = 0
while(not(letraEncontrada)):
    if(frase[i] == letra):
        print("Encontrada")
        letraEncontrada = True
    elif(i == (len(frase) -1)):
        print("No ha sido encontrada")
        break
    i += 1



############################
#########  Parte 2 #########
############################

# Break para salir de un bucle
# Continue para pasar a la sig iteración
# Pass no hace nada, solo sirve para si quieres hacer una función vacia para estructurar codigo

# Se le puede poner un else al for, y se leeria cuando el for halla acabado, y si hay un break 
# que te saca del bucle, el else no se ejecuta

# Ejemplo 2
from random import randint
from re import L


solucion = randint(0,10)
acabar = False
while(not(acabar)):
    respuesta = input("Introduzca un numero a adivinar entre el 0-10: ")
    if(respuesta.isnumeric()):
        respuesta = int(respuesta)
    else:
        print("Error, no es un número")
        break

    if(respuesta == solucion):
        acabar = True
        print("Enhorabuena¡¡¡!!!")
    elif(respuesta < solucion):
        print("La solución es mayor")
    elif(respuesta > solucion):
        print("La solución es menor") 