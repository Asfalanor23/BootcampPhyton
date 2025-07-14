#Usamos el bucle while para que programa siga ejecutando 
#hasta que el usuario introduzca un valor correcto

while True:
    #Se usa float para que se puedan introducir valores decimales
    entrada = input("Introduce un número: ")

    try:
        numero = float(entrada)
        if numero % 2 == 0:
            print(f"{numero} es múltiplo de 2.")
        else:
            print(f"{numero} no es múltiplo de 2.")
        break  # Salimos del bucle si todo ha ido bien
    except ValueError:
        print("Error: No has introducido un número válido. Intenta otra vez.")
