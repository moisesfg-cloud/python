
#FUNCION FORMAT
#format : remplaza los valores que estan contenidos en las variables por llaves vacias
#EJEMPLO:
Nombre = "Moises"
apellido = "Feria"
print("Mi nombre es '{}' y mi apellido es '{}' por lo cual mi nombre es {} ".format(Nombre, apellido, Nombre+ " " +apellido))

#EJEMPLO:
#Cadenas Literales  - se colocan las llaves de igual manera pero ahora con la info dentro de la llave

Nombre = "Moises"
apellido = "Feria"
print(f"Mi nombre es {Nombre} y mi apellido es {apellido} ")


#========================================================================================================================


#Práctica Formatear Cadenas 1
#Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:
#Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)
#Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.

nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print("Estimado/a {}, su número de asociado es: {}".format(nombre_asociado,numero_asociado))
print("\n")
#========================================================================================================================
#Práctica Formatear Cadenas 2
#Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:
#Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

puntos_nuevos = 350
puntos_totales = 1225
print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos,puntos_totales))
print("\n")
#========================================================================================================================
#Práctica Formatear Cadenas 3
#Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:
#Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos
#En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos.
#========================================================================================================================
puntos_anteriores = 875
puntos_nuevos = 350
puntos_totales = puntos_nuevos + puntos_anteriores
print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos,puntos_totales))
print("\n")

#REFINAMIENTO
puntos_anteriores = 875
puntos_nuevos = 350
print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos,puntos_nuevos+puntos_anteriores))
#-------------------------------------

Consola1 = 'XBOX'
Consola2 = 'Play'
Consola3 = 'Nintendo'
Consola4 = 'Switch'

print("Algunos dicen que {} es mejor que {} pero algunos piensan que {} es mejor que {}".format(Consola1,Consola2,Consola3,Consola4))

print(f"Algunos dicen que {Consola2} es mejor que {Consola1} pero algunos piensan que {Consola3} es mejor que {Consola4}")