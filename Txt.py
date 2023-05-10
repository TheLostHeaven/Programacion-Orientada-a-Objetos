#imṕortamos librerias :"D
import time

#Creamos las clases con sus parametros
class Texto:
    def __init__(self, contenido):
        self.__contenido = contenido
#Creamos el metodo "Contenido"
    def get_contenido(self):
        return self.__contenido

#Creamos otra clase hija con sus parametros
class TextoPlano(Texto):
    def __init__(self, contenido, autor):
        super().__init__(contenido)
        self.__autor = autor
#Creamos los metodos "autor"
    def get_autor(self):
        return self.__autor

#Creamos otra clase hija con sus parametros
class TextoEnriquecido(Texto):
    def __init__(self, contenido, formato):
        super().__init__(contenido)
        self.__formato = formato
#Creamos los metodos "Formato"
    def get_formato(self):
        return self.__formato

#Creamos las instancias 
texto_1 = Texto("Este es un texto de ejemplo")
texto_2 = TextoPlano("Este es otro texto", "Juan")
texto_3 = TextoEnriquecido("Este es un tercer texto", "negrita")
#Aqui las imprimimos 
print(texto_1.get_contenido())
print("================================================")
time.sleep(2)
print(texto_2.get_contenido(), "escrito por", texto_2.get_autor())
print("================================================")
time.sleep(2)
print(texto_3.get_contenido(), "con formato", texto_3.get_formato())
print("================================================")