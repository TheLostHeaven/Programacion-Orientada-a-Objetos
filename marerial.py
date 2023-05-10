#Aqui importamos librerias
import time
#Creamos las clase padre con parametros 
class Materia:
    def __init__(self, nombre, creditos):
        self.__nombre = nombre
        self.__creditos = creditos
#Creamos los metodos "nombre"
    def get_nombre(self):
        return self.__nombre
#Creamos los metodos "creditos"
    def get_creditos(self):
        return self.__creditos

#Creamos otra clase hija con parametros
class Matematicas(Materia):
    def __init__(self, nombre, creditos, nivel):
        super().__init__(nombre, creditos)
        self.__nivel = nivel
#En la clase hija creamos un nuevo metodo 
    def get_nivel(self):
        return self.__nivel

#Aqui creamos otra clase hija que tiene un parametro
class Fisica(Materia):
    def __init__(self, nombre, creditos, laboratorio):
        super().__init__(nombre, creditos)
        self.__laboratorio = laboratorio
#Aqui esta el metodo 
    def tiene_laboratorio(self):
        return self.__laboratorio
#Aqui creamos una instancia 
matematicas1 = Matematicas("Matemáticas 1", 6, "Básico")
fisica1 = Fisica("Física 1", 5, "Básico")
#Y finalmente terminamos imprimiendo
print("================================================")
print(matematicas1.get_nombre())
print(matematicas1.get_creditos())
print(matematicas1.get_nivel())
print("================================================")
time.sleep(2)
print(fisica1.get_nombre())
print(fisica1.get_creditos())
print(fisica1.tiene_laboratorio())
print("================================================")