#SUB-STRING - Slici
texto = "ABCDEFGHIJKLM"
#        0123456789++
fragmento = texto[2:8]
#El primer dato dentro de los corchetes es desde que posicion nos mostrara y el segundo dato es para saber hasta donde mostrara
#En caso de que en el segundo corchete no se agrega algun numero se mostrara desde donde empieza y hasta donde termina sin tener un parametro en donde detenerse
#Se puede agregar un tercer factor en el cual depende de el dato ingresado sea una letra o un numero seran cada cuantos caracteres ira saltando
print(fragmento)

print("Práctica Sub-Strings 1")
#Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
#"Controlar la complejidad es la esencia de la programación"
#Pista: "Controlar" tiene un largo de 9 caracteres.

frase = "Controlar la complejidad es la esencia de la programación"
print(frase[0:9])


print("Práctica Sub-Strings 2")
#Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
#"Nunca confíes en un ordenador que no puedas lanzar por una ventana"

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
texto = frase[8]
print(texto)


print("Práctica Sub-Strings 3")
#Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
#"Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza\n"
texto = frase[::-1]
print(texto)

texto = "Este es el texto de Moises"
prueba = texto.upper()
print(prueba)
print(type(prueba))
