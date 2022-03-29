#botellas -> verde | negro | rojo | azul | amarillo
#vasos -> negro | azul

import cv2
import os
import numpy as np

def deteccion_colores(imagen) -> str:
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    colores_rango = {
        "Verde": ([40, 100, 100], [75, 255, 255]),
        "Negro": ([0, 0, 0], [0, 0, 10]),
        "Rojo": ([161, 155, 84], [179, 255, 255]),
        "Azul": ([94, 80, 2], [126, 255, 255]),
        "Amarillo": ([25, 100, 100], [30, 255, 255])}
    for nombre_color, (lower, upper) in colores_rango.items():
        lower = np.array(lower)
        upper = np.array(upper)
        mask = cv2.inRange(hsv, lower, upper)
        resultado = cv2.bitwise_and(imagen, imagen, mask = mask)
        if mask.any():
            color = nombre_color
    return color

def contadores_carpeta(objeto: str, color: str, botellas: dict, vasos: dict) -> dict:
    if objeto == "botella":
        botellas[color] = botellas[color] + 1
    elif objeto == "vaso":
        try:
            vasos[color] = vasos[color] + 1
        except KeyError:
            pass
    return botellas, vasos

def imagenes_carpeta(carpeta, contador_botellas: dict, contador_vasos: dict):
    for filename in os.listdir(carpeta):
        img = cv2.imread(os.path.join(carpeta,filename))
        objeto = "vaso"
        color = deteccion_colores(img)
        print(color)
        contadores_carpeta(objeto, color, contador_botellas, contador_vasos)
        cv2.imshow("escaner", img)
        cv2.waitKey(0)

def cantidades_txt(contador_botellas: dict, contador_vasos: dict):
    with open("botellas.txt", "w") as b:
        for key, value in contador_botellas.items():
            b.write("%s %s\n" % (key, value))
    with open("vasos.txt", "w") as b:
        for key, value in contador_vasos.items():
            b.write("%s %s\n" % (key, value))

def main() -> None:
    contadores_botellas: dict = {"Verde": 0, "Negro": 0, "Rojo": 0, "Azul": 0, "Amarillo": 0}
    contadores_vasos: dict = {"Negro": 0, "Azul": 0}

    imagenes_carpeta("TP_Arch_config/Lote0001", contadores_botellas, contadores_vasos)
    cantidades_txt(contadores_botellas, contadores_vasos)
main()