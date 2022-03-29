import random
ESCALERA = {3: 18, 6: 67, 57: 83, 72: 89, 85: 96}
SERPIENTE = {98: 79, 88: 31, 86: 45, 63: 22, 58: 37, 48: 12, 36: 17}

def mostrar_opciones() -> None:
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
        magicovalue = "magia"
        while magicokey in casilleros_ocupados or magicokey in casilleros_magicos:
            magicokey: int = random.randint(2,99)
            magicovalue: int = "magia"
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
    hongoskey: int = random.randint(12,99)
    hongosvalue = 0
    while hongoskey % 10 == 1 or hongoskey in casilleros_ocupados or hongosvalue in casilleros_ocupados:
        hongoskey = random.randint(12,99)
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

def tablero_base() -> str:
    tablero ="""
!! 99 S7 97 E5 95 94 93 92 91
81 82 E3 84 E5 S5 87 S6 E4 90
80 S7 78 77 76 75 74 73 E4 71
61 62 S4 64 65 66 E2 68 69 70
60 59 S3 E3 56 55 54 53 52 51
41 42 43 44 S5 46 47 S2 49 50
40 39 38 S3 S1 35 34 33 32 S6
21 S4 23 24 25 26 27 28 29 30
20 19 E1 S1 16 15 14 13 S2 11
01 02 E1 04 05 E2 07 08 09 10
"""
    return tablero

def movimiento_dado(posicion: int) -> list:
    dado: int = random.randint(1, 6)
    #print("\ndado:", dado)
    posicion_mas_dado = [dado, posicion]
    posicion_mas_dado[0] = dado
    posicion_mas_dado[1] = posicion + dado
    return posicion_mas_dado

def contadores_casilleros(jugador1: list, jugador2: list, contadores: dict, casilleros_banana: dict, casilleros_magico: dict, casillero_rushero: dict, casillero_hongo: dict) -> dict:
    if jugador1 in ESCALERA or jugador2 in ESCALERA:
        contadores["contador_escaleras"] = contadores["contador_escaleras"] + 1
    elif jugador1 in SERPIENTE or jugador2 in SERPIENTE:
        contadores["contador_serpientes"] = contadores["contador_serpientes"] + 1
    elif jugador1 in casilleros_banana or jugador2 in casilleros_banana:
        contadores["contador_bananas"] = contadores["contador_bananas"] + 1
    elif jugador1 in casilleros_magico or jugador2 in casilleros_magico:
        contadores["contador_magicos"] = contadores["contador_magicos"] + 1
    elif jugador1 in casillero_rushero or jugador2 in casillero_rushero:
        contadores["contador_rusheros"] = contadores["contador_rusheros"] + 1
    elif jugador1 in casillero_hongo or jugador2 in casillero_hongo:
        contadores["contador_hongos"] = contadores["contador_hongos"] + 1
    return contadores

def movimiento(posicion_mas_dado: list, casilleros_banana: dict, casilleros_magico: dict, casillero_rushero: dict, casillero_hongos: dict) -> int:
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
        casilleros_magico[movimiento] = random.randint(2,99)
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

def jugadores(jugador1: int, nombrej1, jugador2: int, nombrej2, casillero_bananas, casillero_magicos, casillero_rushers, casillero_hongo, tablero, random) -> list:
    if random == 1:
        jugadores = [jugador1[1], jugador2[1]]
        print("\ndado:", jugador1[0])
        jugador1 = movimiento(jugador1[1], casillero_bananas, casillero_magicos, casillero_rushers, casillero_hongo)
        jugador1 = movimiento(jugador1, casillero_bananas, casillero_magicos, casillero_rushers, casillero_hongo)
        jugadores[0] = jugador1
        tablero = cambio_tablero(jugador1, tablero, "J1")
        print(tablero)
        print("el jugador 1", nombrej1, "se encuentra en el casillero numero", jugador1)
        input("ingrese Enter para tirar los dados\n")
        if jugador1 >= 100:
            print("         |Ganador Jugador 1|")
            trofeo()
        print("\ndado:", jugador2[0])
        jugador2 = movimiento(jugador2[1], casillero_bananas, casillero_magicos, casillero_rushers, casillero_hongo)
        jugador2 = movimiento(jugador2, casillero_bananas, casillero_magicos, casillero_rushers, casillero_hongo)
        jugadores[1] = jugador2
        tablero = cambio_tablero(jugador2, tablero, "J2")
        print(tablero)
        print("el jugador 2", nombrej2, "se encuentra en el casillero numero", jugador2)
        input("ingrese Enter para tirar los dados\n")
        if jugador2 >= 100:
            print("         |Ganador Jugador 2|")
            trofeo()
    else:
        jugadores = [jugador1, jugador2]
        print("\ndado:", jugador2[0])
        jugador2 = movimiento(jugador2[1], casillero_bananas, casillero_magicos, casillero_rushers, casillero_hongo)
        jugador2 = movimiento(jugador2, casillero_bananas, casillero_magicos, casillero_rushers, casillero_hongo)
        jugadores[1] = jugador2
        tablero = cambio_tablero(jugador2, tablero, "J2")
        print(tablero)
        print("el jugador 2", nombrej2, "se encuentra en el casillero numero", jugador2)
        input("ingrese Enter para tirar los dados\n")
        if jugador2 >= 100:
            print("         |Ganador Jugador 2|")
            trofeo()
        print("\ndado:", jugador1[0])
        jugador1 = movimiento(jugador1[1], casillero_bananas, casillero_magicos, casillero_rushers, casillero_hongo)
        jugador1 = movimiento(jugador1, casillero_bananas, casillero_magicos, casillero_rushers, casillero_hongo)
        jugadores[0] = jugador1
        tablero = cambio_tablero(jugador1, tablero, "J1")
        print(tablero)
        print("el jugador 1", nombrej1, "se encuentra en el casillero numero", jugador1)
        input("ingrese Enter para tirar los dados\n")
        if jugador1 >= 100:
            print("         |Ganador Jugador 1|")
            trofeo()
    return jugadores

