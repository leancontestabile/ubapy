contadornumero = 0

numero = int(input("numero: "))

for divisor in range (1, numero):
    if (numero % divisor) == 0:
        contadornumero = contadornumero + divisor

if contadornumero < numero:
    print("deficiente")
elif contadornumero > numero:
    print("abundante")
else:
    print("perfecto")



#extra
"""contadornumero = 0

veces = int(input("veces "))

for numero in range (1,veces + 1):
    for divisor in range (1, numero):
        if (numero % divisor) == 0:
            contadornumero = contadornumero + divisor

    if contadornumero < numero:
        print(numero, "deficiente")
    elif contadornumero > numero:
        print(numero, "abundante")
    else:
        print(numero, "perfecto")
    
    contadornumero = 0"""