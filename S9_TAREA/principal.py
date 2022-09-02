from Menu import principal
from curso.modulos.funcionesMatematicas import sumar,multi
from curso.POO.Persona import Personas
from curso.POO.curso import Curso
from curso.POO.cuenta import Cuenta
from curso.POO.herencia import *
from curso.POO.herenciaMultiple import *
from curso.POO.Polimorfismo import *
from curso.POO.DependenciaClases import *
from Paquete1.funcionesCadena import contarLetras
from Paquete1.funcionesOperaciones import *
import time
import os
os.system("cls")
var = principal()
lis = ["1)Vid_3","2)Vid_4","3)Vid_5","4)Vid_6","5)Vid_7","6)Vid_8","7)Vid_9","8)Vid_10","9)Vid_11","10)Vid_12","11)Vid_13","12)Vid_14","13)Vid_15","14)Vid_16","15)Vid_17","16)Vid_18","17)Vid_19","18)Vid_20","19)Vid_21","20)Vid_22","21)Vid_23","22)Vid_24","23)Vid_25","24)Vid_26","25)Vid_27","26)Vid_28","27)Vid_29","28)Vid_30","29)Vid_31","30)Vid_32","31)Vid_33","32)Vid_34","35)Vid_37","36)Vid_38","37)Vid_39","38)Vid_40","39)Salir"]
opcion = ""
while opcion != "39":
    os.system("cls")
    opcion = var.menu(lis)
    if opcion == "1":
        os.system("cls")
        print("Hola Mundo")
        time.sleep(1)
    elif opcion =="2":
        os.system("cls")
        variable = "César Tomalá"
        print(variable)
        edad = 20
        print(edad)
        edad = True
        print(edad)
        sueldo = 1,350
        print(sueldo)
        time.sleep(1)
    elif opcion == "3":
        os.system("cls")
        numero1 = "35"
        numero2 = "10"
        print (numero1+numero2)
        
        num1 = int(numero1)
        num2 = int(numero2)
        print(num1+num2)
        
        sueldo = 1200.43
        sueldoEntero = int(sueldo)
        print(sueldoEntero)
        
        valor = "4500.00"
        valorDecimal = float(valor)
        print(valorDecimal *3)
        
        edad = 100
        print(len(str(edad)))
        time.sleep(1)
    elif opcion == "4":
        os.system("cls")
        entero = 23
        decimal = 31.76
        complejo = 12 + 5j
        booleano = True
        """print(entero)
        print(decimal)
        print(complejo)
        print(booleano)
        """
        num1=20
        num2=4
        
        print("suma:", (num1 + num2))
        print("resta:", (num1 - num2))
        print("multiplicacion:", (num1 * num2))
        print("division:", (num1 / num2)) 
        print("Division Exacta:", (num1 // num2))
        print("Potencia:",(num1 ** num2)) 
        time.sleep(1)
    elif opcion == "5":
        os.system("cls")
        texto1="Hola"
        texto2="Mundo"
        textoFinal = texto1 + " " +texto2
        print(textoFinal)

        print("El saludo es: %s %s " %(texto1, texto2))
        saludoFinal = "Saludo: {0} {1}".format(texto1,texto2)
        print(saludoFinal)
        saludoFinal2 = "Saludo: {x} {y}".format(x=texto1,y=texto2)
        print(saludoFinal2)
        time.sleep(1)
    elif opcion == "6":
        os.system("cls")
        texto = "Bienvenido al canal UskoKruM2010"
        print(texto)
        print(texto.lower())
        print(texto.upper())
        print(texto.title())
        print(texto.find("al"))
        print(texto.count("e"))
        textoFinal= texto.replace("e","3")
        print(textoFinal)
        valor = texto.isnumeric()
        print(valor)
        cadenaSeparada = texto.split(" ")
        print(cadenaSeparada)
        time.sleep(1)
    elif opcion == "7":
        os.system("cls")
        tupla=(1,2,3)
        print(tupla)
        tupla2=(7,"oscar",True,450.1,16+7j,15,"felicidades",False)
        print(tupla2)
        tupla3=(9,3,(4,5,6))
        print(tupla3)
        print(tupla2[1])
        print(tupla2[-1])
        print(tupla2[0:4])
        print(tupla2[-2])
        a,b,c=tupla
        print(a)
        print(b)
        print(c)

        tuplaFinal = tupla + tupla3
        print(tuplaFinal)
        print(tuplaFinal.count(3))
        print(tuplaFinal.index(3))
        time.sleep(1)
    elif opcion == "8":
        os.system("cls")
        lista1 = ['oscar',25,98.3,True,"flavio",56.3]
        print(lista1)
        print(lista1[:])
        print(lista1[2])
        print(lista1[-2])
        print(lista1[0:3])
        print(lista1[:2])
        print(lista1[3:])    
        
        lista1.append("UskoKruM2010")
        print(lista1)
        lista1.insert(4,"Peru")
        print(lista1)

        lista1.extend(["alejandro",110,False])
        print(lista1)

        lista1.index("flavio")
        print(lista1)

        lista1.remove(56.3)
        print(lista1)
        lista1.pop()
        print(lista1)

        lista2 = ["Chiclayo","Irna"]
        lista3 = lista1 + lista2
        print(lista3)

        print(lista2 *4)
        print("UskoKruM2010" in lista1)  
        time.sleep(1) 
    elif opcion == "9":
        os.system("cls")
        miDicionario = {"España":"Madrid", "Perú":"Lima","Alemania":"Berlin"}
        print(miDicionario["Perú"])
        print(miDicionario)

        miDicionario["Venezuela"] = "Caracas"
        print(miDicionario)

        miDicionario["España"] = "Barcelona"
        print(miDicionario)
        
        del miDicionario["España"]
        print(miDicionario)

        dic2 = {"Garcia":"Oscar", 25: True, "Sueldo":150.80}
        print(dic2[25])

        llaves = ("España","Francia","Inglaterra")
        dicPaises = {llaves[0]:"Madrid",llaves[1]:"Paris",      llaves[2]:"Londres"}
        print(dicPaises)

        datosPersonales = {"Ape":"Garcia","Anios":{1:2010,      2:2011,3:2012,4:2013,5:2014}}
        print(datosPersonales)
        print(datosPersonales["Anios"])

        print(datosPersonales.get('Ape',"Oscar"))
        print(datosPersonales.keys())
        valores=list(datosPersonales.values())
        print(valores)
        time.sleep(1)
    elif opcion == "10":
        os.system("cls")
        nombre=input("Ingrese el nombre: ")
        edad=int(input("Ingrese su edad: "))
        sueldo=float(input("Ingrese su sueldo: "))
        print("Hola,"+nombre)
        edadFutura = edad + 20 
        print("tu edad es:", edad)
        print("tu edad futura (dentro de 20 años sera):", edadFutura)
        print("Su sueldo es de:",sueldo)
        time.sleep(1)
    elif opcion == "11":
        os.system("cls")
        edad = int(input("Ingrese su edad: "))
        if edad >=18:
            print("Eres mayor de edad")
        elif edad == 18:
            print("Tienes 18 años")
        else:
            print("Eres menor de edad")        
        time.sleep(1)
    elif opcion == "12":
        os.system("cls")
        def saludar():
            print("Tomalá")
            print("Cesar")
            print("Hola a todos")
            return "hola"
        print(saludar())
        
        def evaluarSueldoMinimo(sueldo):
            if sueldo >= 850:
                print("Cumple con el sueldo")
            else:
                print("Ganas menos del sueldo minimo")
        
        evaluarSueldoMinimo(1100)
        time.sleep(1)
    
    elif opcion == "13":
        os.system("cls")
        distancia = 400
        numeroHermanos = 3
        salarioPadres = 3000
        
        tieneBeneficio = False
        
        if (distancia > 1000 and numeroHermanos >2) or salarioPadres < 2000:
            tieneBeneficio = True
        print(not tieneBeneficio)
         
        if (5>3) and (8<15):
            print("verdad")   
        else:
            print("Es mentira...")
        time.sleep(1)
    
    elif opcion == "14":
        os.system("cls")
        sexos = ("Hombre", "Mujer")
        posicion = True
        sexo = sexos[posicion] #Mujer
        print(sexo)
        sexo = sexos[not posicion] #Hombre
        print(sexo)
        time.sleep(1)
    elif opcion == "15":
        os.system("cls")
        print("--- Cursos ---")
        print("Matematica - Biología - Lenguaje - Ciencias")
        curso = input("Ingrese el Curso deseado: ")
        if curso in ("Matematica","Biología","Lenguaje","Ciencias"):
            print("Curso {0} selecionado.".format(curso))
        else:
            print("No existe el Curso")
        time.sleep(1)
    elif opcion == "16":
        os.system("cls")
        numeros = range(5)
        print(numeros[1])
        numeros1 = range(4,10)
        print(numeros1[5])
        numeros2 = range(10,110, 8)
        print(numeros2[9]) 
        time.sleep(1)
    elif opcion == "17":
        os.system("cls")
        for i in range(1,13):
            print("{0} x {1} es: {2}".format(i,i, (i*i)))
        
        for nom in ["Karen", "Oscar","Hector","Leonardo"]:
            print("Cantidad de letras de {0} es: {1}".format(nom, len(nom))) 
        time.sleep(1)
    elif opcion == "18":
        os.system("cls")
        numero=int(input("Ingrese un numero: "))
        factorial=1
        for n in range(1,(numero+ 1)):
            factorial = factorial * n
        print ("El factorial de {0} es: {1}".format(numero,factorial))
        time.sleep(1)
    elif opcion == "19":
        os.system("cls")
        """indice = 1
        
        while indice < 10:
            print("Valor actual {0}".format(indice))
            indice = indice + 1
        print("Hemos terminado el bucle while")"""
        
        inicio = 2
        while inicio <= 100:
            print("Numero par: {0}". format(inicio))
            inicio += 2
        print("Hemos terminado el bucle while") 
        time.sleep(1)            
    elif opcion == "20":
        os.system("cls")
        """for numero in range(1,6):
            if numero == 3:
                break
            print("El numero es: {0}". format(numero))
        print("Bucle terminado.")"""
        """for numero in range(1,6):
            if numero == 3:
                continue
            print("El numero es: {0}". format(numero))
        print("Bucle terminado.")"""
        for numero in range(1,6):
            if numero <= 3:
                pass
            else:
                print("El siguiente valor es mayor a 3:")
            print("El numero es:{0}".format(numero))
        print("Bucle terminado.") 
        
        time.sleep(1)
    elif opcion == "21":
        os.system("cls")
        # Generadores :Permite extraer valores de la función y almacernarlo
        # (de uno en uno) en objetos iterables (que se pueden recorrer),
        # sin la necesidad de almacenar TODOS A LA VEZ en la memoria RAM.
        """
        def generaMultiplos7(limite):
            numero=1
            listaNumeros = []
            
            while numero <= limite:
                listaNumeros.append(numero*7)
                numero = numero + 1
            return listaNumeros 
        
        print(generaMultiplos7(10))
        time.sleep(1)"""
        def generaMultiplos7(limite):
            numero=1   
            while numero <= limite:
                yield numero * 7 #ceder. genera un objeto iterable
                numero = numero + 1
        obtieneMultiplo7= generaMultiplos7(10)
        #print(obtieneMultiplo7)
        """for n in obtieneMultiplo7:
            print(n)"""
        #next(): retorna el siguiente elemento de un objeto interable:
        print(next(obtieneMultiplo7))
        print("Aca hay 300 lineas de código...")
        print(next(obtieneMultiplo7))
        print("Aca hay 300 lineas de código...")
        # son mas eficiente que las funciones tradicionales.
        # Muy útiles son listas de valores infinitos.
        time.sleep(1)        
    elif opcion == "22":
        os.system("cls")
        #Cuando indicamos un * adelante del parametro de una funcion,
        # estamos indicando que se va a recibir un número indeterminado
        # de parametros, y estos se recibiran en forma de tupla
        """def devuelveLenguajes(*lenguajes):
            for leng in lenguajes:
                yield leng"""
        def devuelveLenguajes(*lenguajes):
            for leng in lenguajes:
                yield from leng
        lenguajesObtenidos=devuelveLenguajes("Python","Java","PHP","Ruby","JavaScript")
        print(next(lenguajesObtenidos))
        print(next(lenguajesObtenidos))
        time.sleep(1)
    elif opcion == "23":
        os.system("cls")
        #Exepcion: error en tiempo de ejecucion (durante la ejecucion de un programa)
        numero1=20
        numero2= 2
        #print("La división de {0} entre {1} es: ".format(numero1,numero2,(numero1/numero2)))
        try:
            resultado = numero1/numero2
        #except:
        except ZeroDivisionError:
            print("No se puede dividir entre 0...")
        finally:
            print("Yo siempre aparezco")
        print("Aqui termina el programa.")
        time.sleep(1)
    elif opcion == "24":
        os.system("cls")
        #Raise: Sirve para ejecutar exepciones en Python.
        def evaluarNota(nota):
            if nota <0:
                #raise ZeroDivisionError("Este mensaje es personalizado")
                raise ValueError("Valor incorrecto...")
            elif nota >=16:
                print("Excelente")
            elif nota >= 11:
                print ("Aprobado")
            else:
                print("Desaprobado")
        evaluarNota(1)
        print("Este el fin del programa")
        time.sleep(1)
    elif opcion == "25":
        os.system("cls")
        print("La operacion suma importada del modulo es: ",sumar(5,6))
        print("La operacion multiplicacion importada del modulo es: ",multi(5,5))
        time.sleep(1)
    elif opcion == "26":
        os.system("cls")
        #Los paquetes: sirve para almacenar modulos relacionados entre si.
        #A la vez organiza el codigo para luego poder reutilizar mejor el codigo
        #Lo que hace un __init_.py es covertir en directorio para luego poder importarlo.
        print("La operacion importada del modulo es:",multiplicar(5,6))
        print("La operacion importada del modulo es:",potencia(5,6))
        print("La operacion importada del modulo es:",contarLetras("Cesar"))
        time.sleep(1)
    elif opcion == "27":
        os.system("cls")
        persona1 = Personas()
        persona1.apellidos = "Tomala Gonzalez"
        print(persona1.apellidos)
        persona1.despertar()
        print(persona1.despierta)
        persona2 = Personas()
        persona2.apellidos = "Gonzalez Tomala"
        print(persona2.apellidos)       
        time.sleep(1)
    elif opcion == "28":
        os.system("cls")
        curso1 = Curso("Matematica",5,"Ingenieria en Software")
        print(curso1.nombre,curso1.creditos,curso1.profesion)
        curso2 = Curso("Lenguaje",4,"Ingenieria en Civil")
        print(curso2.nombre,curso2.creditos,curso2.profesion)       
        time.sleep(1)
    elif opcion == "29":
        os.system("cls")
        curso1 = Curso("Matematica",5,"Ingenieria en Software")
        print(curso1.nombre,curso1.creditos,curso1.profesion)
        time.sleep(1)
    elif opcion == "30":
        os.system("cls")
        curso1 = Curso("Matematica",5,"Ingenieria en Software")
        curso1.mostrarDatos()   
        time.sleep(1)
    elif opcion == "31":
        os.system("cls")
        cuenta1=Cuenta("César",245.55,"dolares")
        print(cuenta1.get_saldo())
        print(cuenta1.get_moneda())
        cuenta1.set_moneda("Bolivares")
        print(cuenta1.get_moneda())
        time.sleep(1)
    elif opcion == "32":
        os.system("cls")
        curso1 = Curso("Matematica",5,"Ingenieria en Software")
        print(curso1.nombre,curso1.creditos,curso1.profesion)
        curso1.mostrarDatos()
        print(curso1)   
        time.sleep(1)
    elif opcion == "33":
        os.system("cls")
        estu1=Estudiante("Tomala","Gonzalez","CesarSteven","Ingenieria en Software")
        print(estu1.mostrarNombreCompleto())
        print(estu1.profesion)
        time.sleep(1)
    elif opcion == "34":
        os.system("cls")
        estu1=Estudiante("Tomala","Gonzalez","CesarSteven","Ingenieria en Software")
        estu1.datos()
        time.sleep(1)
    elif opcion == "35":
        os.system("cls")
        estu1=Persona("Tomala","Gonzalez","CesarSteven")
        print(isinstance(estu1,Estudiante))
        time.sleep(1)
    elif opcion == "36":
        os.system("cls")
        cX1 = ClaseX(15,21)
        print(cX1)
        time.sleep(1)
    elif opcion == "37":
        os.system("cls")
        doc1=Trabajador()
        describirPersona(doc1)    
        time.sleep(1)
    elif opcion == "38":
        os.system("cls")
        pais1=Pais("Ecuador","Guillermo Lasso")
        print(pais1)

        ciudad1 =Ciudad("Milagro",22000,pais1)
        print(ciudad1)

        urba1=Urbanizacion("Los Helechos",ciudad1)
        print(urba1)
        time.sleep(1)
    elif opcion == "39":
        os.system("cls")
print("Gracias por usar el Programa...")
    
          
        
        
    
        
        