#Librerias
import time
#Iniciamos la funcionalidad
class Animals:
    def __init__(self, name, Npatas, carnivoro, hervivoro, especie, age):
        """Este metodo se hace para ver las caracteristicas del animal"""
        self.name = name
        self.Npatas = Npatas
        self.carnivoro = carnivoro
        self.hervivoro = hervivoro
        self.especie = especie
        self.age = age
        self.bite = False
    
    def info(self):
        return f"\nHola, ¿Como se llama tu perro?: {self.name}\n¿Tu perro cuantas patas tiene?: {self.Npatas}\n¿Tu perro es carnivoro?: {self.carnivoro}\n¿Tu perro es hervivoro?: {self.hervivoro}\n¿De que especie es tu perro?: {self.especie}\n¿Cuantos años tiene tu perro?: {self.age}"


    def BiteDog(self):
        """Metodo por si el animal muerde"""
        self.bite = True
        print("El perro esta enojado")

    def upgrade(self, new_age):
        """Metodo cuando el animal cumple años"""
        self.age = new_age
        print(f"El perro tuvo una actualizacion o subio de nivel {self.age}.")

datos = Animals("Growly", "4", "Si", "No", "Canina", "2")
print(datos.info())
print("================================================")
datos.upgrade ("3")
print("================================================")
datos.BiteDog ()