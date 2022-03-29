import random
ESCALERA = {3: 18, 6: 67, 57: 83, 72: 89, 85: 96}
SERPIENTE = {98: 79, 88: 31, 86: 45, 63: 22, 58: 37, 48: 12, 36: 17}

def menu() -> None:
    print("1 Iniciar Partida\n2 Mostrar Estadisticas\n3 Resetear Estadisticas\n4 Salir")

def generador_casillero_banana(casilleros_ocupados: list) -> dict:
    casilleros_bananas: dict = {}
    for i in range(5):
        bananakey: int = random.randint(21,99)
        bananavalue: int = bananakey -20
        while bananakey in casilleros_ocupados or bananavalue in casilleros_ocupados or bananakey in casilleros_bananas:
            bananakey: int = random.randint(21,99)
            bananavalue: int = bananakey -20
        casilleros_bananas[bananakey] = bananavalue
    return casilleros_bananas

def generador_casillero_magico(casilleros_ocupados: list) -> dict:
    casilleros_magicos:dict = {}
    for i in range(3):
        magicokey: int = random.randint(2,99)
        magicovalue: int = random.randint(2,99)
        while magicokey in casilleros_ocupados or magicovalue in casilleros_ocupados or magicokey in casilleros_magicos:
            magicokey: int = random.randint(2,99)
            magicovalue: int = random.randint(2,99)
        casilleros_magicos[magicokey] = magicovalue
    return casilleros_magicos

def generador_casillero_rushero(casilleros_ocupados: list) -> dict:
    validacion: bool = True
    rusherokey: int = random.randint(1,99)
    rusherovalue = 0
    while rusherokey % 10 == 0 or rusherokey in casilleros_ocupados or rusherovalue in casilleros_ocupados:
        rusherokey = random.randint(1,99)
    rusherovalue = rusherokey + 1
    casillero_rushero: dict = {}
    while validacion:
        if rusherovalue % 10 == 0:
            casillero_rushero[rusherokey] = rusherovalue
            validacion = False
        else:
            rusherovalue = rusherovalue + 1
    return casillero_rushero

def generador_casillero_hongos(casilleros_ocupados: list) -> dict:
    validacion: bool = True
    hongoskey: int = random.randint(2,99)
    hongosvalue = 0
    while hongoskey % 10 == 1 or hongoskey in casilleros_ocupados or hongosvalue in casilleros_ocupados:
        hongoskey = random.randint(2,99)
    hongosvalue = hongoskey - 1
    casillero_hongos: dict = {}
    while validacion:
        if hongosvalue % 10 == 0:
            hongosvalue = hongosvalue + 1
            casillero_hongos[hongoskey] = hongosvalue
            validacion = False
        else:
            hongosvalue = hongosvalue - 1
    return casillero_hongos

def movimiento_dado(posicion: int):
    dado: int = random.randint(1, 6)
    print("\ndado:", dado)
    posicion_mas_dado = posicion + dado
    return posicion_mas_dado

def movimiento(posicion_mas_dado: int, casilleros_banana: dict, casilleros_magico: dict, casillero_rushero: dict, casillero_hongos: dict) -> int:
    movimiento = posicion_mas_dado
    if movimiento in ESCALERA:
        movimiento = ESCALERA[movimiento]
        print("subiste por una escalera")
    elif movimiento in SERPIENTE:
        movimiento = SERPIENTE[movimiento]
        print("bajaste por una serpiente")
    elif movimiento in casilleros_banana:
        movimiento = casilleros_banana[movimiento]
        print("te resbalaste con una cascara de banana")
    elif movimiento in casilleros_magico:
        movimiento = casilleros_magico[movimiento]
        print("te teletransportaste magicamente")
    elif movimiento in casillero_rushero:
        movimiento = casillero_rushero[movimiento]
        print("rusheaste hasta la esquina del tablero")
    elif movimiento in casillero_hongos:
        movimiento = casillero_hongos[movimiento]
        print("te pusiste loco y corriste a la esquina del tablero")
    if movimiento > 100:
        movimiento = 100
    return movimiento

