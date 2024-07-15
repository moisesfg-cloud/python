 // Asi se hace un booleano con if y else
if (5 > 3 && 3 > 4) {
    console.log("verdadero")
}   else{
    console.log("falso")
}
// switch en JS
let descuento = 0
let pais =
//if (pais == "Peru"){
//    descuento = 10
// } else if (pais == "Argentina") {
 //   descuento = 10
// } else if (pais == "Bolivia") {
//    descuento = 20
//}

//console.log(descuento)

switch (pais){
    case "Argentina":
        descuento = 10;
        break
    case "Bolivia":
        descuento = 30;
        break
    case "Peru":
    descuento = 20;
    break
}
// Año

let year = 2023
if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
    console.log("El ano " + year + "es bisiesto")
 } else {
    console.log("El ano " + "no es bisiesto")
 }
//

function ejecutar() {
}