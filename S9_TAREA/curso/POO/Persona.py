class Personas():
    # Propiedades,Caracteristicas o atributos:
    apellidos= ""
    nombres= ""
    edad = 0
    despierta = False
    
    #funcionalidades:
    def despertar(self):
        #self: Parametro que hace referencia a la instancia perteneciente a la clase
        self.despeierta = True
        print("Buen dia.")
    