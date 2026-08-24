#CONTADOR DE FRASES
frase = input("escribe una frases: ")
print("La frase tiene " + str(len(frase.split())) + " palabras")

conteo = {}

for palabra in frase.split():
    #print(palabra)
    if palabra in conteo:
        conteo[palabra] = conteo[palabra] + 1
    else: conteo[palabra] = 1
    
print(conteo)

for palabra, veces in conteo.items():
    print(palabra, veces)
