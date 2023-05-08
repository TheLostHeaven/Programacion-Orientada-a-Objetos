#Importamos la clase pardre en otro archivo
from Poo1 import Persona
#Aqui iniciamos con la clase hija 
class Estudiante(Persona):
    def __init__(self, name, age, profesion, dni, course, teacher):
        super().__init__(name, age, profesion, dni)
        self._course = course
        self._teacher = teacher
#
    def info(self):
        return f"Hola mi nombre es: {self.name}\nMi edad es: {self.age}\nSoy: {self.profesion}\ny mi T.I es: {self.dni}\nEstoy en el curso: {self.course}\nY mi profesor es: {self.teacher}"
    
datos = Estudiante("Juan Perez", "8", "Estudiante", "45678" "Quinto de primaria" "Julio Profe")

print(datos.info())
