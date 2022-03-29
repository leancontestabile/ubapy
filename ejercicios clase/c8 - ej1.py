#Escribir una función que permita calcular la duración en segundos de un intervalo dado en horas, minutos y segundos.
def horasasegundos(horas:int)->int:
    segundos = horas * 3600
    return segundos
def minutostosegundos(minutos:int)->int:
    segundos = minutos * 60
    return segundos

def main()->None:
    horas = int(input("ingrese las horas: "))
    minutos = int(input("ingrese los minutos: "))
    segundos = int(input("ingrese los segundos: "))

    totalduracion = horasasegundos(horas) + minutostosegundos(minutos) + segundos
    print(totalduracion)
main()

"""
otra solucion

def intervalo(horas:int, minutos:int, segundos:int)->int:
    total: int = horas*3600 + minutos*60 + segundos
    return total

def main()->None:
    horas:int = int(input("ingrese horas "))
    minutos:int = int(input("ingrese minutos "))
    segundos:int = int(input("ingrese segundos "))

    resultado = intervalo(horas, minutos, segundos)
    print(resultado)
main()
"""