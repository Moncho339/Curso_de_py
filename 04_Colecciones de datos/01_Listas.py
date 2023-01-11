### Listas ###

colores = ["rojo", "amarillo", "verde"]
print(colores)

colores[0] = "rosado"
print(colores)
print(len(colores))
print(type(colores))

colores.append("azul")
print(colores)
print(colores[3])
colores.remove("amarillo")
print(colores)

for color in colores:
    print(color)

colores.clear()
print(colores)