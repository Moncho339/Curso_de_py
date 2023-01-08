### Variables ###

# Una variable siempre tiene que empezar por una letra o por un guion bajo
mensaje = "Hola Mundo"
#20mensajes = "Hello World"
print(mensaje)
#print(20mensajes)

# Las variables tambien son sensibles a las MAYUSCULA y minusculas
Ciudad = "Barcelona"
ciudad = "Madrid"

print(Ciudad)
print(ciudad)


# Las variables tambien se pueden unir en solo una variable
cadena1 = "Visca "
cadena2 = "el "
cadena3 = "Barca"
cadena_unida = cadena1 + cadena2 + cadena3
print(cadena_unida)

# Si lo haces con numeros entero o decimales, lo que va hacer es sumarlas ya que no son una string
numero1 = 5
numero2 = 5
resultado = numero1 + numero2
print(resultado)

# Tambien existe una funicion para ver el tipo de una variable
numero01 = 89
type(numero01)
print(type(numero01))

'''
NUMEROS      Tipo         sintaxis

integer      int          1
float        float        3.6
complex      complex      -5j


BOOLEANOS

boolean      bool         True, False

SECUENCIAS

strings      str         'Texto' o "Texto"
list         list         [1, 2, 3]
tuplas       tuple        (1, 2, 3)

SETS

set          set          {1, 2, 3}

DICCIONARIOS

dictionary   dict         {1:'1' , 2:'2'}
'''