### Imprimir variables de cadenas de texto ###

nombre = "Alejandro"
print("Buenos dias " + nombre)
 
# Format

nombre = "Alejandro"
edad = "16"
print("Buenos dias {}, feliz {} cumpleaños".format(nombre,edad))

resultado = 10 / 3
print("El resultado es: {r:1.3f}".format(r=resultado))

# F-Strings

nombre = "Alejandro"
edad = "16"
print(f"Buenos dias {nombre}, feliz {edad} cumpleaños")


