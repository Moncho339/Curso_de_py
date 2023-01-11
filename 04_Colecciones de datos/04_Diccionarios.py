### Diccionarios ###

d_colores = {'red':'rojo', 'blue':'azul', 'yellow':'amarillo'}
print(d_colores)
print(d_colores['yellow'])
print(d_colores['red'])
valor = d_colores['yellow']
print(valor)

d_colores['nigger'] = 'negro'
print(d_colores['nigger'])
print(d_colores)

d_colores.pop('yellow')
print(d_colores)

del(d_colores['red'])
print(d_colores)

for color in d_colores:
    print(color)

for clave,valor in d_colores.items():
    print(clave,valor)

print(len(d_colores))
print(type(d_colores))