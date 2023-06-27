from datetime import date
from Control.RegistroController import RegistroController
from Entity.DAO.CRUD_Registro import ingresar


class CalculoIMCController:
    def __init__(self):
        pass

    def fechaActual(self):
        fechaActual = date.today()
        return fechaActual
    
    def calcularIMC(self, peso, altura, rut):
        if (15 <= peso <= 90) and (0.4 <= altura <= 2.0):
            valor = round(peso / (altura ** 2), 1)
            if valor < 18.5:
                rango = "Peso bajo"
            elif 18.5 <= valor < 25.0:
                rango = "Peso normal"
            elif 25.0 <= valor < 30.0:
                rango = "Sobrepeso"
            else:
                rango = "Obesidad"
            registro = RegistroController(valor, rango, self.fechaActual(), peso, altura, rut)
            ingresar(registro)
            return registro
        else:
            return "Valores inválidos"
