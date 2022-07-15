# Bucles
"""
numeros = [1, 2, 3, 4, 5]
print(numeros)
print(numeros[2])

# Longitud array
print(len(numeros))

nombres = ["Pepe", "Aitor", "Maria"]

variada = [1, "Taza", True, 1.2]

print(variada)
print(nombres)
"""

# Bucle for
"""
for i in range(10):
    print(i)

for i in range(10, 20):
    print(i)
"""

# ejemplo 1
"""
palabra = "ciclismo"

for letra in palabra:
    if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print(letra)
"""

# ejemplo 2
"""
numeros = [1, 20, 43, 2, 34, 4]
for num in numeros:
    print(num)
    num += 10
    print(num)
print(numeros)
# Se modifica solo dentro del bucle, después esta todo igual 
"""

numeros = [1, 20, 43, 2, 34, 4]
for num in range(len(numeros)):
    numeros[num] += 10
print(numeros)