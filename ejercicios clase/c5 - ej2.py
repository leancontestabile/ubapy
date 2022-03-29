#Vicky toma el control del reloj y repetirá cuantas veces quiera hasta que sacie su sed de venganza. 
#Se debe pedir al usuario (Vicky) si quiere agregar un gato más al ataque contra Timmy, cuando ya esté satisfecha se deberá mostrar la cantidad de gatos que atacaron a Timmy.

gatos = 0
pregunta = True

print("hola vicky")

while pregunta == True:
    gatos = gatos + 1
    preguntausuario = str(input("agregar otro gato? "))
    if preguntausuario == "si":
        pregunta = True
    else:
        pregunta = False

print("el numero de gatos que atacaron a timmy fueron:", gatos)