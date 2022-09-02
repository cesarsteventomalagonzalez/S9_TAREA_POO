class Curso():
    """nombre = "Matematica"
    creditos = 5
    profesion = "Ingenieria Civil" """
    #estado inicial del objeto:
    def __init__(self,nom,cre,pro):
        self.nombre = nom
        self.creditos = cre
        self.profesion= pro
        self.__imparticion = "Presencial" #Propiedad encapsulada
    
    def mostrarDatos (self):
        dat="Nombre: {0} / Creditos:{1} / Modo de imparticion: {2}"
        print(dat.format(self.nombre,self.creditos,self.__imparticion))  
        docenteAsigando=self.__verificarDocente()
        if docenteAsigando:
            print("Existe docente asigando")
        else:
            print("No es necesario asignar un docente")
    
    def __verificarDocente(self):
        #print("Verificando si existe docente asigando...")
        if self.__imparticion == "Presencial":
            return True
        else:
            return False
    
    def __str__(self):
        texto="Nombre: {0} - créditos : {1}"
        return texto.format(self.nombre,self.creditos)   
        
        
        

curso1 = Curso("Matematica",5,"Ingenieria en Software")
print(curso1.nombre,curso1.creditos,curso1.profesion)
curso1.mostrarDatos()
print(curso1)


# curso2 = Curso("Lenguaje",4,"Ingenieria en Civil")
# print(curso2.nombre)
    