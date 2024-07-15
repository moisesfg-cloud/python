"INDICE - INDEX"
# De esta manera se buscan los valores con un integer
frase = "La gelatina es de fresa"
buscar = frase[3]
print(buscar)

# De esta manera se buscan los valores como string - TE INDICA DESDE QUE NUMERO COMIENZA EL VALOR A BUSCAR
frase = "La gelatina es de fresa"
buscar = frase.index("fresa")
print(buscar)

# Strings y substrings

frase = "La gelatina es de fresa"
buscar = frase.index("e",5)
print(buscar)

# rindex busca de derecha a izquierda
frase = "La gelatina es de fresa"
buscar = frase.rindex("e",5)
print(buscar)

"EXTRAER O FRAGMENTAR"
# Aqui vamos a extraer un valor dependiendo su posicion
texto = 'ABCDEFGHIJKLM'
fragmento = texto[2]
print(fragmento)

# CON ESTO VAMOS A INDICAR DESDE QUE POSICION HASTA QUE POSICION VA A EXTRAER VALORES
texto = 'ABCDEFGHIJKLM'
fragmento = texto[2:6]
print(fragmento)


texto = 'ABCDEFGHIJKLM'
fragmento = texto[2:8:2] # CON ESTE ULTIMO FACTOR LE INDICAMOS CADA CUANTOS VALORES VA A IR EXTRAYENDO
print(fragmento)

texto = 'ABCDEFGHIJKLM'
fragmento = texto[::1] # DE ESTA MANERA LE INDICAMOS QUE EXTRAIGA TODOS LOS ELEMENTOS SALTANDO UNO POR CADA EXTRACCION
print(fragmento)

texto = 'ABCDEFGHIJKLM'
fragmento = texto[::-1] # DE ESTA MANERA LE INDICAMOS QUE EXTRAIGA TODOS LOS DATOS COMENZANDO DE DERECHA A IZQUIERDA
print(fragmento)

# EJERCICIOS

texto = "Doce horas más tarde estaba en casa, en cama. La habitación estaba a oscuras."
extraer = texto[0:20]
extraer2 = texto[45:75]
print(extraer + " - " + extraer2)

texto = "Sook, sentada a mi lado, se balanceaba en una mecedora; un sonido tan sedante como el de las olas en el océano"
extraer = texto[::-1]
print(extraer)

texto = "En 1928, a los nueve años, yo formaba parte, con todo el espíritu de cuerpo posible, de una organización conocida como el Club de los Comanches."
extraer = texto [::3]
print(extraer)
# ·······················································································································

"METODOS STRING"
# ·······················································································································

"UPPER"
# CON ESTE METODO PODEMOS PASAR UN TEXTO A MATUSCULAS
texto = "Este es el texto de Federico"
resultado = texto.upper()
print(resultado)
# ·······················································································································
"LOWER"
# CON ESTE METODO PODEMOS PASAR UN TEXTO A MINUSCULAS
texto = "Este es el texto de Federico"
resultado = texto.lower()
print(resultado)
# ·······················································································································
# "SPLIT" #ESTE METODO TOMA COMO SEPARADOR AL VALOR QUE DESEAS
texto = "Este es el texto de Moises"

resultado = texto.split("t")

print(resultado)

texto = "caguate pistache caguate psitache a cuanto la bolsa caguate pistache"

resultado = texto.split("caguate")

print(resultado)
# ·······················································································································
"JOIN" # JOIN ES UN METODO EL CUAL NOS AYUDA A UNIR

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

a ="Mi nombre es"
b ="Moises"
c ="Feria"
d ="Garcia"
e = " ".join([a,b,c,d])

print(e)
# ·······················································································································
"FIND" # BUSCA UN DETERMINADO CARACTER DENTRO DEL STRING - CUANDO EL METODO NO ENCUENTRE EL CARACRTER EL RESULTADO SIEMPRE SERA -1

texto = "Este es el texto de Moises"

resultado = texto.find("M")

print(resultado)
# ·······················································································································
"REPALCE" # SIRVE PARA TOMAR UN FRAGMENTO Y REMPLAZARLO POR OTRO = NECESITA 2 PARAMETROS

texto = "Este es el texto de Moises"

resultado = texto.replace("Moises","todos ustedes mens")
print(resultado)

