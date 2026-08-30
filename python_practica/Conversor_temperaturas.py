#CONVERSOR DE TEMPERATURAS 
def celcius_a_fah(C):
    resultado = (C * 9/5 + 32)
    return resultado

def fah_a_celcius(F):
    resultado = ((F - 32) * 5/9)
    return resultado

def celcius_a_kelvin(C):
    resultado = (C + 273.15)
    return resultado

def kelvin_a_celcius(K):
    resultado = (K - 273.15)
    return resultado

def fah_a_kelvin(F):
    resultado = ((F - 32) * 5/9) + 273.15
    return resultado

def kelvin_a_fah(K):
    resultado = ((K - 273.15) * 9/5) + 32
    return resultado

#Menu de conversiones 
print("1. Celcius a Fah")
print("2. Fah a Celcius")
print("3. Celcius a Kelvin")
print("4. Kelvin a Celcius")
print("5. Fah a Kelvin")
print("6. Kelvin a Fah")

#opciones 
opcion = input("escoge una opcion: 1 / 2 / 3 / 4 / 5 / 6 ")

#logica 
if opcion == "1":
    valor = input("ingresa la temperatura en celcius: ")
    valor = float(valor)
    conversion = celcius_a_fah(valor)
    print("conversion:" + str(conversion))
elif opcion == "2":
    valor = input("ingresa la temperatura en Fahrenheit: ")
    valor = float(valor)
    conversion = fah_a_celcius(valor)
    print("conversion:" + str(conversion))
elif opcion == "3":
    valor = input("ingresa la temperatura en celcius: ")
    valor = float(valor)
    conversion = celcius_a_kelvin(valor)
    print("conversion:" + str(conversion))
elif opcion == "4":
    valor = input("ingresa la temperatura en Kelvin: ")
    valor = float(valor)
    conversion = kelvin_a_celcius(valor)
    print("conversion:" + str(conversion))
elif opcion == "5":
    valor = input("ingresa la temperatura en Fahrenheit: ")
    valor = float(valor)
    conversion = fah_a_kelvin(valor)
    print("conversion:" + str(conversion))
elif opcion == "6":
    valor = input("ingresa la temperatura en Kelvin: ")
    valor = float(valor)
    conversion = kelvin_a_fah(valor)
    print("conversion:" + str(conversion))
else:
    print("opcion no valida")