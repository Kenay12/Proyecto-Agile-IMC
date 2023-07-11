from Entity.DAO.CRUD_Curso import mostrarTodos
from Entity.DAO.CRUD_Alumno import consultaParticular
from Control.CursoController import CursoController
from Control.AlumnoController import AlumnoController





class AdministradorReporteController:
    def __init__(self):
        pass

    def listaCursos(self):
        cursos = mostrarTodos()
        listaCursos = []
        for curso in cursos:
            listaCursos.append(CursoController(curso[0], curso[1], curso[2]))
        return listaCursos
    def listaAlumnos(self,nivel,seccion):
        alumnos = consultaParticular(nivel,seccion)
        listaAlumnos = []
        for alumno in alumnos:
            listaAlumnos.append(AlumnoController(alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], alumno[5]))
        return listaAlumnos




