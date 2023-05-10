#Aqui ponemos las librerias :D
import time
#Aqui iniciamos la clase llamando a Animal
class Animal:
    def __init__(self, nombre, edad, especie):
        self.__nombre = nombre
        self.__edad = edad
        self.__especie = especie
#Aqui en este def es para que obtenga el dato del nombre privado
    def get_nombre(self):
        return self.__nombre
#Aqui en este def es para que obtenga el dato del edad privado
    def get_edad(self):
        return self.__edad
#Aqui en este def es para que obtenga el dato del especie privado
    def get_especie(self):
        return self.__especie
#Es un metodo que esta vacio y las hijas lo pueden heredar e imprimir lo que se le configure en las clases hijas 
    def hacer_sonido(self):
        pass
#Esta es la clase "Perro" e hija de la la clase padre "Animal"
class Perro(Animal):
    def hacer_sonido(self):
#El sonido que hacer es Guau
        print("Guau!")
#Esta es la clase "Gato" e hija de la la clase padre "Animal"
class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")
#El sonido que hacer es Miau

#Esta es la clase "Pajaro" e hija de la la clase padre "Animal"
class Pajaro(Animal):
    def hacer_sonido(self):
        print("Pío!")
#El sonido que hacer es Pio

# Creamos una instancia de animales con otros dato para que me los imprima en pantalla 
animales = [Perro("Rex", 5, "perro"),
                Gato("Garfield", 3, "gato"),
                Pajaro("Tweety", 1, "pájaro")]

# Llamamos al método hacer_sonido de cada animal
for animal in animales:
    animal.hacer_sonido()
print("================================================")
time.sleep(2)
#Y en lo ultimo implementamos los print para ver los datos de los animales en pantalla
for animal in animales:
    print("Nombre:", animal.get_nombre(), "- Edad:", animal.get_edad(), "- Especie:", animal.get_especie())
    print("================================================")