def cambio_tablero(posicion: int, tablero: str, jugador: str) -> str:
    if posicion < 10:
        jugadorstr = str(posicion)
        jugadorstr = "0" + jugadorstr
    else:
        jugadorstr = str(posicion)
    tablero = tablero.replace(jugadorstr, jugador)
    return tablero

def trofeo() -> str:
    print("""
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
                """)

def main() -> None:
    jugador1: int = 0
    jugador2: int = 0
    contadores: dict = {"contador_escaleras": 0, "contador_serpientes": 0, "contador_bananas": 0, "contador_magicos": 0, "contador_rusheros": 0, "contador_hongos": 0}
    casilleros_ocupados = list(ESCALERA.keys()) + list(ESCALERA.values()) + list(SERPIENTE.keys()) + list(SERPIENTE.values())
    casillero_bananas: dict = generador_casillero_banana(casilleros_ocupados)
    casilleros_ocupados = casilleros_ocupados + list(casillero_bananas.keys()) + list(casillero_bananas.values())
    casillero_magicos: dict = generador_casillero_magico(casilleros_ocupados)
    casilleros_ocupados = casilleros_ocupados + list(casillero_magicos.keys())
    casillero_rushers: dict = generador_casillero_rushero(casilleros_ocupados)
    casilleros_ocupados = casilleros_ocupados + list(casillero_rushers.keys()) + list(casillero_rushers.values())
    casillero_hongo: dict = generador_casillero_hongos(casilleros_ocupados)
    mostrar_opciones()
    tablero = tablero_base()
    opcion: str = str(input("-> "))
    while opcion != "4":
        if opcion == "1":
            nombre_j1: str = str(input("ingrese el nombre del jugador 1\n-> "))
            nombre_j2: str = str(input("ingrese el nombre del jugador 2\n-> "))
            empieza = random.randint(1,2)
            print("\nCasilleros\nSerpientes ->", SERPIENTE, "\nEscaleras ->", ESCALERA,"\nBananas ->", casillero_bananas, "\nMagicos ->", casillero_magicos, "\nRushero ->", casillero_rushers, "\nHongo loco ->", casillero_hongo)
            input("\nPresione la tecla Enter para continuar")
            while jugador1 < 100 and jugador2 < 100:
                jugador1_mas_dado = movimiento_dado(jugador1)
                jugador2_mas_dado = movimiento_dado(jugador2)
                contadores = contadores_casilleros(jugador1_mas_dado[1], jugador2_mas_dado[1], contadores, casillero_bananas, casillero_magicos, casillero_rushers, casillero_hongo)
                movimientos = jugadores(jugador1_mas_dado, nombre_j1, jugador2_mas_dado, nombre_j2, casillero_bananas, casillero_magicos, casillero_rushers, casillero_hongo, tablero, empieza)
                jugador1 = movimientos[0]
                jugador2 = movimientos[1]
                tablero = tablero_base()
            jugador1 = 0
            jugador2 = 0
        elif opcion == "2":
            if sum(contadores.values()) == 0:
                print("\nNo hay estadisticas")
            else:
                print("\nLas estadisticas de cuanto se han activado los casilleros son\nEscaleras:", contadores["contador_escaleras"],"\nSerpientes:", contadores["contador_serpientes"],"\nBananas:", contadores["contador_bananas"],"\nMagicos:", contadores["contador_magicos"],"\nRusheros:", contadores["contador_rusheros"],"\nHongos:", contadores["contador_hongos"])
        elif opcion == "3":
            contadores= {"contador_escaleras": 0, "contador_serpientes": 0, "contador_bananas": 0, "contador_magicos": 0, "contador_rusheros": 0, "contador_hongos": 0}
            print("\nLas estadisticas se han reiniciado")
        opcion = str(input("\n1 Iniciar Partida\n2 Mostrar Estadisticas\n3 Resetear Estadisticas\n4 Salir\n-> "))
    print("\nHasta luego!")
main()

"""
arreglar el print del dado (devolver lista en funcion de los dados)
"""