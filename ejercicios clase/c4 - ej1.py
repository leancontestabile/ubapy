#Escribe un programa en Python que solicite al usuario 5 números enteros. Luego imprimir el máximo y el mínimo de los valores ingresados. El programa deberá permitir el ingreso de valores iguales.

import random

numero1 = random.randint(0,10)
numero2 = random.randint(0,10)
numero3 = random.randint(0,10)
numero4 = random.randint(0,10)
numero5 = random.randint(0,10)

print(numero1, numero2, numero3, numero4, numero5)

maximo = max(numero1, numero2, numero3, numero4, numero5)
print("el numero mas grande es:", maximo)

minimo = min(numero1, numero2, numero3, numero4, numero5)
print("el numero mas chico es:", minimo)