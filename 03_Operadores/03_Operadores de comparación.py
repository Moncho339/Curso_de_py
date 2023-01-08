### Operadores de comparación ###
"""
Operadores de comparación

Es igual = ==
Distinto de = !=
Mayor = >
Menor = <
Mayo o igual = >=
Menor o igual = <=
"""
## es igual ##
numero1 = 6
numero2 = 3
print(numero1 == numero2)

cadena1 = "Hola mundo"
cadena2 = "Hola mundo"
print(cadena1 == cadena2)


cadena = "Hola mundo"
if (cadena == "Hola mundo"):
    print("Hello world")

cadena = "Hello"
if (cadena == "Hola mundo"):
    print("Hello world")

## distinto de ##
numero1 = 6
numero2 = 3
print(numero1 != numero2)

cadena = "Hello"
if (cadena != "Hellow"):
    print("Visca el Barca")

cadena = "Hello"
if (cadena != "Hello"):
    print("Visca el Barca")

### Mayor que ###
numero1 = 6
numero2 = 3
print(numero1 > numero2)

## Menor que ##
numero1 = 6
numero2 = 3
print(numero1 < numero2)

## Mayor o igual ##
numero1 = 6
numero2 = 3
print(numero1 >= numero2)

numero1 = 6
numero2 = 6
print(numero1 >= numero2)

numero1 = 3
numero2 = 6
print(numero1 >= numero2)

## Menor o igual ##

numero1 = 3
numero2 = 6
print(numero1 <= numero2)

numero1 = 3
numero2 = 3
print(numero1 <= numero2)

numero1 = 7
numero2 = 6
print(numero1 <= numero2)
