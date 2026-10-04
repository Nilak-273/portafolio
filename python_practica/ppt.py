import random

opciones = ["piedra", "papel", "tijera"]

while True:
    usuario = input("Escoge piedra, papel o tijera: ").lower()
    if usuario in opciones:
        break          
    else:
         print("Opción invalida")
maquina = random.choice(opciones)

print("maquiná: ", maquina,"\nusuario: ", usuario)

if usuario == maquina:
    print("empate")
elif usuario == "piedra" and maquina == "papel" or usuario == "papel" and maquina == "tijera" or usuario == "tijera" and maquina == "piedra":
    print("Gana la maquiná!") 
else:
    print("Has ganado!")
