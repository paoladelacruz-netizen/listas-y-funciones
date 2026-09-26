calificaciones_estudiantes = [16, 17, 19, 20, 14, 18, 5]
print("Lista de calificaciones de los estudiantes : ")
for calificacion in calificaciones_estudiantes:
    print(calificacion)

calificaciones_estudiantes.append(15)
calificaciones_estudiantes.remove(5)
print("Lista de calificaciones actualizada:")
for calificacion in calificaciones_estudiantes:
    print(calificacion)