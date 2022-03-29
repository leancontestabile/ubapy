#Escribir una función que dados cuatro números, devuelva el mayor producto de dos de ellos
def maximo_producto(num_1, num_2, num_3, num_4):
    max = -999
    m1 = num_1 * num_2
    if m1 > max:
        max = m1
    m12 = num_1 * num_3
    if m12 > max:
        max = m12
    m13 = num_1 * num_4
    if m13 > max:
        max = m13
    m2 = num_2 * num_3
    if m2 > max:
        max = m2
    m21 = num_2 * num_4
    if m21 > max:
        max = m21
    m3 = num_3 * num_4
    if m3 > max:
        max = m3
    return max

def main()->None:
    num1: int = int(input("ingrese el primer numero: "))
    num2: int = int(input("ingrese el segundo numero: "))
    num3: int = int(input("ingrese el tercer numero: "))
    num4: int = int(input("ingrese el cuarto numero: "))
    resultado = maximo_producto(num1, num2, num3, num4)
    print(resultado)
main()

#1,5,-2,-4 = 8