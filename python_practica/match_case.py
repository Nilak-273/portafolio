numero_1 = float(input("Primer número: "))
operacion = input("Operación (+, -, *, /): ")
numero_2 = float(input("Segundo número: "))

match operacion:
    case "+":
        print("Resultado:", numero_1 + numero_2)
    case "-":
        print("Resultado:", numero_1 - numero_2)
    case "*":
        print("Resultado:", numero_1 * numero_2)
    case "/":
        print("Resultado:", numero_1 / numero_2)
    case _:
        print("Operación no válida")