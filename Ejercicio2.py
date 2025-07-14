# Solicita los números (usamos float para que podamos pasar numeros decimales con ".") y el operador
numero1 = float(input("Introduce el primer número (para decimales usar .): "))
numero2 = float(input("Introduce el segundo número (para decimales usar .): "))
operador = input("Introduce el operador (+, -, *, /): ")

# Usa match-case para seleccionar la operación
match operador:
    case "+":
        resultado = numero1 + numero2
    case "-":
        resultado = numero1 - numero2
    case "*":
        resultado = numero1 * numero2
    case "/":
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            resultado = "Error: División por cero"
    case _:
        resultado = "Operador no válido"

# Muestra el resultado
print("Resultado:", resultado)
