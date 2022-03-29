#Se dice que dos números A y B se llaman números amigos si la suma de los divisores de A es igual B y la suma de los divisores de B es igual a A.
def numeros_amigos(a: int, b: int) -> bool:
    contador1 = 0
    contador2 = 0
    for divisor in range (1, a):
        if (a % divisor) == 0:
            contador1 += divisor
    for divisor in range (1, b):
        if (b % divisor) == 0:
            contador2 += divisor
    if contador1 == b and contador2 == a:
        numeros_amigos = True
    else:
        numeros_amigos = False
    return numeros_amigos

def main()->None:
    numero1 = int(input("ingrese el primer numero: "))
    numero2 = int(input("ingrese el segundo numero: "))
    numeros_amigos(numero1, numero2)
main()