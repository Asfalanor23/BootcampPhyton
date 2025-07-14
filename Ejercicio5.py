#Como queremos que imprima cada medio segundo, necesitamos el modulo time
import time

#El limite superior es excluyente, por lo que necesitamos poner 101 en lugar de 100
for numero in range(1, 101):
    print(numero)
    time.sleep(0.5)  # pausa de 0.5 segundos entre impresiones
