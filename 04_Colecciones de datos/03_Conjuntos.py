### Conjuntos ###

c_colores = {'rojo', 'verde', 'azul'}
print(c_colores)

for color in c_colores:
    print(color)

#print(c_colores[0]) Da error

print(len(c_colores))
print(type(c_colores))

c_colores.add("negro")
print(c_colores)
c_colores.remove('negro')
print(c_colores)