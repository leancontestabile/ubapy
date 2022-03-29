#sumar | restar | multiplicar | dividir | salir
#1     |2       |3            |4        |5

menuopen : bool = True

menucalculo : str = str(input("bienvenido a la calculadora, que quiere hacer? "))

while menuopen == True:

    if menucalculo != "sumar" and menucalculo != "1" and menucalculo != "restar" and menucalculo != "2" and menucalculo != "multiplicar" and menucalculo != "3" and menucalculo != "dividir" and menucalculo != "4" and menucalculo != "salir" and menucalculo != "5":
        menucalculo = str(input("error, ingrese una opcion correcta "))

    if menucalculo == "sumar" or menucalculo == "1":
        numero1 = int(input("ingrese el primer numero a sumar "))
        numero2 = int(input("ingrese el segundo numero a sumar "))
        suma = numero1 + numero2
        print(suma)
        menucalculo = str(input("quiere hacer otra operacion? "))
    
    if menucalculo == "restar" or menucalculo == "2":
        numero1 = int(input("ingrese el primer numero a restar "))
        numero2 = int(input("ingrese el segundo numero a restar "))
        resta = numero1 - numero2
        print(resta)
        menucalculo = str(input("quiere hacer otra operacion? "))

    if menucalculo == "multiplicar" or menucalculo == "3":
        numero1 = int(input("ingrese el primer numero a multiplicar "))
        numero2 = int(input("ingrese el segundo numero a multiplicar "))
        multiplicacion = numero1 * numero2
        print(multiplicacion)
        menucalculo = str(input("quiere hacer otra operacion? "))

    if menucalculo == "dividir" or menucalculo == "4":
        numero1 = int(input("ingrese el primer numero a dividir "))
        numero2 = int(input("ingrese el segundo numero a dividir "))
        division = numero1 / numero2
        print(division)
        menucalculo = str(input("quiere hacer otra operacion? "))

    if menucalculo == "salir" or menucalculo == "5":
        print("hasta la proxima")
        menuopen = False