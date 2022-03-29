"""
Cargar los datos de cada país (nombre del país, cantidad de registros, cantidad de usd invertidos en el juego).
Mostrar la información de los países que tengan más de 50.000 usd invertidos.
Mostrar el índice de usd invertidos totales/registros totales
Usar mínimo 3 funciones. 
El usuario no puede ingresar dos veces el mismo país
"""
def ingresopais () -> list:
    pais: str = str(input("ingrese el nombre del pais: "))
    registros: int = int(input("ingrese la cantidad de registros: "))
    inversion: int = int(input("ingrese la invesion en usd: "))
    datospais: list = [pais, registros, inversion]
    return datospais
def paisesconaltainversion (listapaises: list) -> list:
    for i in listapaises:
        if i[2] > 50000:
                print(i[0], "tiene una inversion de mas de $50000")
def rentabilidad (listapaises: list) -> None:
    inversiontotal = 0
    registrostotales = 0
    for i in listapaises:
        inversiontotal = inversiontotal + i[2]
        registrostotales = registrostotales + i[1]
        calculo = inversiontotal / registrostotales
        calculofinal = print(i[0], "tiene un indice de usd invertidos/registros totales de", calculo)
    return calculofinal

def main()->None:
    ingreso: bool = True
    listapaises: list = []
    while ingreso:
        listapaises.append(ingresopais())
        print(listapaises)
        pregunta = str(input("desea ingresar otro pais? (si/no) "))
        if pregunta == "si":
            ingreso = True
        else:
            ingreso = False
    paisesconaltainversion(listapaises)
    rentabilidad(listapaises)
main()