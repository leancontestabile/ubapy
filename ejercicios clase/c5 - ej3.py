#Búsqueda de extremos: 
#Solicitar el ingreso de n números, hallar el maximo y el minimo.

pregunta = True
numeromax = -999
numeromin = 999

while pregunta == True:
    numero = int(input("ingrese su numero: "))
    if numero > numeromax:
        numeromax = numero
    if numero < numeromin:
        numeromin = numero
    
    preguntausuario = str(input("agregar otro numero? "))
    if preguntausuario == "si":
        pregunta = True
    else:
        pregunta = False

print("el numero maximo es:", numeromax, "y el numero minimo es:", numeromin) 