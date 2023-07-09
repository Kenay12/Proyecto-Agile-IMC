from Entity.DAO.CRUD_Curso import mostrarTodos
from Control.CursoController import CursoController
from datetime import date


class AdministradorAlumnosController:
    def __init__(self):
        pass

    def listaCursos(self):
        cursos = mostrarTodos()
        listaCursos = []
        for curso in cursos:
            listaCursos.append(CursoController(curso[0], curso[1], curso[2]))
        return listaCursos

    def validarFechaNac(self, fecha):
        fecha_hoy = date.today()
        fecha_anio = fecha.split("-")[2]
        if fecha_hoy.year >= (int(fecha_anio) + 4):
            return True
        else:
            return False
