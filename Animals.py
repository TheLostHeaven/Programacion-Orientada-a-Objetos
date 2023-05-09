class Animal:
    def __init__(self, nombre, edad, especie):
        self.__nombre = nombre
        self.__edad = edad
        self.__especie = especie

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_especie(self):
        return self.__especie

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")

class Pajaro(Animal):
    def hacer_sonido(self):
        print("Pío!")

# Creamos una lista de animales
animales = [Perro("Rex", 5, "perro"),
                Gato("Garfield", 3, "gato"),
                Pajaro("Tweety", 1, "pájaro")]

# Llamamos al método hacer_sonido de cada animal
print(animales)

for animal in animales:
    animal.hacer_sonido()
for animal in animales:
    print("Nombre:", animal.get_nombre(), "- Edad:", animal.get_edad(), "- Especie:", animal.get_especie())