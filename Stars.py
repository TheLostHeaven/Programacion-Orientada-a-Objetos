class CuerpoCeleste:
    def __init__(self, nombre, masa, diametro):
        self.__nombre = nombre
        self.__masa = masa
        self.__diametro = diametro

    def get_nombre(self):
        return self.__nombre

    def get_masa(self):
        return self.__masa

    def get_diametro(self):
        return self.__diametro


class Estrella(CuerpoCeleste):
    def __init__(self, nombre, masa, diametro, tipo):
        super().__init__(nombre, masa, diametro)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo


class Planeta(CuerpoCeleste):
    def __init__(self, nombre, masa, diametro, distancia_sol):
        super().__init__(nombre, masa, diametro)
        self.__distancia_sol = distancia_sol

    def get_distancia_sol(self):
        return self.__distancia_sol


# Crear instancias de la clase Estrella
estrella1 = Estrella("Sol", 1.989e30, 1.3914e6, "enana amarilla")
estrella2 = Estrella("Sirio", 2.021e30, 1.711e6, "enana blanca")

# Crear instancias de la clase Planeta
planeta1 = Planeta("Tierra", 5.97e24, 12.742e3, 149.6e6)
planeta2 = Planeta("Marte", 6.39e23, 6.779e3, 227.9e6)

# Imprimir información de las instancias
print("Nombre:", estrella1.get_nombre(), "- Masa:", estrella1.get_masa(), "- Diámetro:", estrella1.get_diametro(), "- Tipo:", estrella1.get_tipo())
print("Nombre:", estrella2.get_nombre(), "- Masa:", estrella2.get_masa(), "- Diámetro:", estrella2.get_diametro(), "- Tipo:", estrella2.get_tipo())
print("Nombre:", planeta1.get_nombre(), "- Masa:", planeta1.get_masa(), "- Diámetro:", planeta1.get_diametro(), "- Distancia al sol:", planeta1.get_distancia_sol())
print("Nombre:", planeta2.get_nombre(), "- Masa:", planeta2.get_masa(), "- Diámetro:", planeta2.get_diametro(), "- Distancia al sol:", planeta2.get_distancia_sol())
