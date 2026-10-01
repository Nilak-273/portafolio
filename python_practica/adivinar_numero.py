import random
numero_secreto = random.randint(1, 100)
intentos = 0

while True: 
    intento = int(input("Ingresa un número entre 1 y 100: "))
    intentos += 1
    if intento > numero_secreto:
        print("El número es menor")
    elif intento < numero_secreto:
        print("El número es mayor")
    else:
        print("¡Has adivinado el número!","en", intentos, "intentos") 
        break    