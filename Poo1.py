#Aqui ponemos las librerias :D
import time
#Aqui hacemos la funcionalidad
#Priemro creamos una clase
class Persona:
    def __init__(self, name, age, profesion, dni):
        self.name = name
        self.age = age
        self.profesion = profesion
        self.dni = dni
#Aqui es la def es una estructura para reutilizar el codigo y pueda cambiar la informacion agregada en los "datos"
    time.sleep(2)
    def info(self):
        return f"Hola mi nombre es: {self.name}\nMi edad es: {self.age}\nTambien estudio la profesion de: {self.profesion}\ny mi cedula es: {self.dni}"
#Def para cambiar el nombre
    def changer_name(self, new_name):
        """Aqui cambiamos el nombre"""
        self.name = new_name
        print(f"El nuevo nombre de la perosna es: {self.name}.")
#Def para cambiar la cedula 
    def changer_cc(self, new_dni):
        """Aqui se corrigue la cc por si quedo mal"""
        self.dni = new_dni
        print(f"El nuevo numero de Cedula es: {self.dni}.") 
#Aqui se ponen los datos que se va a utilizar para que se imprima con el "def info"
datos = Persona("Daniel Molina", "20", "Programador", "1234567")
#Aqui imprimimos lo que necesitamos para visualizar la estructura del info ya con los parametros 
print(datos.info())
#Aqui es para modificar los parametros originales 
time.sleep(2)
print("================================================")
datos.changer_name("Carlos Molina")
datos.changer_cc ("987654")
