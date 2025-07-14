#Usamos el bucle while para que programa siga ejecutando 
#hasta que el usuario introduzca un valor correcto

while True:
    color = input("¿Cual es el color de la luz encendida?: ").lower()

    match color:
        case "verde":
            print("Usted puede pasar sin problema.")
            break
        case "amarillo":
            print("Usted puede pasar con dificultades.")
            break
        case "rojo":
            print("Usted no puede pasar bajo ningún concepto.")
            break
        case _:
            print("Error: El semáforo solo puede tener 3 colores. Por favor, intentelo de nuevo")
