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
        if (peso >= 15 and peso <= 90) and (altura >= 0.4 and altura <= 2.0):
            valor = round(peso / (altura ** 2), 1)
            if valor < 18.5:
                rango = "Peso bajo"
            elif valor >= 18.5 and valor < 25.0:
                rango = "Peso normal"
            elif valor >= 25.0 and valor < 30.0:
                rango = "Sobrepeso"
            else:
                rango = "Obesidad"
            registro = RegistroController(valor, rango, self.fechaActual(), peso, altura, rut)
            try:
                ingresar(registro)
            except Exception as e:
                return "Error al ingresar en {}".format(e)
            return registro
        else:
            return "Valores inválidos"
