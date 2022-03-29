ingresonumero : bool = True
acumuladornumero : int = 0
contadornumero : int = 0
numeromaximo : int = -999
numerominimo : int = 999
minimototal : int = 999

for juegonumeros in range(8):
    while ingresonumero == True:
        numero : int = int(input("ingrese un numero: "))
        if numero < 0:
            print("debe ingresar un numero positivo")

        while numero >= 0:
            acumuladornumero = acumuladornumero + numero
            contadornumero = contadornumero + 1

            if numero < numerominimo:
                numerominimo = numero
        
            if numero > numeromaximo:
                numeromaximo = numero
        
            pregunta = str(input("desea ingresar otro numero? "))

            if pregunta == "si":
                ingresonumero = True
            else:
                ingresonumero = False
            numero= -1

    ingresonumero = True

    promedio = acumuladornumero / contadornumero

    print("el numero maximo de este juego es:", numeromaximo)
    print("el numero minimo de este juego es:", numerominimo)
    print("el promedio de este juego es:", promedio)

    if numerominimo < minimototal:
        minimototal = numerominimo
        nminimototal = juegonumeros

    numeromaximo = -999
    numerominimo = 999
    acumuladornumero = 0
    contadornumero = 0

print("el minimo total es:", minimototal, "del juego numero", nminimototal)