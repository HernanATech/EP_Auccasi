# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

archivo = open("login.txt","at")

contenido = "Eder"
archivo.write(contenido)
archivo.close()

archivo = open("clave.txt","at")

contenido = "123456789"
archivo.write(contenido)
archivo.close()

archivo = open("dni.txt","at")

contenido = "77048235\n92548461\n95465875\n21546548\n31154876\n31548754\n84513487\n87456854\n34587468\n54865271"
archivo.write(contenido)
archivo.close()

archivo = open("nombre.txt","at")

contenido = "Eder\nJuan\nCarlos\nPedro\nLuis\nMarco\nIssac\nManuel\nAngel\nLucas"
archivo.write(contenido)
archivo.close()

archivo = open("apellido.txt","at")

contenido = "Auccasi\nRodriguez\nGutierrez\nFernandez\nVentocilla\nTruebas\nTarrillo\nHuaman\nGomez\nNuñez"
archivo.write(contenido)
archivo.close()
