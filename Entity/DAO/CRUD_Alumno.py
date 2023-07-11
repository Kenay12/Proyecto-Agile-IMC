
from Entity.DTO.Conexion import Conexion


host = "localhost"
user = "root"
password = ""
db = "proyecto_imc"


def ingresar(estudiante):
    con = Conexion(host, user, password, db)
    sql = "INSERT INTO estudiante SET rut='{}', nombres='{}', apellidos='{}', fecha_nacimiento='{}', " \
          "sexo='{}', id_curso='{}'".format(estudiante.rut.get(), estudiante.nombres.get(),
                                                estudiante.apellidos.get(), estudiante.fecha_nac.get(),
                                                estudiante.intSexo, estudiante.id_curso)
    con.ejecuta_query(sql)
    con.commit()
    con.desconectar()

def consultaParticular(nivel,seccion):
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT `estudiante`.`nombres`,`estudiante`.`apellidos`,`imc`.`valor`,`imc`.`rango`,`curso`.`nivel`,`curso`.`seccion` FROM `estudiante` INNER JOIN `curso` ON `curso`.`id_curso` = `estudiante`.`id_curso` INNER JOIN `imc` ON `imc`.`rut_estudiante` = `estudiante`.`rut_estudiante` WHERE `curso`.`nivel` = '{}' AND `curso`.`seccion` = '{}'".format(nivel,seccion)
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print(e)


