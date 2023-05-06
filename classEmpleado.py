class Empleado: #Clase
    def __init__(self, IdEmpleado, apellidos,nombres,area,salario):#Propiedades
        self.IdEmpleado = IdEmpleado 
        self.apellidos = apellidos
        self.nombres = nombres
        self.area = area
        self.salario = salario
         
    def imprimirDatos(self): # Metodos
        print("_________________________")
        print("   DATOS DEL EMPLEADO    ")
        print("_________________________")
        print(f"Cedula ---> {self.IdEmpleado}")
        print(f"Apellidos ---> {self.apellidos}")
        print(f"Nombre ---> {self.nombres}")
        print(f"Area ---> {self.area}")
        print(f"Salario ---> {self.salario}")
        
    def calcularSalario(self,nroHoras):
        vlrDia=self.salario / 30
        vlrHora=vlrDia / 8
        vlrSalario=nroHoras / vlrHora
        datos=[vlrDia,vlrHora,vlrSalario]
        return datos  #esta retornando una lista
    def imprimirColilla (self,datos):
        print("___________________")
        print("  COLILLA DE PAGO  ")
        print("___________________")
        print(f"Cedula ----> {self.IdEmpleado}")
        print(f"Apellidos--> {self.apellidos}")
        print(f"Nombre-----> {self.nombres}")
        print(f"Area-------> {self.area}")
        print(f"Salario----> {self.salario}")
        print(f"Valor Dia--> {datos[0]}")
        print(f"Valor Hora-> {datos[1]}")
        print(f"Neto pagar-> {datos[2]}")
        
        
        
        
if  __name__=="__main__":
    #crear un objeto empleado1 a partir de la clase Empleado
    #Instanciar el objeto, crearlo
    empleado1 = Empleado(123, "Moncada", "Señora Valeria", "TI",2800000)
    empleado1.imprimirDatos()
    datos = empleado1.calcularSalario(280)
    empleado1.imprimirColilla(datos)
    
    
    # empleado2 = Empleado(147, "Ospina", " Carlos", "Gerencia",4000000)
    # empleado2.imprimirDatos()



   
        
        

    