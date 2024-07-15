#VARIABLES/ EN las variables deben de comenzar siempre con una letra ya que de empezar con un numero el compiladro nos regresara un error

#Una variable  es cuando tu guardas un libro u objeto ese es valor de la variable
#caja = variable
#objeto a guardar = valor

nombre = "Moises"
print(nombre)
nombre = "Laura"
print(nombre)
nombre = input("Cual es tu nombre: ")
print("Tu nombre es " + nombre)
#========================================================================================================================
nombre = "CR7"
nombre2 = " El bicho"
frase1 = " SIUUUUUUU"
frase = nombre + nombre2 + frase1
print(frase)
print("\n")
#========================================================================================================================
#Práctica con Variables 1
#Declara dos variables, llamadas nombre y edad.
#Asigna a la variable nombre el valor "Tony Soprano", y a la edad, el valor 51.
nombre = "Tony Soprano"
edad = 51
print(nombre)
print(edad)
print("\n")
#========================================================================================================================
#Práctica con Variables 2
#Crea tres variables:
#nombre
#apellido
#nombrecompleto

nombre = "Julia"
print(nombre)
apellido = "Roberts"
print(apellido)
nombrecompleto = nombre+apellido
print(nombrecompleto)
nombrecompleto = "JuliaRoberts"
print(nombrecompleto)
print("\n")
#========================================================================================================================
#Práctica con Variables 3
#Declara la variable curso, asígnale el valor "Python", y muestra en pantalla la frase:

Frase= "Estas tomando un curso de"
Curso = "Python"
print(Frase + Curso)
print("\n")
#========================================================================================================================



#PROYECTO 2
#Nombre del empleado#

#Nombre = input("Nombre del empleado: ")
#Ventas = input("Cuanto vendiste en este mes: $" )
#Informacion = print("\n\t" +  (Nombre) + "\n\t" + "$"  + (Ventas))
#Texto = input("Tus datos son correctos: ")
#Conversion= int(Ventas)
#Conversion1= float(Conversion)
#Comisiones = 0.13
#Resultado2 = (f"{Conversion*Comisiones}")
#Resultado1 = print(f"{Nombre} tus ganancia por comision seran de: $ {Resultado2}\n\t 'Sig ue Vendiendo'")
#print(type(Resultado2))

#ó

Nombre = input("Nombre del empleado: ")
Ventas = input("Cuanto vendiste en este mes: $" )

Ventas = int(Ventas)
Comision = Ventas * 13 / 100
Comision = round(Comision)
print(f"{Nombre}, tus ganancias por comision seran de ${Comision}")
print("\n")
Materias = {materia1:'Mateticas',materia2: 'Física',materia3: 'Química'}
