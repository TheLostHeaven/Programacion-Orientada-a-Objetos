# #Librerias
# import time
# #Iniciamos la funcionalidad
# class Animals:
#     def __init__(self, name, Npatas, carnivoro, hervivoro, especie, age):
#         """Este metodo se hace para ver las caracteristicas del animal"""
#         self.name = name
#         self.Npatas = Npatas
#         self.carnivoro = carnivoro
#         self.hervivoro = hervivoro
#         self.especie = especie
#         self.age = age
#         self.bite = False
    
#     def info(self):
#         return f"\nHola, ¿Como se llama tu perro?: {self.name}\n¿Tu perro cuantas patas tiene?: {self.Npatas}\n¿Tu perro es carnivoro?: {self.carnivoro}\n¿Tu perro es hervivoro?: {self.hervivoro}\n¿De que especie es tu perro?: {self.especie}\n¿Cuantos años tiene tu perro?: {self.age}"


#     def BiteDog(self):
#         """Metodo por si el animal muerde"""
#         self.bite = True
#         print("El perro esta enojado")

#     def upgrade(self, new_age):
#         """Metodo cuando el animal cumple años"""
#         self.age = new_age
#         print(f"El perro tuvo una actualizacion o subio de nivel {self.age}.")

# datos = Animals("Growly", "4", "Si", "No", "Canina", "2")
# print(datos.info())
# print("================================================")
# datos.upgrade ("3")
# print("================================================")
# datos.BiteDog ()

#Aqui re escribimos el codigo, pero el codigo anterior tambien funciona pero no lo necesito para este proyecto
#Aqui iniciamos codigo con la clase Animal
class Animal:
    def __init__(self, nombre, edad, especie):
        self.__nombre = nombre
        self.__edad = edad
        self.__especie = especie
#Aqui hacemos la def "hacer sonido" y es de la clase padre que puede ser heredada a los hijos 
    def hacer_sonido(self):
        pass
#Aqui creamos def nombre
    def get_nombre(self):
        return self.__nombre
#Aqui creamos def edad
    def get_edad(self):
        return self.__edad
#Aqui creamos def especie
    def get_especie(self):
        return self.__especie

# Estos son las clases hija que comparte los atributos con el padre que es "def hacer_sonido" pero aqui es de un perro 
class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau")
# Esta es la clase hija que comparte los atributos con el padre "def hacer_sonido" y el de aqui es el de un gato
class Gato(Animal):
    def hacer_sonido(self):
        print("Miau miau")
#Aqui ponemos los datos que vamos a imprimor junto con los self y toca asi porque estan protegidos
mi_animal_1 = Animal("Rex", 5, "perro")
mi_animal_2 = Animal("Garfield", 3, "gato")
mi_animal_3 = Animal("Tweety", 1, "pájaro")

#Aqui imprimimos el sonido del perro 
perro1 = Perro("Growly")
print(perro1.nombre) 
perro1.hacer_sonido() 
#Aqui imprimimos el sonido de un gato
gato1 = Gato("Sony")
print(gato1.nombre)
gato1.hacer_sonido()
#Y por ultimo hacemos que nos imprima los datos
print("Nombre:", mi_animal_1.get_nombre(), "- Edad:", mi_animal_1.get_edad(), "- Especie:", mi_animal_1.get_especie())
print("Nombre:", mi_animal_2.get_nombre(), "- Edad:", mi_animal_2.get_edad(), "- Especie:", mi_animal_2.get_especie())
print("Nombre:", mi_animal_3.get_nombre(), "- Edad:", mi_animal_3.get_edad(), "- Especie:", mi_animal_3.get_especie())