#Importamos la clase pardre en otro archivo
# from Poo1 import Persona
from Poo1 import Persona
#Aqui iniciamos con la clase hija 
class Estudiante(Persona):
    def __init__(self, name, age, profesion, dni, course, teacher):
        super().__init__(name, age, profesion, dni)
        self.__course = course
        self.__teacher = teacher
#
    def info2(self):
        return f"Hola mi nombre es: {self.__name()}\nMi edad es: {self.__age()}\nSoy: {self.__profesion()}\ny mi T.I es: {self.__dni()}\nEstoy en el curso: {self.__course()}\nY mi profesor es: {self.__teacher()}"
    
datos2 = Estudiante("Juan Perez", "8", "Estudiante", "45678", "Quinto de primaria", "Julio Profe")

print(datos2.info2())