from Entity.DAO.CRUD_Curso import mostrarTodos
from Control.CursoController import CursoController


class AdministradorAlumnosController:
    def __init__(self):
        pass

    def listaCursos(self):
        cursos = mostrarTodos()
        listaCursos = []
        for curso in cursos:
            listaCursos.append(CursoController(curso[0], curso[1], curso[2]))
        return listaCursos
