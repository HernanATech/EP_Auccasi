# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:27:19 2024

@author: Alumno
"""

       
def leer_datos_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, "rt", encoding='utf8') as archivo:
            return archivo.read().strip()
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {ruta_archivo}")
        return None

def validar_credenciales(usuario, contraseña):
    usuario_correcto = leer_datos_archivo("login.txt")
    contraseña_correcta = leer_datos_archivo("clave.txt")
    
    if usuario_correcto and contraseña_correcta:
        return usuario == usuario_correcto and contraseña == contraseña_correcta
    else:
        return False

def login():
    intentos_maximos = 3
    intentos = 0
    
    while intentos < intentos_maximos:
        usuario = input('Ingrese el nombre de usuario: ')
        contraseña = input('Ingrese su contraseña: ')
        
        if validar_credenciales(usuario, contraseña):
            print("Logeado correctamente")
            return
        else:
            print("Credenciales incorrectas. Intente nuevamente.")
            intentos += 1
    
    print("Ha superado el número máximo de intentos. El sistema se cerrará.")
    quit()

# Llamada a la función de login
login()