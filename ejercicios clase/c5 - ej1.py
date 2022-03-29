#Pedir al usuario que ingrese 10 números y retornar la suma de los mismos.

suma = 0

for k in range(10):
    valor = int(input("ingrese un numero: "))
    suma = suma + valor

print("la suma de todos los numeros es", suma)