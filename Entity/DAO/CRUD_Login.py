from Entity.DTO.Conexion import Conexion


host = "localhost"
user = "root"
password = ""
db = "proyecto_imc"


def modificar(usu):
    try:
        con = Conexion(host, user, password, db)
        sql = "UPDATE usuario SET rut='{}', nombreUsuario='{}', apellidoUsuario='{}', mailUsuario='{}', " \
              "claveUsuario='{}', estadoUsuario='{}', fechaUltimoIngreso='{}', horaUltimoIngreso='{}' WHERE " \
              "idUsuario='{}'".format(usu[1], usu[2], usu[3], usu[4], usu[5], usu[6], usu[7], usu[8], usu[0])
        con.ejecuta_query(sql)
        con.commit()
        con.desconectar()
    except Exception as e:
        print(e)


def consultaParticular(email):
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM usuario WHERE email='{}'".format(email)
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchone()
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print(e)