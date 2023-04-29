#Estudiante ={
 #   "Nombre": "Iris Gongora",
  #  "Edad": 20,
   # "Programa": "Desarrollo de software",
    #"Nota": 4.7
    
  
    
#}
#print("Elemento del diccionario")
#print(Estudiante)

#print("Nombre ",Estudiante["Nombre"])

listaEstudiantes={}

listaEstudiantes["valeria"]=4.1
listaEstudiantes["Laura"]=5
listaEstudiantes["richard"]=4


for nombre, nota in listaEstudiantes.items():
    print(nombre,"Tiene una nota de ", nota)


