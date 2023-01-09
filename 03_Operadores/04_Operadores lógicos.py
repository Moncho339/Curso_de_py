### Operadores Lógicos ###

numero1 = 20
numero2 = 10
numero3 = 14
numero4 = 16

## Operador and ##
print(numero1 > numero2)
print(numero3 < numero4)
print(numero1 > numero2 and numero3 < numero4)

print(numero3 > numero4)
print((numero1 > numero2) and (numero3 > numero4))

## Operador or ##
print((numero1 > numero2) and (numero3 > numero4))
print(numero3 > numero4)

## Operador not ##
print(not (numero3 > numero4))