numerop1 : int = int(input("jugador 1 ingrese su numero: "))
numerop2 : int = int(input("jugador 2 ingrese su numero: "))

if (numerop1 == numerop2):
    print("ganaste en 0 intentos o.o")

while (numerop1 != numerop2):
    for intentos in range(1, 20):
        numerop2 = int(input("ingrese otro numero: "))

        if (numerop2 == numerop1):
            print("ganaste en", intentos, "intentos")

    print("excedio los 20 intentos")
    numerop2 = numerop1

    #corregir