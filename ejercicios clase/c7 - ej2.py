"""Escribir un programa que permita desencriptar un texto dado.
El encriptado del código es el siguiente
El mensaje está escrito cada 3 caracteres comenzando por el tercero.
Cada número corresponde a una vocal (1=a,2=e,3=i,4=o,5=u)
Los espacios se representan con “&”
Texto="avFfe2rtlty3cvchg3yutui1olcpi3bv4qwnef2zxsza,zc&cvdjy4uimkm3lindg1qcnxa&wesxatqhrjr3xcnumgaqs"""

texto = "avFfe2rtlty3cvchg3yutui1olcpi3bv4qwnef2zxsza,zc&cvdjy4uimkm3lindg1qcnxa&wesxatqhrjr3xcnumgaqs"

textonuevo = texto.replace("&"," ")
textonuevo = textonuevo.replace("1","a")
textonuevo = textonuevo.replace("2","e")
textonuevo = textonuevo.replace("3","i")
textonuevo = textonuevo.replace("4","o")
textonuevo = textonuevo.replace("5","u")

print(texto)
print(textonuevo[2::3])