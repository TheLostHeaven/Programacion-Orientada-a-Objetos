class Materia:
    def __init__(self, nombre, creditos):
        self.__nombre = nombre
        self.__creditos = creditos

    def get_nombre(self):
        return self.__nombre

    def get_creditos(self):
        return self.__creditos


class Matematicas(Materia):
    def __init__(self, nombre, creditos, nivel):
        super().__init__(nombre, creditos)
        self.__nivel = nivel

    def get_nivel(self):
        return self.__nivel


class Fisica(Materia):
    def __init__(self, nombre, creditos, laboratorio):
        super().__init__(nombre, creditos)
        self.__laboratorio = laboratorio

    def tiene_laboratorio(self):
        return self.__laboratorio

matematicas1 = Matematicas("Matemáticas 1", 6, "Básico")
fisica1 = Fisica("Física 1", 5, "Básico")

print("================================================")
print(matematicas1.get_nombre())
print(matematicas1.get_creditos())
print(matematicas1.get_nivel())
print("================================================")
print(fisica1.get_nombre())
print(fisica1.get_creditos())
print(fisica1.tiene_laboratorio())
print("================================================")