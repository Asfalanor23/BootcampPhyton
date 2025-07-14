#Como queremos que imprima cada medio segundo, necesitamos el modulo time
import time

for numero in range(1, 101):  # Recorre todos los números del 1 al 100
    if numero % 3 == 0:       # Comprueba si el número es divisible por 3
        print(numero)
        time.sleep(0.5)  # pausa de 0.5 segundos entre impresiones
