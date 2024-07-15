"""Tipos de datos
Python no es un lenguaje tipado
En los lenguajes estricatamente tipados no se puede cambiar el tipo de dato
id devuelve la direccion fisica de la variable
"""

Variable_1 = "Buenas tardes a todos"
print("DIreccion 1:", id(Variable_1))


cadena1 = "Arelineas de Mexico"
print(cadena1)
cadena2 = "son las mejores del mundo"
cadena3 = cadena1 + " " + cadena2
print(cadena3)

print(cadena1,cadena2)

numero = 5.5
nummero1 = 5
print(type(numero + nummero1))

num1 = "23"
num2 = "36"
print("Concatenacion: ", num1 + num2)

conversion = int(num1) + int(num2)
print(conversion)

conversion_1 = int(num2)