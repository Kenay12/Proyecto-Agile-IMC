class CalculoIMCController:
    def __init__(self, registro, rutEstudiante):
        self.__registroIMC = registro
        self.__registroIMC.__rutEstudiante = rutEstudiante
    
    def calcularIMC(self, peso, altura):
        self.__registroIMC.peso = peso
        self.__registroIMC.altura = altura
        self.__registroIMC.valor = peso / (altura ** 2)