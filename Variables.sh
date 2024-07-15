"PARAMETROS"
Un script puede recibir información mediante parametros, que seran cadenas de texto que pondremos despues del nombre del script
Estaran separado por espacios
Dentro del script podremos acceder a ellos mediante variables predefinidas del sistema:
#-$n= la informacion de un parametro en concreto,siendo n un numero del parametro
#-$*= todos los parametros. Se presentan en una sola cadena de caracteres
#-$#= sirve para saber cuantos parametros se han introducido.
#-$@= todos los parametros. Es una lista con un elemento por cada parametro recibido
#----------------------------------------------------------
#COMO USAR "VI"
 vim == a vi
 para salir de vi tenemos que ingresar ":q" en caso de que no quieras guardar y quieras forzar la salida de vi ingresa ":q!"
 :x == guardar y salir
 :W == guardar
 :q == salir
 :q! == forzar salida
:set numbre == te numera las lineas del archivo
#"NAVEGAR EN VI"
h - te desplaza hacia la izquierda
j - te desplaza hacia abajo
k - te desplaza hacia arriba
l - te desplaza hacia la derecha
0 = te pone al principio de la linea
$ = te pone al final de la linea
e = te pone al final de cada palabra
b = te ubica al inicio de la palabra
* = te ubica en la siguiente palabra con la cual coincide en donde estas parado
gg = te envia a la primera linea del documento
GG = te envia al final del documento
numero de linea que queiras + G = te envia a la liena que ingresaste
o = crea una nueva linea y activa el modo de incersicion
x minuscula = elimina el caracter sobre el cual  estas parado
r +  letra a cambiar= remplaza la letra en donde esta parado el puntero
dw = elimina palabra
dd = elima linea
p = pega info
:/ +  palabra a buscar  = esta funcion es para buscar + "n" para ir viendo en donde esta cada palabra

"CONFIGURACION DE VI O VIM"
set showmode = valida que la sintaxis sea correcta
ser autoindent = identacion para cuando oprimamos "enter"
set tabstop + el numero de renglones por cada vez que vayamos a oprimir "enter"
set expandtap = esta funcion permite las tabulaciones
sintax on = activa la sintaxis

Pais



