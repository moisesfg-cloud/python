#Práctica Operadores de Comparación 1
#Crea dos variables (num1 y  num2) con los valores 36 y 17 respectivamente.
#Verifica si num1 es mayor o igual que num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool
num1 = 36
num2 = 17
mi_bool = num1>=num2
print(mi_bool)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Práctica Operadores de Comparación 2
#Crea dos variables (num1 y  num2):
#Dentro de num1, almacena el resultado de la operación raíz cuadrada de 25
#Dentro de num2, almacena el número 5.
#Verifica si num1 es igual a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.
raiz = 25**0.5 #Raiz cuadrada
num1 = raiz
num2 = 5
mi_bool = num1 == num2
print(mi_bool)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Práctica Operadores de Comparación 3
#Crea dos variables (num1 y  num2):
#Dentro de num1, almacena el resultado de la operación 64 x 3
#Dentro de num2, almacena el resultado de la operación 24 x 8
#Verifica si num1 es diferente a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 64*3  #Multiplicacion
num2 = 24*8  #Multiplicacion
mi_bool = num1!=num2
print(mi_bool)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Práctica Operadores Lógicos 1
#Crea tres variables (num1 ,  num2 y num3):
#Dentro de num1, almacena el valor 36
#Dentro de num2, almacena el resultado de la operación 72/2
#Dentro de num3, almacena el valor 48
#Verifica si num1 es mayor que num2, y menor que num3.
#Almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 36
num2 = 36.0
num3 = 48
validar = num1 > num2
res = validar < num3
mi_bool = validar
print("mi_bool")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Práctica Operadores Lógicos 2
#Crea tres variables (num1 ,  num2 y num3):
#Dentro de num1, almacena el valor 36
#Dentro de num2, almacena el resultado de la operación 72/2
#Dentro de num3, almacena el valor 48
#Verifica si num1 es mayor que num2, o menor que num3.
#Almacena el resultado de dicha comparación en una variable llamada mi_bool.

num1 = 36
num2 = 36
num3 = 48
validar = num1 > num2
res = validar < num3
mi_bool = res
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Práctica Operadores Lógicos 3
#Verifica si las palabras almacenadas en las siguientes variables:
#palabra1 = "éxito", y
#palabra2 = "tecnología"
#no se encuentran en la frase a continuación,
#y almacena el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:
#"Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
#Elon Musk

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = ('éxito'  not in frase) and  ('tecnología' not in frase)
print(mi_bool)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CONTROL DE FLUJO
numero = int(input("Escoje un numero del 1 al 10: "))
if 10 > numero:
    print('Este número es menor')
else:
    print('Este número es mayor ')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mascota = input("Que animal tienes: ")

if mascota == ' un gato':
    print('Tienes un gato')
elif mascota == 'un perro':
    print('Tienes un perro')
elif mascota == 'un pez':
    print('Tienes un pez')
else:
    print('No se que animal tienes')
edad =  16

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

calificación = 9

if edad < 18:
    print('Eres menor  de edad')
    if calificación>=7:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('No eres adulto')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Práctica Control de Flujo 1
#Utilizando las variables num1 y num2, que se alimentan con el input del usuario (tal como en el código ya proporcionado):
#Crea una estructura de control de flujo que compare los valores de las variables, y arroje un resultado de acuerdo al caso:
#"num1 es mayor que num2"
#"num2 es mayor que num1"
#"num1 y num2 son iguales"
#Debes mostrar en pantalla el valor de las variables ingresadas en lugar de num1 y num2.
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
        print(f"{num1} es mayor que {num2}")
elif num2 > num1:
        print(f"{num2} es mayor que {num1}")
else:
        print(f"{num1} y {num2} son iguales")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Práctica Control de Flujo 2
#Las leyes de un país establecen que un adulto puede conducir si tiene licencia para hacerlo,
#y para optar por una licencia para conducir, debe de tener 18 años o más.
#Crea una estructura condicional para verificar si una persona de 16 años sin licencia puede conducir,
#y muestra el resultado que corresponda en pantalla:
#"Puedes conducir"
#"No puedes conducir aún. Debes tener 18 años y contar con una licencia"
#"No puedes conducir. Necesitas contar con una licencia"
#Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones.

edad = int(input('Ingresa tu edad: '))
tiene_licencia = False

"Puedes conducir"
"No puedes conducir aún. Debes tener 18 años y contar con una licencia"
("No puedes conducir. Necesita"
 "s contar con una licencia")

if edad > 18:
    print("Puedes conducir")
elif edad <18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Práctica Control de Flujo 3
#Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python y tener conocimientos de inglés.
#Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:
#"Cumples con los requisitos para postularte"
#"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"
#"Para postularte, necesitas tener conocimientos de inglés"
#"Para postularte, necesitas saber programar en Python"
#Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones.
#Evalúa a un candidato que sabe inglés, pero no programa en Python.

habla_ingles = True
sabe_python = False

"Cumples con los requisitos para postularte"
"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"
"Para postularte, necesitas tener conocimientos de inglés"
"Para postularte, necesitas saber programar en Python"

if habla_ingles == sabe_python:
    print("Cumples con los requisitos para postularte")
elif sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif habla_ingles:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
#---------------------------------------------------------------------------
monedas = 5
#while significa "mientras"
while monedas > 0:
    print(f"Tengo {monedas} monedas ")
    #puede escribirse de estas dos maneras:
    # monedas = monedas -1 o monedas -=1
    monedas = monedas -1
else:print("No tengo mas dinero")

respuesta = 's'
while respuesta == 's':
     respuesta = input("Quieres continuar?: (s/n)")
else:
    print("De acuerdo, gracias")

    #PASS - PASAR  / BREAK
nombre = input("Ingresa tu nombre: ")
for letra in nombre:
    if letra =='s':
         continue
    print(letra)
