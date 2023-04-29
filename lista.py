#[] -> listas
#() -> 
#{} ->

listaEstudiantes=["Iris", "Robert", "Miguel","Richard","Laura"]

print("Imprimir un elemento de la lista, debo colocar el index")
print("El estudiante de la posicion 2 es: " , listaEstudiantes[2])

print("listado de estudiantes", listaEstudiantes)


print("Agregar un elemento al final de la lista")

listaEstudiantes.append("santiago")
print("listado de estudiantes", listaEstudiantes)

listaEstudiantes.insert(1,"sebastian")
print("listado de estudiantes", listaEstudiantes)

print("El cantidad de la lista es: ", len (listaEstudiantes))
print ("En la ultima posicion se encuentra ", listaEstudiantes[-1])#forma 1
print ("En la ultima posicion se encuentra ", listaEstudiantes[len(listaEstudiantes)-1])#forma 2

listaEstudiantes[1]="valeria"
print("listado de estudiantes", listaEstudiantes)
