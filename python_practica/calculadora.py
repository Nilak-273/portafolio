#CALCULADORA
print("ELIGE UNA OPERACIÓN")
print("1. suma")
print("2. resta")
print("3. multiplicar")
print("4. Dividir")

numero_1 = float(input("Elige el primer número: "))
numero_2 = float(input("Elige el segundo número: "))

operacion = input("elige una operación: ")

if operacion == "1":
    print("Resultado:", numero_1 + numero_2)

elif operacion == "2":
    print("Resultado:", numero_1 - numero_2)

elif operacion == "3":
    print("Resultado:", numero_1 * numero_2)

elif operacion == "4":
    print("Resultado:", numero_1 / numero_2)

else: 
    print("Escoge una opción válida")