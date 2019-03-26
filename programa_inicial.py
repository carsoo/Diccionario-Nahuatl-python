# -*- coding: utf-8 -*-
import mechanize
from conectar_webapp import conectarWebApp

print("--"*24)
print("<>"*24)
print("Bienvenido al Diccionario Náhuatl")
print("<>"*24)
print("--"*24)
print("Codeado por: https://github.com/carsoo")
print("Aulex.org")
print("Vocabulario compilado por Manuel Rodríguez Villegas\n")

def busqueda_palabra():
    try:
        palabra = str(raw_input("Escribe la palabra que deseas traducir a Náhuatl: "))
        conectarWebApp(palabra)
    except:
        print("Hubo un error al iniciar el programa")
busqueda_palabra()

while True:
    try:
        nueva_palabra = int(raw_input(("¿Quieres Buscar otra Palabra? \n Ingresa 1 para SI \n Ingresa 0 para NO\n")))
        if nueva_palabra == 1:
            busqueda_palabra()
        elif nueva_palabra == 0:
            print("--" * 12)
            print("<>"*12)
            print("\tAdiós")
            print("<>"*12)
            print("--" *12)
            break
    except ValueError:
            print("¡¡¡ INTENTA DENUEVO !!!")



