def signo_zodiaco(dia, mes):
    if mes == 1:
        zodiaco = 0 + dia
    elif mes == 2:
        zodiaco = 31 + dia
    elif mes == 3:
        zodiaco = 59 + dia
    elif mes == 4:
        zodiaco = 90 + dia
    elif mes == 5:
        zodiaco = 120 + dia
    elif mes == 6:
        zodiaco = 150 + dia
    elif mes == 7:
        zodiaco = 181 + dia
    elif mes == 8:
        zodiaco = 212 + dia
    elif mes == 9:
        zodiaco = 242 + dia
    elif mes == 10:
        zodiaco = 273 + dia
    elif mes == 11:
        zodiaco = 303 + dia
    elif mes == 12:
        zodiaco = 334 + dia
    if zodiaco >= 0 and zodiaco <= 20 or zodiaco >= 356 and zodiaco <= 365:
        signo="Capricornio"
    elif zodiaco >= 21 and zodiaco <= 50:
        signo="Acuario"
    elif zodiaco >= 51 and zodiaco <= 79:
        signo="Piscis"
    elif zodiaco >= 80 and zodiaco <= 110:
        signo="Aries"
    elif zodiaco >= 111 and zodiaco <= 140:
        signo="Tauro"
    elif zodiaco >= 141 and zodiaco <= 171:
        signo="Geminis"
    elif zodiaco >= 172 and zodiaco <= 204:
        signo="Cancer"
    elif zodiaco >= 205 and zodiaco <= 235:
        signo="Leo"
    elif zodiaco >= 236 and zodiaco <= 265:
        signo="Virgo"
    elif zodiaco >= 266 and zodiaco <= 295:
        signo="Libra"
    elif zodiaco >= 296 and zodiaco <= 325:
        signo="Escorpio"
    elif zodiaco >= 326 and zodiaco <= 355:
        signo="Sagitario"
    return signo

def main():
    dia: int = int(input("Ingrese el dia: "))
    mes: int = int(input("Ingrese el mes: "))
    resultado = signo_zodiaco(dia, mes)
    print(resultado)
main()