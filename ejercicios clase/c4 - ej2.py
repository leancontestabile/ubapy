#Escribe un programa en Python que solicite 5 números enteros al usuario. El mismo debe indicar si entre dichos valores hay números duplicados o no, imprimiendo por pantalla “HAY DUPLICADOS” o “SON TODOS DISTINTOS”.

import random

numero1 = random.randint(0,10)
numero2 = random.randint(0,10)
numero3 = random.randint(0,10)
numero4 = random.randint(0,10)
numero5 = random.randint(0,10)

distincion = True  #son distintos?

if numero1 == numero2 or numero1 == numero3 or numero1 == numero4  or numero1 == numero5:
    distincion = False
elif numero2 == numero3 or numero2 == numero4 or numero2 == numero5:
    distincion = False
elif numero3 == numero4 or numero3 == numero5:
    distincion = False
elif numero4 == numero5:
    distincion = False

mensaje = print("son todos distintos") if distincion else print("hay duplicados")

print(numero1, numero2, numero3, numero4, numero5)