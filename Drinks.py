#Aqui ponemos librerias :D
import time
#Creamos la clase
class Bebida:
    def __init__(self, marca, sabor, precio):
        self.__marca = marca
        self.__sabor = sabor
        self.__precio = precio
#Obtener el dato de la "marca" ya que es privado
    def get_marca(self):
        return self.__marca
#Obtener el dato de la "Sabor" ya que es privado
    def get_sabor(self):
        return self.__sabor
#Obtener el dato de la "Precio" ya que es privado ("cinco peso")
    def get_precio(self):
        return self.__precio
#Creamos la clase hija que hereda del padre
class Refresco(Bebida):
    def __init__(self, marca, sabor, precio, tipo):
        super().__init__(marca, sabor, precio)
        self.__tipo = tipo
#Y le añadimos mas def para que haga mas cosas
    def get_tipo(self):
        return self.__tipo

# Crear instancias de la clase Refresco
coca_cola = Refresco("Coca-Cola", "Cola", 4.500, "Regular")
print("================================================")
sprite = Refresco("Sprite", "Limón", 3.500, "Light")
fanta = Refresco("Fanta", "Naranja", 5.000, "Regular")
# Imprimir información de cada refresco
for refresco in [coca_cola, sprite, fanta]:
    print("Marca:", refresco.get_marca())
    print("Sabor:", refresco.get_sabor())
    print("Precio:", refresco.get_precio())
    print("Tipo:", refresco.get_tipo())
    print("================================================")
    time.sleep(2)
    print()