def main() -> None:
    jugador1: int = 0
    jugador2: int = 0
    turno: int = random.randint(0,1)
    contadores: dict = {"contador_escaleras": 0, "contador_serpientes": 0, "contador_bananas": 0, "contador_magicos": 0, "contador_rusheros": 0, "contador_hongos": 0}
    contadores_vacios: int = 0
    casilleros_ocupados = list(ESCALERA.keys()) + list(ESCALERA.values()) + list(SERPIENTE.keys()) + list(SERPIENTE.values())
    casillero_bananas: dict = generador_casillero_banana(casilleros_ocupados)
    casilleros_ocupados = list(ESCALERA.keys()) + list(ESCALERA.values()) + list(SERPIENTE.keys()) + list(SERPIENTE.values()) + list(casillero_bananas.keys()) + list(casillero_bananas.values())
    casillero_magicos: dict = generador_casillero_magico(casilleros_ocupados)
    casilleros_ocupados = list(ESCALERA.keys()) + list(ESCALERA.values()) + list(SERPIENTE.keys()) + list(SERPIENTE.values()) + list(casillero_bananas.keys()) + list(casillero_bananas.values()) + list(casillero_magicos.keys()) + list(casillero_magicos.values())
    casillero_rushers: dict = generador_casillero_rushero(casilleros_ocupados)
    casilleros_ocupados = list(ESCALERA.keys()) + list(ESCALERA.values()) + list(SERPIENTE.keys()) + list(SERPIENTE.values()) + list(casillero_bananas.keys()) + list(casillero_bananas.values()) + list(casillero_magicos.keys()) + list(casillero_magicos.values()) + list(casillero_rushers.keys()) + list(casillero_rushers.values())
    casillero_hongo: dict = generador_casillero_hongos(casilleros_ocupados)
    tablero ="""
!! 99 S7 97 E5 95 94 93 92 91
81 82 E3 84 E5 S5 87 S6 E4 90
80 S7 78 77 76 75 74 73 E4 71
61 62 S4 64 65 66 E2 68 69 70
60 59 S3 E3 56 55 54 53 52 51
41 42 43 44 S5 46 47 S2 49 50
40 39 38 S3 S1 35 34 33 32 S6
21 S4 23 24 25 26 27 28 29 30
20 19 E2 S1 16 15 14 13 S2 11
01 02 E1 04 05 E2 07 08 09 10
"""
    menu()
    opcion: str = str(input("-> "))
    while opcion != "4":
        if opcion == "1":
            nombre_j1: str = str(input("ingrese el nombre del jugador 1\n-> "))
            nombre_j2: str = str(input("ingrese el nombre del jugador 2\n-> "))
            print("\nCasilleros\nSerpientes ->", SERPIENTE, "\nEscaleras ->", ESCALERA,"\nBananas ->", casillero_bananas, "\nMagicos ->", casillero_magicos, "\nRushero ->", casillero_rushers, "\nHongo loco ->", casillero_hongo)
            input("\nPresione la tecla Enter para continuar")
            while jugador1 < 100 and jugador2 < 100:
                turno = turno + 1
                if not turno % 2 == 0:
                    jugador1_mas_dado = movimiento_dado(jugador1)
                    if jugador1_mas_dado in ESCALERA:
                        contadores["contador_escaleras"] = contadores["contador_escaleras"] + 1
                    elif jugador1_mas_dado in SERPIENTE:
                        contadores["contador_serpientes"] = contadores["contador_serpientes"] + 1
                    elif jugador1_mas_dado in casillero_bananas:
                        contadores["contador_bananas"] = contadores["contador_bananas"] + 1
                    elif jugador1_mas_dado in casillero_magicos:
                        contadores["contador_magicos"] = contadores["contador_magicos"] + 1
                    elif jugador1_mas_dado in casillero_rushers:
                        contadores["contador_rusheros"] = contadores["contador_rusheros"] + 1
                    elif jugador1_mas_dado in casillero_hongo:
                        contadores["contador_hongos"] = contadores["contador_hongos"] + 1
                    jugador1 = movimiento(jugador1_mas_dado, casillero_bananas, casillero_magicos, casillero_rushers, casillero_hongo)
                    if jugador1 < 10:
                        jugador1str = str(jugador1)
                        jugador1str = "0" + jugador1str
                    else:
                        jugador1str = str(jugador1)
                    tablero = tablero.replace(jugador1str, "J1")
                    print(tablero)
                    print("el jugador 1", nombre_j1, "se encuentra en el casillero numero", jugador1)
                    input("ingrese Enter para tirar los dados\n")
                    if jugador1 >= 100:
                        print("""
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |      | Ganador |
            '-|:.     |-'      | Jugador 1 |
              \::.    /
               '::. .'
                 ) (
               _.' '._
                """)
                else:
                    jugador2_mas_dado = movimiento_dado(jugador2)
                    if jugador2_mas_dado in ESCALERA:
                        contadores["contador_escaleras"] = contadores["contador_escaleras"] + 1
                    elif jugador2_mas_dado in SERPIENTE:
                        contadores["contador_serpientes"] = contadores["contador_serpientes"] + 1
                    elif jugador2_mas_dado in casillero_bananas:
                        contadores["contador_bananas"] = contadores["contador_bananas"] + 1
                    elif jugador2_mas_dado in casillero_magicos:
                        contadores["contador_magicos"] = contadores["contador_magicos"] + 1
                    elif jugador2_mas_dado in casillero_rushers:
                        contadores["contador_rusheros"] = contadores["contador_rusheros"] + 1
                    elif jugador2_mas_dado in casillero_hongo:
                        contadores["contador_hongos"] = contadores["contador_hongos"] + 1
                    jugador2 = movimiento(jugador2_mas_dado, casillero_bananas, casillero_magicos, casillero_rushers, casillero_hongo)
                    if jugador2 < 10:
                        jugador2str = str(jugador2)
                        jugador2str = "0" + jugador2str
                    else:
                        jugador2str = str(jugador2)
                    tablero = tablero.replace(jugador2str, "J2")
                    print(tablero)
                    print("el jugador 2", nombre_j2, "se encuentra en el casillero numero", jugador2)
                    input("ingrese Enter para tirar los dados\n")
                    tablero ="""
!! 99 S7 97 E5 95 94 93 92 91
81 82 E3 84 E5 S5 87 S6 E4 90
80 S7 78 77 76 75 74 73 E4 71
61 62 S4 64 65 66 E2 68 69 70
60 59 S3 E3 56 55 54 53 52 51
41 42 43 44 S5 46 47 S2 49 50
40 39 38 S3 S1 35 34 33 32 S6
21 S4 23 24 25 26 27 28 29 30
20 19 E2 S1 16 15 14 13 S2 11
01 02 E1 04 05 E2 07 08 09 10
"""
                    if jugador2 >= 100:
                        print("""
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |      | Ganador |
            '-|:.     |-'      | Jugador 2 |
              \::.    /
               '::. .'
                 ) (
               _.' '._
                """)
            jugador1 = 0
            jugador2 = 0
            turno = random.randint(0,1)
        elif opcion == "2":
            for i in contadores.values():
                if i == 0:
                    contadores_vacios = contadores_vacios + 1
            if contadores_vacios == 6:
                print("\nNo hay estadisticas")
                contadores_vacios = 0
            else:
                print("\nLas estadisticas de cuanto se han activado los casilleros son\nEscaleras:", contadores["contador_escaleras"],"\nSerpientes:", contadores["contador_serpientes"],"\nBananas:", contadores["contador_bananas"],"\nMagicos:", contadores["contador_magicos"],"\nRusheros:", contadores["contador_rusheros"],"\nHongos:", contadores["contador_hongos"])
        elif opcion == "3":
            contadores= {"contador_escaleras": 0, "contador_serpientes": 0, "contador_bananas": 0, "contador_magicos": 0, "contador_rusheros": 0, "contador_hongos": 0}
            contadores_vacios = 0
            print("\nLas estadisticas se han reiniciado")

        opcion = str(input("\n1 Iniciar Partida\n2 Mostrar Estadisticas\n3 Resetear Estadisticas\n4 Salir\n-> "))
    print("\nHasta luego!")
main()