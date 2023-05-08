#Aqui ponemos las librerias :D
import time
#Aqui hacemos la funcionalidad
#Priemro creamos una clase
class Persona:
    def __init__(self, name, age, profesion, dni):
        self.__name = name
        self.__age = age
        self.__profesion = profesion
        self.__dni = dni
    time.sleep(2)
#Aqui es la def es una estructura para reutilizar el codigo y pueda cambiar la informacion agregada en los "datos"
    def info(self):
        return f"Hola mi nombre es: {self.__name}\nMi edad es: {self.__age}\nEstudio la profesion de: {self.__profesion}\ny mi cedula es: {self.__dni}"
#Def para cambiar el nombre
    def changer_name(self, new_name):
        """Aqui cambiamos el nombre"""
        self.name = new_name
        print(f"El nuevo nombre de la persona es: {self.name}.")
#Def para cambiar la cedula 
    def changer_cc(self, new_dni):
        """Aqui se corrigue la cc por si quedo mal"""
        self.dni = new_dni
        print(f"El nuevo numero de Cedula es: {self.dni}.") 
#aqui podemos hacer otra funcion donde podemos saludar
    def saludar (self):
        """Aqui es poner de que estamos saludando"""
        self.saludar = True
        print(f"Hola yo {self.name}, \nTe esta saludando")
#Aqui hacemos una breve precentacion con este def
    def precentarse (self):
        """Presentacion"""
        self.precentarse = True
        print(datos.info())
#Aqui se ponen los datos que se va a utilizar para que se imprima con el "def info"
datos = Persona("Daniel Molina", "20", "Programador", "1234567")
#Aqui imprimimos lo que necesitamos para visualizar la estructura del info ya con los parametros 
print("================================================")
print(datos.info())
#Aqui es para modificar los parametros originales 
print("================================================")
#Aqui imprimimos el def presentarse
datos.precentarse()
time.sleep(2)
print("================================================")
#Aqui imprimimos los cambios hechos en def changer_name
datos.changer_name("\nCarlos Molina")
print("================================================")
#Aqui imprimimos los cambios de hechos en def changer_cc
datos.changer_cc ("\n987654")
print("================================================")
#Aqui inprimimos el def saludar
datos.saludar()
