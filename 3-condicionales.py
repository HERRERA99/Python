# Entrada de datos

edad = input("Por favor introduce la edad: ")
tipoDeDato = type(edad)
print(edad)
print(tipoDeDato)


# Boolean e if

verdadero = True
falso = False

if(verdadero == True):
    print("Soy verdadero")

if(falso != True):
    print("No soy verdadero")

if(falso == True):
    print("Soy verdadero")

# Comparación, elif, else, and, or , not

edad = input("Por favor introduce tu edad: ")
RespuestaPaseVip = input("¿Tienes pase vip?(S/N): ")
if(RespuestaPaseVip == "S"):
    paseVip = True
else:
    paseVip = False

edad = int(edad)
if(edad >= 18 and paseVip == True):
    print("Puedes entrar")
elif(edad <= 0 or edad >= 100):
    print("Eso es imposible")
else:
    print("No puedes entrar")



# Ejercicio practica

print("Por favor introduce un numero: ")
numero = input()
if(not(numero.isnumeric())):
    print("No es un numero")
else:
    numero = int(numero)
    if((numero%2) == 0):
        print("Es par")
    else:
        print("No es par")

