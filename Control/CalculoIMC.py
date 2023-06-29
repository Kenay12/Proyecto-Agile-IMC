from datetime import date
from Control.RegistroController import RegistroController
from Entity.DAO.CRUD_Registro import ingresar
from Control.EstudianteController import EstudianteController


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
            return registro
        else:
            return "Valores inválidos"

    def ingresarIMC(self, peso, altura, rut):
        if rut != "":
            registro = self.calcularIMC(peso, altura, rut)
            if not isinstance(registro, str):
                ingresar(registro)
            return registro
        else:
            return "Se necesita seleccionar un alumno"

    def obtenerListaAlumno(self):
        return {
                "Quinto Básico A": [EstudianteController("11.111.111-1", "Bastián", "Zarate", "01-01-2000", 1, 1),
                                    EstudianteController("22.222.222-2", "Nicolás", "Zarate", "01-01-2000", 1, 1),
                                    EstudianteController("33.333.333-3", "Valencia", "Zarate", "01-01-2000", 1, 1)],
                "Quinto Básico B": [EstudianteController("44.444.444-4", "Vidal", "Zarate", "01-01-2000", 1, 1),
                                    EstudianteController("55.555.555-5", "Medel", "Zarate", "01-01-2000", 1, 1),
                                    EstudianteController("66.666.666-6", "Landeros", "Zarate", "01-01-2000", 1, 1)],
                "Sexto Básico A": [EstudianteController("77.777.777-7", "Guerra", "Zarate", "01-01-2000", 1, 1),
                                   EstudianteController("88.888.888-8", "Assadi", "Zarate", "01-01-2000", 1, 1),
                                   EstudianteController("99.999.999-9", "Sanchez", "Zarate", "01-01-2000", 1, 1)],
                "Sexto Básico B": [EstudianteController("12.345.678-9", "Messi", "Zarate", "01-01-2000", 1, 1),
                                   EstudianteController("98.765.432-1", "Julian", "Zarate", "01-01-2000", 1, 1),
                                   EstudianteController("00.000.000-0", "Mono", "Sanchez", "01-01-2000", 1, 1)]
            }

    def obtenerCursos(self):
        return ["Quinto Básico A", "Quinto Básico B", "Sexto Básico A", "Sexto Básico B"]
