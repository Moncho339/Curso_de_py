### Operadores de identidad ###

## Operador is ##
ciudades1 = ["Barcelona", "Madrid", "Paris"]
ciudades2 = ["Barcelona", "Madrid", "Paris"]
ciudades3 = ciudades1
print(ciudades3 is ciudades1)
print(ciudades2 is ciudades1)


ciudades3.append("Buenos aires")
print(ciudades3)
print(ciudades1)

## Operador is not ##
print(ciudades2 is not ciudades1)
print(ciudades3 is not ciudades1)