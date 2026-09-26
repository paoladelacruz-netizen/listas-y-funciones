notas = (13,15,18,19,20,14,17,16,18,12,14,13)
def ver_datos(notas):
    cantidad = len(notas)
    suma = sum(notas)
    promedio = suma /cantidad

    mayor = max (notas)
    menor = min (notas)

    return cantidad,suma,promedio,mayor,menor 

cantidad,suma,promedio,mayor,menor = ver_datos(notas)

print("Nota mas alta: ", mayor)
print("Nota mas baja: ", menor)
print("Promedio de notas: ",promedio)