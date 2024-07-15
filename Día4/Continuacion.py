# MIN Y MAX
# ESTAS FUNCIONES SE USAN DE LA SIGUIENTE MANERA

# EN ESTE EJERCICIO EL MIN Y MAX NOS AYUDA A SABER CUAL ES EL NUMERO MAS GRANDE Y CUAL ES EL MAS PEQUENO
menor = (58, 34, 10, 98)
mayor = (58, 34, 10, 98)
print(min(menor))
print(max(mayor))

lista = [58, 96, 73, 64, 4]
print(f"El menor es {min(lista)} y el menor es {max(lista)} ") #

nombre = ["Alicia","Carlos","Sergio","Yair"]
print(min(nombre)) # IMPRIME EL NOMBRE CON LA PRIMERA LETRA MENOR O INICIAL SEGUN LE ABECEDARIO
print(max(nombre)) # IMPRIME EL NOMBRE CON LA PRIMERA LETRA MAYOR O ULTIMA

nombre = "Carlos"
print(min(nombre)) # IMPRIMIO LA "c" DEBIDO A QUE PRIMERO BUSCA LAS MAYUSCULAS EN CASO DE QUE SE CONTENGA ALGUNA
print(max(nombre))
print(min(nombre.lower())) #AQUI SE AGREGA EL METODO LOWER PARA EVITAR QUE BUSQUE MAYUSCULAS Y NO OBTENGAMOS EL RESULTADO DESEADO


nombre = "carlos"
print(min(nombre)) #COMO TODAS SON LOWER IMPRIME LA MENOR
print(max(nombre))

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

maximo = max(lista_numeros)
minimo = min(lista_numeros)

rango = maximo - minimo

print("El rango de la lista de números es:", rango)


diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
minimo = min(diccionario_edades.values())
edad_minima = minimo
print(edad_minima)
nombre = max(diccionario_edades)
ultimo_nombre = nombre
print(ultimo_nombre)


# metodo randint "RANDOM INTEGER" metodo para que nos devuelva un numero entero aleatorio
# libreria = random
# for random import randit

#HAY QUE IMPORTAR DESDE LA LIBRERIA EL METODO
    # seria 'desde' random (libreria) import 'randint' = from random import randint

    #EN CASO DE QUE VAYAMOS A OCUPAR MUCHOS METODOS DE UNA MISMA LIBRERIA EN LUGAR DE INGRESAR EL METODO SOLO PONER "*"
    #EJEMPLO:

    # from random import randint
    # ó
    # from random import *

    #METODOS A APRENDER
    #RANDINT ()
    #UNIFORM ()
    #RANDOM ()
    #CHOICE ()
    #SHUFFLE ()


from random import * #CON ESTO ESTAMOS IMPORTANDO LA LIBRERIA Y TODOS SUS METODOS

aleatorio = randint(1,70) #EN ESTA LINEA CON EL RANDINT ESCOGERA UN NUMERO ALEATORIO DEL 1 AL 70
print(aleatorio)

aleatorio = round(uniform(1,50),1) #UNIFORM ESCOGE UN NUMERO ALEATORIO PERO QUE SEA DECIMAL
#SE HIZO UN CASTING CON LA FUNCION ROUND (REDONDEO) PARA SELECCIONAR CUANTOS DECIMALES QUEREMOS
print(aleatorio)

aleatorio = random() #DENTRO DE ESTA METODO NO SE ESCRIBIRA NADA YA QUE RANDOM TOMARA UN NUMERO FLOAT ENTRE 1 y 0
print(aleatorio)

colores = ['azul','amarillo','verde','rojo']
aleatorio = choice(colores) #EL METODO CHOICE TOMARA ALEATORIAMENTE CUALQUIER VALOR DE UNA LISTA O CUALQUIER COLECCIONABLE
print(aleatorio)

numeros = list(range(5,50,5))
shuffle(numeros) #EL METODO SHUFFLE SIGNIFICA MEZCLAR EL CUAL MEZCLA LO VALORES DE LA LISTA DESORDENANDO O ACOMODANDO DE NUEVO LOS LUGARES DE CADA VALOR
#NO SE PUEDE USAR CON STRINGS
print(numeros)


#COMPRENSION DE LISTAS

palabra = "phyton"
lista= []
for letra in palabra: #POR CADA "LETRA" EN "PALABRA"
    lista.append(letra) #AGREGA LETRA POR LETRA EN LA LISTA
print(lista)

#MANERA CON COMPRENSION DE LISTAS 




palabra = "phyton"
lista = [letra for letra in palabra] #DENTRO DE LA LISTA AGREGA LETRA POR LETRA DE PALABRA
print(lista)

#ó

lista = [letra for letra in "phyton"]
print(lista)

#AHORA CON NUMEROS

lista = [numeros for numeros in range(0,40,2)] #DENTRO DE LA LISTA NUMERO POR NUMERO AGREGA EL RANGO DEL 0 AL 40 DE DOS EN DOS
print(lista)

lista = [numeros /2 for numeros in range(0,40,2)] #DENTRO DE LISTA NUMEROS DIVIDIDOS POR DOS PRO NUMEROS DENTRO DEL RANGO DEL 0 AL 40 DE DOS EN DOS
print(lista)

lista = [numeros for numeros in range(0,40,2) if numeros * 2 > 10] #DENTRO DE LA LISTA NUMEROS POR NUMEROS EN EL RANGO DEL 0 AL 40 DE DOS EN DOS
#SOLO IMPRIME SIEMPRE Y CUANDO MULTIPLICADOS POR DOS SEAN MAYORES A 10
print(lista)


lista = [numeros if numeros * 2 > 10 else "no" for numeros in range(0,40,2)] # AGREGAREMOS A NUMEROS SIEMPRE Y CUNADO NUMEROS *2 SEA MAYOR A 10 Y SI NO SE PONDRA LA PALABRA NO
#POR CADA NUMEROS QUE ESTE EN EL RANGO


pies = [10,20,30,40,50]
metros = [numero /3.281 for numero in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [numeros for numeros in valores]
print(valores_cuadrado)


valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [numeros for numeros in valores]
print(valores_pares)

