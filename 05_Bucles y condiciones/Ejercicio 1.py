### Ejercicio 1 ###
frutas = {"manzana":"apple", "naranja":"orange", "platano":"banana", "limon":"lemon"}
print(frutas["naranja"])
frutas["piña"] = "pineapple"
for clave,valor in frutas.items():
    print("{} en ingles es {}".format(clave,valor))