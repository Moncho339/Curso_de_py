### Bucle for ###

colores = {"rojo","verde","azul"}
for color in colores:
    print(color)

string = "Hola Mundo"
for caracter in string:
    print(caracter)

range(10)

for numero in range(10):
    print(numero)

for numero in range(10,20):
    print(numero)

for numero in range(3,21,2):
    print(numero)

## Break ##

for numero in range(10):
    if (numero == 5):
        break
    print(numero)

## continue - para parar solo la interaccion actual ##

for numero in range(10):
    if (numero == 6):
        continue
    print(numero)

## for doble ##

for numero1 in range(4):
    for numero2 in range(3):
        print(numero1,numero2)





#Incompleto