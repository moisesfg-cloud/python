#printenv
#Print Work Directori = PWD
#HOME = Ruta para el home del equipo
#PATH - Apunta a las carpetas en donde estan almacenados los binarios
#ecport = inicializas una variable
#"Un binario es un programa que se encarga de realizar una tarea"

#EJERCICIOS
#OPERADORES ARITMETICOS

numA=2
numB=2
echo "Operadores Aritmeticos entre $numA y $numB"
echo "---------------------------------------------------"
echo "$numA + $numB = " $((numA + numB))
echo "$numA - $numB = " $((numA - numB))
echo "$numA * $numB = " $((numA * numB))
echo "$numA / $numB = " $((numA / numB))
echo "---------------------------------------------------"
echo "0 = FALSE , 1 = TRUE"
echo "$numA » $numB = " $((numA > numB))
echo "$numA « $numB = " $((numA < numB))
echo "$numA »= $numB = " $((numA >= numB))
echo "$numA «= $numB = " $((numA <= numB))
echo "$numA != $numB = " $((numA != numB))

#Operadores de asignacion
