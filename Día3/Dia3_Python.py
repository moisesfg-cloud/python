
#metodo de string
frase = "Este es el texto de Moises"
texto = (frase
         .replace("el","un")
         .replace("Moises","Todos"))
print(texto)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ". join([a,b,c,d])
print(e)
#Práctica Métodos de String 2
#Une la siguiente lista en un string, separando cada elemento con un espacio.
#Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
#Une la siguiente listalista_palabras = ["La","legibilidad","cuenta."]

lista_palabras = ["La","legibilidad","cuenta."]
a = "La"
b = "legibilidad"
c = "cuenta."
d = " ".join([a,b,c])
print(d)


#Práctica Métodos de String 3
#Reemplaza en la siguiente frase:
#"Si la implementación es difícil de explicar, puede que sea una mala idea."
#los siguientes pares de palabras:
#"difícil" --> "fácil"
#"mala" --> "buena"
#y muestra en pantalla la frase con ambas palabras modificadas.

texto = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = (texto
            .replace("difícil","fácil")
            .replace("mala","buena"))
print(resultado)

#Práctica Propiedades de Strings 1
#Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. Por suerte, conoces que los strings son multiplicables y puedes realizar esta actividad de forma simple y elegante.
frase = "Repetición"
print(frase * 15)

#Práctica Propiedades de Strings 2
#Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.
#Tierra mojada,
#mis recuerdos de viaje
#entre las lluvias

poema = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""

resultado = print("agua" not in poema)


#Práctica Propiedades de Strings 3
#Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.

frase = "electroencefalografista"
print(len(frase))

mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2
eliminado = mi_lista3.pop(0)
print(mi_lista3)
print(eliminado)

lista = ['g','o','b','m','c']
lista.sort()
print(lista)

#Práctica Listas 1
#Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.

mi_lista = ['M','V',27,27.5,'P']

#Práctica Listas 2
#Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
#medios_transporte = ["avión", "auto", "barco", "bicicleta"]
#No debes modificar la línea de código ya suministrada,
#sino que debes emplear el método apropiado de listas para añadir un nuevo elemento.

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
adicion = medios_transporte.append("motocicleta")
print(medios_transporte)

#Práctica Listas 3
#Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas,y
#almacénalo en una variable llamada eliminado. Utiliza métodos de listas sin alterar la línea de código ya suministrada.
#manzana
#banana
#mango
#cereza
#sandía

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
correccion = frutas.pop(2)
eliminado = correccion
print(frutas)
print(eliminado)

#DICCIONARIO

diccionario = {'c1':'valor1','c2':'valor1'}
print(type(diccionario))
print(diccionario)
resultado = diccionario['c1']
print(resultado)

Contraseñas ={'Facebook':'Moises271100','google getin':'Moises271100',}
Solicitud = Contraseñas ['Facebook']
print(Solicitud)
#---------------------------------------------------------------
persona = {'nombre':'Moises','apellido':'Feria','peso':90,'edad':22,'estatura':1.86}
resultado = persona ['nombre']
print(resultado)

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c3']['s2'])

dic1= {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic1['c2'][1].upper())
#Ó

dic1= {'c1':['a','b','c'],'c2':['d','e','f']}
operacion = (dic1['c2'][1])
print(operacion.upper())

#--------------------------------------------------------
dic2 = {1:'a',2:'b'}
print(dic2)

dic[3]='c'
print( dic)
#--------------------------------------------------------
Contraseñas ={1:'Facebook-Moises271100',2:'google getin-Moises271100',}
Solicitud = Contraseñas [1]
print(Solicitud)

Contraseñas[3] = 'gmail-Moises271100'
print(Contraseñas)

Contraseñas[1] = 'Facebook-Hola mundo'
print(Contraseñas)
print(Contraseñas.keys())
print(Contraseñas.items())
#--------------------------------------------------------
#Práctica Diccionarios 1
#Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:
#nombre: Karen
#apellido: Jurgens
#edad: 35
#ocupacion: Periodista
#Los nombres de las claves y valores deben ser iguales a la consigna.

mi_dic = {'nombre':'Karen','apellido':'Jurgens','edad':35,'ocupacion':'Periodista'}

#Práctica Diccionarios 2
#Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.
#Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en esa misma posición.
#Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])


#Práctica Diccionarios 3
#Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
#nombre: Karen
#apellido: Jurgens
#edad: 36
#ocupacion: Editora
#pais: Colombia
#para ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

mi_dic["pais"] = "Colombia"
mi_dic["nombre"] = "Karen"
mi_dic["apellido"] = "Jurgens"
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
print(mi_dic)

#TUPLES

mi_tuple = (1,2,(10,20),4)
mi_tuple = list(mi_tuple)
print(mi_tuple)

mi_tuple = (1,2,(10,20),4)
print(mi_tuple[2][0])
print(mi_tuple.index(1))

t =  (1,2,3)
x,y,z = t #PARA QUE SE LE AGREGUE EL VALOR A LA VARIANTE SIEMPRE TIENEN QUE SER EL MISMO NUMERO DE VALORES
print(x,y,z)

t =  (1,2,3)
print(len(t)) #Saber el largo

t = (1,2,3,4,1)
print(t.index(2))

#Práctica Tuples 1
#Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla, y muestra el resultado (integer) en pantalla:
#mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

#Práctica Tuples 2
#Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.
#mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_tupla = list(mi_tupla)
mi_lista= mi_tupla

#Práctica Tuples 3
#Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d
#mi_tupla = (1, 2, 3, 4)

mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla
print(a,b,c,d)

#PROYECTO3
texto = input("Ingresa un texto:")
print (" Ingresa 3 letra de tu elección ")
letra1 = input("Letra 1: ")
letra2 = input("Letra 2: ")
letra3 = input("Letra 3: ")
letra4 =print(letra1 + letra2 + letra3)
#MINUSCULAS
print("MINUSCULAS")
convercion = texto.lower()
print(convercion)
#LISTA
print("LISTA \n")
lista= [letra1 + " " + letra2 + " " + letra3]
print(lista)
#CONTEO
print("CONTEO")
print(convercion.count(letra1))
print(convercion.count(letra2))
print(convercion.count(letra3))
print("\n")
#SEGUNDO ANALISIS
print("SEGUNDO ANALISIS\n")
largo = len(texto)
print(largo)
print("\n")
#TERCER ANALISIS
print("TERCER PUNTO\n")
index = convercion[1]
index1 = convercion[-2]
print(index)
print(index1)
print("\n")
#CUARTO ANALISIS
print("CUARTO ANALISIS\n")
frase = texto
texto = frase[::-1]
print(texto)


#----------------------------------------------------------------------------------
#PROYECTO3 2.1
texto =input("Ingresa un texto: ")
letras = []

texto = texto.lower()

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segnda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al reeves va a decir '{texto_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True:"Si", False:"No"}
print(f"La palabra 'Python {dic[buscar_python]} se encuentra en el texto")
