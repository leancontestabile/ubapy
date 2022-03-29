#Escribir un programa que permita cambiar todas las palabras que indique el usuario en un texto dado.
proximamodificacion : bool = False


texto : str = str(input("ingrese su texto "))

print(texto)

pregunta = str(input("desea modificar alguna palabra del texto? (si/no) "))

if pregunta == "si":
    palabra_a_modificar = str(input("que palabra desea modificar? "))
    palabra_modificada = str(input("por cual palabra la quiere reemplazar? "))
    textomodificado = texto.replace(palabra_a_modificar,palabra_modificada)
    print("este es su nuevo texto:", textomodificado)
    proximamodificacion = str(input("desea modificar alguna otra palabra del texto? "))
    if proximamodificacion == "si":
        proximamodificacion = True
    else:
        proximamodificacion = False

while proximamodificacion:
    palabra_a_modificar = str(input("que palabra desea modificar? "))
    palabra_modificada = str(input("por cual palabra la quiere reemplazar? "))
    textomodificado = textomodificado.replace(palabra_a_modificar,palabra_modificada)
    print("este es su nuevo texto:", textomodificado)
    proximamodificacion = str(input("desea modificar alguna otra palabra del texto? "))
    if proximamodificacion == "si":
        proximamodificacion = True
    else:
        proximamodificacion = False

print("hasta luego")