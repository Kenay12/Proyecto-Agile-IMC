from datetime import date


class CalculoIMCController:
    def __init__(self, registro, rutEstudiante):
        self.__registroIMC = registro
        self.__registroIMC.__rutEstudiante = rutEstudiante

    def fechaActual(self):
        fechaActual = date.today()
        self.__registroIMC.__fecha = fechaActual
    
    def calcularIMC(self, peso, altura):
        if (peso >= 15 and peso <= 90) and (altura >= 0.4 and altura <= 2.0):
            self.__registroIMC.__peso = peso
            self.__registroIMC.__altura = altura
            self.__registroIMC.__valor = round(peso / (altura ** 2), 1)
            if self.__registroIMC.__valor < 18.5:
                self.__registroIMC.__rango = "Peso bajo"
            elif self.__registroIMC.__valor >= 18.5 and self.__registroIMC.valor < 25.0:
                self.__registroIMC.__rango = "Peso normal"
            elif self.__registroIMC.__valor >= 25.0 and self.__registroIMC.valor < 30.0:
                self.__registroIMC.__rango = "Sobrepeso"
            elif self.__registroIMC.__valor >= 30.0:
                self.__registroIMC.__rango = "Obesidad"
            fechaActual()
        else:
            return "Valores inválidos"
