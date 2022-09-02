class Persona():
    def __init__(self,apePat,apeMat,nom):
        self.apellidoPaterno= apePat
        self.apellidoMaterno=apeMat
        self.nombres=nom
    
    def mostrarNombreCompleto(self):
        txt="{0} {1},{2}"
        return txt.format(self.apellidoPaterno,self.apellidoMaterno,self.nombres)
        
    def datos(self):
        print(self.mostrarNombreCompleto())
        
    
    
    
class Estudiante(Persona):
    
    def __init__(self,apePat,apeMat,nom,pro):
        super().__init__(apePat,apeMat,nom)
        self.profesion=pro
        
    def datos(self):
        super().datos()
        print("Profesion: {0}".format(self.profesion))
        
        



# estu1=Estudiante("Tomala","Gonzalez","CesarSteven","Ingenieria en Software")
estu1=Persona("Tomala","Gonzalez","CesarSteven")
# print(estu1.mostrarNombreCompleto())
# print(estu1.profesion)
# estu1.datos()

print(isinstance(estu1,Estudiante))
#Un estudiante siempre una persona, pero una persona no siempre es un estudiante.