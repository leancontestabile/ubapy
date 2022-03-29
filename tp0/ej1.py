"""Escribir un programa que pida dos números enteros al usuario (a y b) e imprima los primeros a múltiplos de b.
El programa debe validar que cada número que ingrese el usuario sea un entero positivo y, en caso de que no lo sea, solicitarlo nuevamente (hasta que se ingrese algo correcto)."""

numeroa: str = str(input("Ingrese el número 'a': "))

while numeroa.isdecimal() == False or numeroa == "0":
    numeroa: str = str(input("Ingrese el número 'a': "))
else:
    a: int = int(numeroa)

numerob: str = str(input("Ingrese el número 'b': "))

while numerob.isdecimal() == False or numerob == "0":
    numerob: str = str(input("Ingrese el número 'b': "))
else:
    b: int = int(numerob)

for multiplos in range(1,a + 1):
    resultado = b * multiplos
    print(resultado)