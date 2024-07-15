#TIPOS DE DATOS
#string (str) - son: "hola","%$&","123"
#integer(int) - son: numeros enteros 150,1,555,-15,0
#floating (float) - numeros decimales 1.25,25.0,500.50,-95.1
#listas (list) - ["sal",1,-3,4.5,"marte",0] coleccion de datos ordenada van entre corchetes   Las listas tienen un orden en numero en que empieza desde 0
#diccionarios (dic) - {'color':'rojo':'arte':'cine'} van entre llaves {clave y valor - cada diccionario tiene dos pares las cuales contienen una clave y un valor, los pares no estan ordenados, tienen un orden interior
#tuples (tuple) - ('lun','mar','mie','jue','vie') cualquier tipo de dato, orden que no se puedee cambiar
#sets (set)- {'a','b','c'.'d','e'} conjunto de elementos ordenados unicos
#booleanos (bool) - Solo puede tener dos valotes true(verdadero) - false(Falso) - sirve para que nuestro codigo tome dicisiones, saber si se cumple una condicion.
========================================================================================================================

#STRING: En resumen, un Python string es una cadena formada por una secuencia de caracteres individuales.
#INTEGER O INT : Entero o int. Los enteros en Python o también conocidos como int, son un tipo de datos que permite representar números enteros, es decir, positivos y negativos no decimales.
#FLOAT: El tipo numérico float permite representar un número positivo o negativo con decimales, es decir, números reales.
#BOOLEANO: Al igual que en otros lenguajes de programación, en Python existe el tipo bool o booleano. Es un tipo de dato que permite almacenar dos valores True o False .

========================================================================================================================
#\n = salto de linea
#\t = tabulador
#append () - agregar
#.sort () - ordenar
#.reverse () - ordena desde el final hasta el principio
#pop () - saltar o eliminar el ultimo de los elementos
#upper() - pasar a mayusculas
#lower() - pasar a minusculas
#split() - separalo en partes (lista)
#join() - unir items usando separador
#find() - encontrar un substring
#replace()  - reemplazar un substring
#len() - determina su longitud
#index - buscar elementos dentro de los strings asi como tambien muestra la posicion desde la cual comienza busca elemento de izquierda a derecha \
#rindex - busca el elemento de derecha a izquierda
#multilineales: pueden escribirse en varias líneas al encerrarse entre triples comillas simples (''' ''') o dobles (""" """)
#los diccionarios no tienen un orden
========================================================================================================================
#Operadores Lógicos
#mayor >
#menor <
#mayor o igual >=
#menor o igual <=
#igual ==
#diferente !=
#incremento de uno en uno a = 1 a+= 1 a = a + 1
========================================================================================================================

print(f"{x} mas {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} dividido {y} es igual a {z/y}")
print(f"{x} dividido al piso {y} es igual a {z//y}") esta es cuando realizas una division y en lugar de que te de un resultado con punto decimal lo haga con un numero entero
print(f"{x} modulo de {y} es igual a {z%y}") #cuantas veces cabe en el numero#
print(f"{x} elevado a la {y} es igual a {x**y}")
print(f"{x} elevado a la {3} es igual a {x**3}")
print(f"La raiz cuadrada de  {x} es  {x**0.5}")
========================================================================================================================
Funciones
format : remplaza los valores que estan contenidos en las variables por llaves vacias
