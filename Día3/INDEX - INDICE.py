#NOTA: PARA SABER
#EJEMPLO:
#Se puede colocar la palabra que se quiera buscar y te va a mencionar desde donde comienza esa misma palabra
Mi_variable = "Hola mundo"
#              0123456789
indice = Mi_variable.index("mundo")
print(indice)
#Se puede colocar el numero a buscar en el indice y te mostrara a que letra representa o la cual este en esa posicion
Mi_variable = "Hola mundo"
#              0123456789
indice = Mi_variable [2]
print(indice)
#Se puede buscar mendiante solo una letra y te dira en que posicion esta colocada
Mi_variable = "Hola mundo"
#              0123456789
print(Mi_variable.index('m'))

#R-INDEX - busca de deracha a izquierda


print("Práctica Método Index 1")
# Te ayuda a saber en que indice se encuentra, busca
palabra = "ordenador"
#          012345678
resultado = palabra[4]
print(resultado)

print("Práctica Método Index 2")
#Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.index("práctica")
print(resultado)

#NUEVA SOLUCION
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))


print("Práctica Método Index 3")
#Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:

"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
 #       0123456789012345678901234567890123456789012345678901234567890123456789012345
resultado = frase.rindex("práctica")
print(resultado)


frase = "hola"
palabras = frase.rindex()