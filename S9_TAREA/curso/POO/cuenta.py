class Cuenta():
    def __init__(self,pro,sal,mon):
        self.__Propietario = pro
        self.__saldo = sal
        self.__moneda=mon
    # getters (metodo get): sirve para leer o modifcar propiedades de una clase 
    def get_saldo (self):
        return self.__saldo
    def get_propietario(self):
        return self.__Propietario
    def get_moneda(self):
        return self.__moneda
    #setter (metodo set)
    def set_moneda(self,moneda):
        self.__moneda = moneda
        
        
        
        
        
cuenta1=Cuenta("César",245.55,"dolares")
print(cuenta1.get_saldo())
print(cuenta1.get_moneda())
cuenta1.set_moneda("Bolivares")
print(cuenta1.get_moneda())
