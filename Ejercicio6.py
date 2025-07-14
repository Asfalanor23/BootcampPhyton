#Como queremos que imprima cada medio segundo, necesitamos el modulo time
import time

for numero in range(2, 101, 2):  #El tercer valor (2) representa el incremento del bucle, para que avance de 2 en 2
    print(numero)
    time.sleep(0.5)  # pausa de 0.5 segundos entre impresiones
