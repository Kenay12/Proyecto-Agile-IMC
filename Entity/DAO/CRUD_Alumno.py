from Entity.DTO.Conexion import Conexion


host = "localhost"
user = "imc_usuario"
password = "123"
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
