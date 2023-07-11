from Entity.DTO.Conexion import Conexion


host = "localhost"
user = "root"
password = ""
db = "proyecto_imc"


def mostrarTodos():
    try:
        con = Conexion(host,user,password,db)
        sql = "Select * from curso"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        print("Error en Mostrar Todos: ",e)
        




