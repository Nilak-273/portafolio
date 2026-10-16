#Lista vacía donde se guardarán las notas
notas = []

#Pregunta cuántas notas se van a ingresar (int porque es un número entero)
cantidad_notas = int(input("¿Cuántas notas vas a ingresar? "))

#Repite una vez por cada nota
#numero_nota empieza en 0, por eso se le suma 1 al mostrarlo
for numero_nota in range(cantidad_notas):
    #float permite notas con decimales (ej. 3.5)
    nota = float(input(f"Ingresa la nota {numero_nota + 1}: "))
    #Guarda la nota en la lista
    notas.append(nota)

#sum() suma todas las notas y len() cuenta cuántas hay
promedio = sum(notas) / len(notas)

print(f"Tu promedio es {promedio}")

if promedio >= 3:
    print("Aprobado")
else:
    print("Desaprobado")