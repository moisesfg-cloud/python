#Práctica con Tipos de Datos Numéricos
#¿De qué tipo es el resultado de la suma de 7.5 + 2.5? Genera el código para verificarlo.

#Para ello, crea dos variables:

num1 = 7.5
num2 = 2.5

print(type(num1 + num2))
print("\n")
#================================================================================================================
#El proceso de convertir un tipo de dato en otro tipo de dato se llama casting y existen dos tipos:
#**Implicita: Sucede en automatico por Python cuando realizamos ciertas operaciones con dos tipos distintos y
#eso lo resuelve trasnformando el datos sin que  nos demos cuenta**
#Explicita: Cuando pedimos a traves del codigo que un tipo de dato se ha convertido en otro tipo de dato:
#Como se hace? R= Expresando que quiero meter un determinado tipo de dato dentro de otro:

# #========================================================================================================================

#                     EJEMPLO :
    #     mi_valor = 1
#      otro_valor = str(mi_valor)

#EJERCICIOS - IMPLICITO

num1 = 20
num2 = 30.5
num1 = num1+num2
print(type(num1))
print(type(num2))
print()
#EJERCICIOS-EXPLICITO

num = 5.8
print(num1)
print(type(num1))

num2 = int(num1)
print(num2)
print(type(num2))

edad = input("Dime tu edad: ")

print(type(edad))

edad = int(edad)

print(type(edad))

nueva_edad = 1 + edad
print("Tu nueva edad va a ser:" + str(nueva_edad))

#========================================================================================================================
#Práctica con Conversiones 1
#Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:

num1 = 7.5
num = int(num1)
print(type(num))
print("\n")

#========================================================================================================================    #Práctica con Conversiones 2
#Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:

num2 = 10
num1 = float(num2)
print(type(num1))
print("\n")

#========================================================================================================================
#Práctica con Conversiones 3
#Suma los valores de num1 y num2.
#No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la función print().

num1 = "7.5"
num2 = "10"
num3 = float(num1)
num4 = float(num2)
num7 = print(float(int(num4) + (num3)))
print("\n")

#ó

num1 = "7.5"
num2 = "10"

num3 = float(num1)
num4 = float(num2)

num7 = print(num4 + num3)
#========================================================================================================================
