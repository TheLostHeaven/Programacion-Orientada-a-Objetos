class Bebida:
    def __init__(self, marca, sabor, precio):
        self.__marca = marca
        self.__sabor = sabor
        self.__precio = precio

    def get_marca(self):
        return self.__marca

    def get_sabor(self):
        return self.__sabor

    def get_precio(self):
        return self.__precio

class Refresco(Bebida):
    def __init__(self, marca, sabor, precio, tipo):
        super().__init__(marca, sabor, precio)
        self.__tipo = tipo

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
    print()