# # #OPERADORES LOGICOS
# #
# # # Y - and
# # # O - or
# # # NO - not
# #
# # #Ejercicio para saber si las operaciones son verdaderas o falsas
# #
# # num = 10 < 5 and 5 > 10
# # print(num)
# #
# # num1 = 10 < 5 or 5 > 10
# # print(num1)
# #
# # #Vamos a validar si una palbra u otra se encuentran en el texto
# # frase = "Moises trabaja 9 horas"
# # busqueda = ("Moises" in frase) and ("9 horas" in frase)
# # print(busqueda)
# #
# # num = not 10 > 5
# # print(num)
# #
# # #CONTROL DE FLUJO - SEA LA OPCION QUE SEA SIEMPRE SE DEBERAN CERRAR CON DOS PUNTOS
# # # if - si
# # # elif - si no ocurre vamos a la otra opcion
# # # else - si no ocurre ninguno
# #
# # if 10 == 9:
# #     print("Es correcto")
# # else:
# #     print("Es incorrecto")
# #
# # # Aqui vamos a validar dependiendo el valor de mascota es la respuesta que obtendras por parte del codigo
# #
# # mascota = input("Que mascota tienes: ")
# # numero_de_mascotas = input("Cuantas mascotas tienes: ")
# #
# # if mascota == "gato" and "gatos":
# #     print(f"Tienes { numero_de_mascotas } gato")
# # elif mascota == "perro" and "perros":
# #     print(f"Tienes { numero_de_mascotas } perro")
# # else:
# #     print("No se que animal tienes")
# #
# #
# # # En este ejercicio vamos a validar dependiendo la edad de la persona si el codigo reconoce si es menor o mayor de edad
# #
# # edad = int(input("Introduce tu edad: "))
# # calificacion = int(input("Cual es tu calificacion: "))
# #
# # if edad < 18:
# #     print("Eres menor de edad")
# #     if calificacion >= 7:
# #         print("Aprobado")
# #     else:
# #         print("No aprobado")
# # else:
# #     print("Eres mayor de edad")
# #
# # CELULAR = input("Cual es la marca de tu celular:".lower() )
# #
# # if CELULAR == "apple":
# #     print("Tienes celular de rico")
# # else:
# #     print("Tienes celular de probre")
# #
# # # En este ejercicio vamos a solicitar al usuario que ingrese dos numero con los cuales se van a generar 3 comparaciones.
# #
# # num1 = int(input("Ingresa un número:"))
# # num2 = int(input("Ingresa otro número:"))
# #
# # f"{num1} es mayor que {num2}"
# # "num2 es mayor que num1"
# # "num1 y num2 son iguales"
# #
# #
# # if num1 > num2:
# #     print(f"{num1} es mayor que {num2}")
# # elif num2 > num1:
# #     print(f"{num2} es mayor que {num1}")
# # else:
# #     print(f"{num1} y {num2} son iguales")
# from Día4.Dia4_Python import numero
#
# # Crear un codigo que sea capaz de determinar con la respuesta del usuario si es capaz o no de postularse.
#
# # habla_ingles = input('Sabes ingles: '.lower())
# # sabe_python = input('Sabes Python: '.lower())
# #
# # "Cumples con los requisitos para postularte"
# #
# # "Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"
# #
# # "Para postularte, necesitas tener conocimientos de inglés"
# #
# # "Para postularte, necesitas saber programar en Python"
# #
# # if habla_ingles == "si" and sabe_python == "si":
# #     print("Cumples con los requisitos para postularte")
# # elif habla_ingles == "si":
# #     print("Para postularte, necesitas saber programar en Python")
# # elif sabe_python == "si":
# #     print("Para postularte, necesitas tener conocimientos de inglés")
# # else:
# #     print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
# #
# #
# # if habla_ingles and sabe_python:
# #     print("Cumples con los requisitos para postularte")
# # elif habla_ingles:
# #     print("Para postularte, necesitas saber programar en Python")
# # elif sabe_python:
# #     print("Para postularte, necesitas tener conocimientos de inglés")
# # else:
# #     print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
# #
# # # LOOP FOR
# #
# # nombres = ['juan','ana','carlos','belen']
# #
# #     # por cada elemento en nombmbres
# #             # imprimir ('hola')
# #
# # nombres = ['juan','ana','carlos','belen']
# # for elemento in nombres:
# #     print('hola ' + elemento)
# #
# # #Aqui lo que hacemos es hacer que cada letra dentro de la lista sea acompanada del texto o cadena
# # mi_lista = ['a','b','c','d']
# # for letrita in mi_lista:
# #     print('Letra: ' + letrita)
# #
# # #Aqui lo que vamos a hacer es que cada letra tenga el numero de letra que es acompanada de el texto
# # mi_lista = ['a','b','c','d']
# # for letrita in mi_lista:
# #     numero_letra= mi_lista.index(letrita) + 1 #Con ese numero 1 lo que se hace es que por cada letra en lista se le asigne un numero
# #     print(f'Letra {numero_letra}:  {letrita}')
# #
# # #METODO - .startswith este metodo nos ayuda a saber si alguna cadena comienza con un determinado caracter
# #
# # nombres = ['moises','yair','sergio','maria','mauricio']
# #
# # for item in nombres:
# #     if item.startswith('m'): #.startswith te ayuda a saber que valores comienzan con el caracter a buscar
# #         print(f"El nombre {item} comienza con 'm' ")
# #         print("\n")
# #     else:
# #         print(f"Estos nombres no comienzan con 'm' :"
# #               f"{item}")
# #         print("\n")
# #     if item.endswith('o'): #.endswith te ayuda a saber que valores terminan con el caracter a buscar
# #         print(f"El nombre {item} termina con 'o' ")
# #         print("\n")
# #     else:
# #         print(f"Estos nombres no comienzan con 'o' :"
# #               f"{item}")
# #
# # numeros = [1,2,3,4,5]
# # mi_valor = 0
# #
# # for numero in numeros:
# #     mi_valor = mi_valor + numero
# #
# #     print(mi_valor) #Si yo idento el print con un tab me aparecera la suma de los numeros
# # print(mi_valor) #Si yo idento el print al mismo nivel que el "for" solo me mostrara el resultado
# #
# #
# # apellidos = ['fernandez','feria','hernandez','gutierrez','mmarquez'.lower()]
# # for i in apellidos:
# #     if i.startswith("f"):
# #         print(f"Estos nombres comienzan con 'f': \n{i}")
# #
# # #LOOP WHILE / MIENTRAS
# #
# #         #mientras que se cumpla una condicion booleana (si o no)
# #                 #ejecutar el sig codigo
# #
# #     #while una_condicion:
# #         #un codigo
# #
# # monedas = 5
# #
# # while monedas > 0:
# #     print(f"Tengo {monedas} monedas") #Aqui lo que se esta haciendo es que el codigo nos imprima Tengo 5 monedas mientra monedas sea mayor a 0
# #     monedas = monedas - 1 #Aqui lo que se esta realizando es que al resultado de "monedas" se le restara - 1
# #     monedas -=1 #Tambien se puede hacer de esta manera
# #
# # respuesta = 'S'
# # while respuesta == 'S':
# #     respuesta = input("Deseas continuar? (S/N)")
# # else:
# #     print("Gracias")
#
# #PASS - GUARDA EL LUGAR PARA QUE PUEDAS SEGUIR AVANZANDO Y GUARDA UN LUGAR O LINEA
# #BREAK - INTERRUMPIR LA ITERACION DEL LOOP Y SALE DEL LOOP
#
#
# # nombre = input("Tu nombre: ")
# # for i in nombre:
# #     if i == 'e': #En este ejercicio el usuario va a ingresar su nombre y el codigo lo va a interrumpir cuando se encuentre la letra "e"
# #         break
# #     print(i)
# #
# # nombre = input('moises')
# # for i in nombre:
# #     if i == 's': #En este ejercicio hay una cadena de texto y el codigo nos esta mostrando la letra cual se ingreso dentro del if
# #         print(i)
# #
# # escuela = input('Tu escuela es: ')
# # for i in escuela:
# #     if i == 'C':
# #         break
# #     print(i)
# #
# # #CONTINUE - TE PERMITE CONTINUAR PERO SIN EL CARACTER A BUSCAR
# #
# # escuela = input('Tu escuela es: ')
# # for i in escuela:
# #     if i == 'C':
# #         continue
# #     print(i)
# #
# # numero = 101
# # while numero > 0:
# #     numero -= 1 #DE ESTA MANERA HACEMOS QUE DISMINUYAN DE UNO EN UNO
# #     print(numero)
# #
# # numero = 51
# # while numero  > 0:
# #     numero -=1
# #
# #     if numero % 5 == 0:
# #         print(numero)
# #         continue
# # print("\n")
# # #Práctica Interrupción de Flujo
# # #Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos,
# # #e interrumpe el flujo en el momento que encuentres un valor negativo:
# #
# # lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4, 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]
# #
# # for numero in lista_numeros:
# #     if numero < 0:
# #         break
# #     print(numero)
# # print("\n")
# #
# # #RANGE O RABNGO FUNCIONA PARA SABER EL RANGO O LAS ITERECIONES DENTRO DEL CODIGO
# #
# # for numero in range(10): #En este codifo lo que se esta realizando es que con solo poner el range(10), estamos indicando que debe de detenerse en el numero 10
# #     print(numero)
# # # EJEMPLOS
# # for numero in range(10,40): # TRADUCCION: / POR CADA NUMERO DENTRO O EN EL RANGO DEL 10 AL 40 ME VAS A IMPRIMIR LOS NUMEROS QUE ESTEN EN ESE RANGO
# #     print(numero)
# #
# # for i in range(10,40,2): # EN EL RANGE SE TIENE UNA TERCERA OPCION QUE ES SELECCIONAR CADA CUANTOS NUMEROS SE ESTARA SALTANDO
# #     print(i)
# #
# # #ESTA FORMA EN EL RANGE NOS AYUDA A GENERAR LA LISTA DESDE EL NUMERO QUE DECEAMOS QUE COMIENZE HASTA EL CUAL QUEREMOS QUE TETMINE
# # lista = list(range(2500,2586))
# # print(lista)
# #
# # lista = list(range(1,101))
# # print(lista)
#
#
# # ENUMERADOR - ENUMERATE LA FUNCION DE ESTE ES AYUDARNOS A ACCEDER A LOS INDICES DE UNA COLECCION
#
# # EJEMPLO:
# # Nos ayuda a ingresar a los elementos dentro de un for
#
# # lista = ['a','b','c']
# # indice = 0
# # for i in lista:
# #     print(indice,i) #EN ESTE CODIGO LO QUE HACEMOS ES QUE EL INDICE OTORGE UN NUMERO EN FORMA DE LISTA POR CADA LETRA QUE CONTIENE
# #     indice +=1
# #     # SEGUN EL NUMERO INGRESADO
# #
# #
# #
# # nombre = 'moises'
# # indice = 0
# # for i in nombre:
# #     print(indice,i)
# #     indice +=1
# #
# #
# # lista = ['moises','eduardo','frank','yair']
# # for i,nombre in enumerate(lista):
# #      print(f'El nombre {nombre} se encuentra en el indice {i}')
# #
# #
# # txt="Python"
# # for i in list(enumerate(txt)):
# #     print(i)
# #
# #
# # txt = [1,2,3,4]
# # for i,numero in enumerate(txt): #QUE POR CADA "ITEM Y NUMERO" DENTRO DE LA LISTA DE "TXT" ME VAS A CREAR UNA LOS VAS A "NUMERAR"
# #     print(f"El numero {numero} se encuentra en el indice {i} de la lista ") #IMPRIME QUE NUMERO DE INDICE OCUPA CADA NUMERO DENTRO DE LA LISTA
# #
# #
# # nombre = "moises"
# # indice = 0
# # for i in nombre:           #A QUE POR CADA ITEM EN LA VARIABLE "NOMBRE
# # # ME VAS A IMPRIMIR EL INDICE Y EL ITEM
# #  print(indice,i)
# #  indice+=1       #AL CUAL POR CADA LETRA DE LA VARIABLE "NOMBRE" LE VAS A OTORGAR UN NUMERO COMENZANDO DESDE EL CERO
# #
# # #EL ENUMERADOR TAMBIEN SE PUEDE USAR DENTRO DE LAS LISTAS O TUPLAS
# #
# # lista = ['T','H','E'] #AQUI TENEMOS UN "TUPLE QUE SON LAS COMAS" DENTRO DE UNA LISTA
# # tupla = list(enumerate(lista)) #"GENERA UNA LISTA Y ENUMERA" LA VARAIBLE "LISTA"
# # print(tupla)
# # print(tupla [1])
# #
# #
# # lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
# # for i,nombre in (enumerate(lista_nombres)): #POR CADA "ITEM" Y "NOMBRE" EN "LISTA DE NUMEROS" VAS A ENUMERARLOS
# #     if nombre.startswith("M"): # SI EL "NOMBRE" DEL "ITEM" COMIENZA CON "M"
# #         print(i)  # ME VAS A IMPRIMIR EL "INDICE" DEL "ITEM"
# #
# #         # METODOS STRING O INDEX
# # lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
# # for i in range(len(lista_nombres)):
# #     if lista_nombres[i][0] == "M":
# #         print(i)
# #
# #         #ZIP NOS AYUDA A OTORGARLE UN VALOR A CADA ITEM DENTRO DE UNA LISTA
# #         a = [1,2]
# #         b = ["one","two"]
# #         c = zip(a,b)
# #         print(list(c))
# # # RECUERDA QUE SI TENEMOS UNA LISTA QUE CONTENGA 4 VALORES Y EN OTRA SOLO HAYA 3 VALORES LA FUNCION "ZIP" SOLO AGREGARA VALOR HASTA DONDE ESTE LA LISTA MAS CORTA
# #         #EJEMPLO
# #
# #         nombres = ['Moi','yair','sergio']
# #         edades = [23,22,28,50,30,102]
# # combinados = list(zip(nombres,edades))
# # print(combinados)
# #
# # nombres = ['Moi','yair','sergio']
# # edades = [23,22,28]
# # ciudades = ['mexico','honduras','venezuela']
# # combinados = list(zip(nombres,edades,ciudades )) #RECUERDA PONER LA FUNCION "LIST" YA QUE ZIP GENERA UN TUPLE Y NECESITA ESTAR DENTRO DE UNA LISTA
# # print(combinados)
# #
# # nombres = ['Moi','yair','sergio']
# # edades = [23,22,28]
# # ciudades = ['mexico','honduras','venezuela']
# # combinados = list(zip(nombres,edades,ciudades))
# # print(combinados)
# #
# # for nombre,edad,ciudades in combinados:
# #     print(f"{nombre} tiene {edad} años y vive en {ciudades}")
# #
# #
# #     capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
# # paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
# #
# # combinados = zip(capitales,paises)
# # for capitales, paises in combinados:
# #     print(f"La capital de {paises} es {capitales}")
# #
# #     marcas = ["Coca","apple","samsung","coppel"]
# # productos =["refresco","iphone","television","moto"]
# # mi_zip = list(zip(marcas,productos))
# # print(mi_zip[0])
# #
# # uno = ["uno","um","one"]
# # dos = ["dos","dois","two"]
# # tres = ["tres","três","three"]
# # cuatro = ["cuatro","quatro","four"]
# # cinco = ["cinco","cinco","five"]
# #
# #
# # uno = ["uno","um","one"]
# # dos = ["dos","dois","two"]
# # tres = ["tres","três","three"]
# # cuatro = ["cuatro","quatro","four"]
# # cinco = ["cinco","cinco","five"]
# # numeros = list(zip(uno, dos, tres, cuatro, cinco))
# # print(numeros)
# #
# #
# #
# # # MIN Y MAX
# # # ESTAS FUNCIONES SE USAN DE LA SIGUIENTE MANERA
# #
# # # EN ESTE EJERCICIO EL MIN Y MAX NOS AYUDA A SABER CUAL ES EL NUMERO MAS GRANDE Y CUAL ES EL MAS PEQUENO
# # menor = (58, 34, 10, 98)
# # mayor = (58, 34, 10, 98)
# # print(min(menor))
# # print(max(mayor))
# #
# # lista = [58, 96, 73, 64, 4]
# # print(f"El menor es {min(lista)} y el menor es {max(lista)} ") #
# #
# # nombre = ["Alicia","Carlos","Sergio","Yair"]
# # print(min(nombre)) # IMPRIME EL NOMBRE CON LA PRIMERA LETRA MENOR O INICIAL SEGUN LE ABECEDARIO
# # print(max(nombre)) # IMPRIME EL NOMBRE CON LA PRIMERA LETRA MAYOR O ULTIMA
# #
# # nombre = "Carlos"
# # print(min(nombre)) # IMPRIMIO LA "c" DEBIDO A QUE PRIMERO BUSCA LAS MAYUSCULAS EN CASO DE QUE SE CONTENGA ALGUNA
# # print(max(nombre))
# # print(min(nombre.lower())) #AQUI SE AGREGA EL METODO LOWER PARA EVITAR QUE BUSQUE MAYUSCULAS Y NO OBTENGAMOS EL RESULTADO DESEADO
# #
# #
# # nombre = "carlos"
# # print(min(nombre)) #COMO TODAS SON LOWER IMPRIME LA MENOR
# # print(max(nombre))
# #
# # lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
# #
# # maximo = max(lista_numeros)
# # minimo = min(lista_numeros)
# #
# # rango = maximo - minimo
# #
# # print("El rango de la lista de números es:", rango)
# #
# #
# # diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
# # minimo = min(diccionario_edades.values())
# # edad_minima = minimo
# # print(edad_minima)
# # nombre = max(diccionario_edades)
# # ultimo_nombre = nombre
# # print(ultimo_nombre)
# #
# #
# # # metodo randint "RANDOM INTEGER" metodo para que nos devuelva un numero entero aleatorio
# # # libreria = random
# # # for random import randit
# #
# # #HAY QUE IMPORTAR DESDE LA LIBRERIA EL METODO
# #     # seria 'desde' random (libreria) import 'randint' = from random import randint
# #
# #     #EN CASO DE QUE VAYAMOS A OCUPAR MUCHOS METODOS DE UNA MISMA LIBRERIA EN LUGAR DE INGRESAR EL METODO SOLO PONER "*"
# #     #EJEMPLO:
# #
# #     # from random import randint
# #     # ó
# #     # from random import *
# #
# #     #METODOS A APRENDER
# #     #RANDINT ()
# #     #UNIFORM ()
# #     #RANDOM ()
# #     #CHOICE ()
# #     #SHUFFLE ()
# #
# #
# # from random import * #CON ESTO ESTAMOS IMPORTANDO LA LIBRERIA Y TODOS SUS METODOS
# #
# # aleatorio = randint(1,70) #EN ESTA LINEA CON EL RANDINT ESCOGERA UN NUMERO ALEATORIO DEL 1 AL 70
# # print(aleatorio)
# #
# # aleatorio = round(uniform(1,50),1) #UNIFORM ESCOGE UN NUMERO ALEATORIO PERO QUE SEA DECIMAL
# # #SE HIZO UN CASTING CON LA FUNCION ROUND (REDONDEO) PARA SELECCIONAR CUANTOS DECIMALES QUEREMOS
# # print(aleatorio)
# #
# # aleatorio = random() #DENTRO DE ESTA METODO NO SE ESCRIBIRA NADA YA QUE RANDOM TOMARA UN NUMERO FLOAT ENTRE 1 y 0
# # print(aleatorio)
# #
# # colores = ['azul','amarillo','verde','rojo']
# # aleatorio = choice(colores) #EL METODO CHOICE TOMARA ALEATORIAMENTE CUALQUIER VALOR DE UNA LISTA O CUALQUIER COLECCIONABLE
# # print(aleatorio)
# #
# # numeros = list(range(5,50,5))
# # shuffle(numeros) #EL METODO SHUFFLE SIGNIFICA MEZCLAR EL CUAL MEZCLA LO VALORES DE LA LISTA DESORDENANDO O ACOMODANDO DE NUEVO LOS LUGARES DE CADA VALOR
# # #NO SE PUEDE USAR CON STRINGS
# # print(numeros)
# #
# #
# # #COMPRENSION DE LISTAS
# #
# # palabra = "phyton"
# # lista= []
# # for letra in palabra: #POR CADA "LETRA" EN "PALABRA"
# #     lista.append(letra) #AGREGA LETRA POR LETRA EN LA LISTA
# # print(lista)
# #
# # #MANERA CON COMPRENSION DE LISTAS
# #
# #
# #
# #
# # palabra = "phyton"
# # lista = [letra for letra in palabra] #DENTRO DE LA LISTA AGREGA LETRA POR LETRA DE PALABRA
# # print(lista)
# #
# # #ó
# #
# # lista = [letra for letra in "phyton"]
# # print(lista)
# #
# # #AHORA CON NUMEROS
# #
# # lista = [numeros for numeros in range(0,40,2)] #DENTRO DE LA LISTA NUMERO POR NUMERO AGREGA EL RANGO DEL 0 AL 40 DE DOS EN DOS
# # print(lista)
# #
# # lista = [numeros /2 for numeros in range(0,40,2)] #DENTRO DE LISTA NUMEROS DIVIDIDOS POR DOS PRO NUMEROS DENTRO DEL RANGO DEL 0 AL 40 DE DOS EN DOS
# # print(lista)
# #
# # lista = [numeros for numeros in range(0,40,2) if numeros * 2 > 10] #DENTRO DE LA LISTA NUMEROS POR NUMEROS EN EL RANGO DEL 0 AL 40 DE DOS EN DOS
# # #SOLO IMPRIME SIEMPRE Y CUANDO MULTIPLICADOS POR DOS SEAN MAYORES A 10
# # print(lista)
# #
# #
# # lista = [numeros if numeros * 2 > 10 else "no" for numeros in range(0,40,2)] # AGREGAREMOS A NUMEROS SIEMPRE Y CUNADO NUMEROS *2 SEA MAYOR A 10 Y SI NO SE PONDRA LA PALABRA NO
# # #POR CADA NUMEROS QUE ESTE EN EL RANGO
# #
# #
# # pies = [10,20,30,40,50]
# # metros = [numero /3.281 for numero in pies]
# # print(metros)
# #
# # valores = [1, 2, 3, 4, 5, 6, 9.5]
# # valores_cuadrado = [numeros for numeros in valores]
# # print(valores_cuadrado)
# #
# #
# # valores = [1, 2, 3, 4, 5, 6, 9.5]
# # valores_pares = [numeros for numeros in valores]
# # print(valores_pares)

# monedas = 5
# while monedas > 0:
#     monedas = monedas - 1
#     print(f"Tengo {monedas} mone- es que al resultado de "monedas" se le restara - 1
# monedas -=1  # Tambien se puede hacer de esta manera

#PREGUNTAR NOMBRE\
nombre = input("Dime cual es tu nombre: ")
print(f'Bueno,{nombre} he pensado un numero entre el 1 y 100, solo tienes ocho intentos para adivinar que numero es')
intentos = 8
from random import randint
aleatorio = randint(0,100)
ingreso = int(input("A ver que numero crees que es: "))
while intentos > 0:
    # print(f"Te quedan {intentos} intentos")
if ingreso == aleatorio:
    print(f"Felicidades adivinaste, esto te tomo {intentos} intentos")
elif ingreso < 1 or ingreso > 100:
    print("El numero ingresado no esta permitido")
elif ingreso <= aleatorio:
    print(f"El numero que ecogiste fue {ingreso} y el numero aleatorio fue {aleatorio}")
intentos = intentos -1
# break cuando intentos llegue a 0
