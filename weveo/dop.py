valores = range(21)
random = tuple(valores) 
print(random)
 
numero = input("Introduce un valor que este entre medio de 10 y 20: ")
print(numero)

dato = numero
numero = int(dato)

if numero <= 10:
    print("El numero es menor o igual a 10")
if numero >= 20:
    print("El numero es mayor o igual a 20")
if numero > 10 and numero < 20:
    print("El numero esta entre medio de 10 y 20")