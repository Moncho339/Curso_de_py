### Ejercicio 3 ###

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)
seleccion = input('Introduce un numero que este dentro de la lista: ')
print(seleccion)
dato = seleccion
numero = int(dato)
if (numero in numeros):
    print("El numero que introduciste si esta dentro de la lista")
if (numero not in numeros):
    print("El numero que introduciste no esta dentro de la lista")