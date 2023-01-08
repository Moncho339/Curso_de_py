### Cadenas de texto ###

string = "Hola Mundo"
print(string)
""""
H o l a   M u n d o
0 1 2 3 4 5 6 7 8 9

esta es la numeracion que tiene de dentro de string
y en el recorrido inverso, no se empieza con 0, si no que con -1
"""
print(string[1])
print(string[2])
print(string[3])

print(string[-1])
print(string[-2])
print(string[-3])

print(string[0:5])
#el primer numero es donde empieza, y el segundo es donde termina. pero al segundo numero restale 1 de posicion

print(string[1:])
#este va recoger los caractares desde la posicion 1 en adelante
'''
string[1] = 'w'
print(string)

Las strings son inmutables
'''
string = "Hola"
other_string = "Mundo"
space = " "
superstr = string + space + other_string
print(superstr)