# ·······················································································································
texto = "Este es el texto de Moises"
resultado = texto.replace("Moises","todos ustedes mens")
print(resultado)


texto = "Este es el texto de Moises"  # EN ESTE EJERCICIO VEMOS COMO SE PUEDEN HACER DOS LINEAS EN EL MISMO PARAMETRO
resultado = (texto.replace("e","x")
             .replace("E","X"))
print(resultado)
# ·······················································································································

"PROPIEDADES DE LOS STRING"
# ·······················································································································
# CON ESTE EJERCICIO NOS DAMOS CUENTA QUE LOS STR SON INMUTABLES, OTRA COSA ES REESCRIBIR LA VARIABLE
# nombre = "Karina"
# nombre [0] = "C"
# print(nombre)

n1 = "Kari"
n2 = "na"
print(n1 + n2)
# ·······················································································································
# CON EL SIGNO DE * SE MULTIPLICARA Y NOS DARA COMO RESULTADO EL STR LAS VECES POR LAS CUALES SE HAYA REALIZADO DICHA MULTIPLICACION
n1 = "Kari"
n2 = "na"
print(n1 * 12)
# ·······················································································································
# DE ESTA MENERA PODEMOS ESCRIBIR UN STR CON SALTOS DE LINEA - COLO CANDO TRES VECES COMILLAS DOBLES (""" """)
poema = """mil pequeños peces blancos
como si hiriviera
el color del agua"""
print(poema)
# ·······················································································································
# CON ESTE EJERCICIO VAMOS A BUSCAR SI ALGUNA PALABRA SE ENCUENTRA DENTRO DEL TEXTO

poema = """mil pequeños peces blancos
como si hiriviera
el color del agua"""
print("agua" in poema) # IMPRIME SI "AGUA" ESTA EN LA VARIABLE 'POEMA' TIPO DE VALOR BOOLEANO
print("SOL" in poema)
print("agua" not in  poema) # IMPRIME SI ES QUE LA PALABRA NO ESTA EN LA VARIABLE
# ·······················································································································
"LEN" # ESTA PROPIEDAD NOS AYUDA PARA SABER EL LARGO

poema = """mil pequeños peces blancos
como si hiriviera
el color del agua"""
print(len(poema))

frase = "hola mundo"
print(len(frase))
# ·······················································································································
"TIPOS DE OBJETOS"

"LISTAS" # SIEMPRE VAN ENTRE CORCHETES Y TIENEN QUE SER SEPARADOS POR COMAS

mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2 # CONCATENACION
resultado = mi_lista[0:]
print(mi_lista3)
# ·······················································································································
# ESTA MANERA NOS AYUDA A SOBRESCRIBIR LA INFO ESTO SOLO SE PUEDE CON LAS LISTAS
mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = 'alfa'
print(mi_lista3)
# ·······················································································································
"APPEND" # AGREGAR
mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3.append('g') # AQUI SE ESTA AGREGANDO LA LETRA 'G' A LA LISTA
# ·······················································································································
"POP"
mi_lista3.pop() # CON "POP" SE ELIMINARA DE LA LISTA EL VALOR INGRESADO RECORDENMOS QUE SE DEBE DE INGRESAR EL VALOR SEGUN EL NUMERO DE POSICION QUE USA
print(mi_lista3)

# EN ESTE EJERCICIO VAMOS A ALMACENAR DENTRO DE UNA VARIABLE EL VALOR ELIMINADO POR EL "POP",RECORDAR ASIGNAR LA VARIABLE PARA
# EL ALMACENAMIENTO DEL VALOR ELIMINADO
mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2
eliminado = mi_lista3.pop()
print(mi_lista3)
print(eliminado)

"SORT" # ACOMODAR U ORDENAR
lista = ['g','h','a','x','f']
lista.sort() # AQUI ESTA ACOMODANDO POR ORDEN ALFABETICO
# ·······················································································································
"REVERSE"
lista.reverse()# ESTE METODO NOS ACOMODA DESDE LO ULTIMO HATA LO PRIMERO
print(lista)
# ·······················································································································
"DICCIONARIOS" # SE ESCRIBEN ENTRE LLAVES Y VAN SEPARADOS POR UNA COMA NO TIENEN ORDEN NI INDICE

diccionario = {'fb':'M01535Fg','getinio':'Moises271100','apple':'271100'}
resultado = diccionario['fb']
print(diccionario[1])

