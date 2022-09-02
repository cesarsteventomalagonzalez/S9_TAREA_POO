class Pais():
    def __init__(self,nom,pre):
        self.nombre=nom
        self.presidente=pre
        
    def __str__(self):
        text="Pais: {0} - Presidente: {1}"
        return text.format(self.nombre,self.presidente)
class Ciudad():
    def __init__(self,nom,hab,pai):
        self.nombre=nom
        self.habitantes=hab
        self.pais=pai
        
    def __str__(self):
        text="Ciudad: {0} - N' Habitantes: {1}({2})"
        return text.format(self.nombre,self.habitantes,self.pais)

class Urbanizacion():
    def __init__(self, nom, ciu):        
        self.nombre = nom
        self.ciudad = ciu
        
    def __str__(self):
        text="Urbanizacion: {0} - ({1})"
        return text.format(self.nombre,self.ciudad)
        
        
        
        
        
        
pais1=Pais("Ecuador","Guillermo Lasso")
print(pais1)

ciudad1 =Ciudad("Milagro",22000,pais1)
print(ciudad1)

urba1=Urbanizacion("Los Helechos",ciudad1)
print(urba1)