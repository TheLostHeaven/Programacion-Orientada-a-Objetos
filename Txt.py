class Texto:
    def __init__(self, contenido):
        self.__contenido = contenido

    def get_contenido(self):
        return self.__contenido


class TextoPlano(Texto):
    def __init__(self, contenido, autor):
        super().__init__(contenido)
        self.__autor = autor

    def get_autor(self):
        return self.__autor


class TextoEnriquecido(Texto):
    def __init__(self, contenido, formato):
        super().__init__(contenido)
        self.__formato = formato

    def get_formato(self):
        return self.__formato


texto_1 = Texto("Este es un texto de ejemplo")
texto_2 = TextoPlano("Este es otro texto", "Juan")
texto_3 = TextoEnriquecido("Este es un tercer texto", "negrita")

print(texto_1.get_contenido())
print(texto_2.get_contenido(), "escrito por", texto_2.get_autor())
print(texto_3.get_contenido(), "con formato", texto_3.get_formato())