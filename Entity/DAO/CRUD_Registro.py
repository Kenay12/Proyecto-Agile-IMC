from Entity.DTO.Conexion import Conexion


host = "localhost"
user = "imc_usuario"
password = "123"
db = "proyecto_imc"


def ingresar(reg):
    try:
        con=Conexion(host,user,password,db)
        sql="Insert Into imc set valor='{}',rango='{}',fecha='{}',peso='{}',altura='{}',rut_estudiante = '{}'" \
            "".format(reg.valor, reg.rango, reg.fecha, reg.peso, reg.altura, reg.rut_estudiante)
        con.ejecuta_query(sql)
        con.commit()
        con.desconectar()

    except Exception as e:
        print(e)

def modificar(reg):
    try:
        con=Conexion(host,user,password,db)
        sql="UPDATE registro SET valor='{}',rango='{}',fecha='{}',peso='{}',altura='{}'" \
            "WHERE idCurso={}".format(reg[1],reg[2],reg[3],reg[4],reg[5],reg[0])

        con.ejecuta_query(sql)
        con.commit()
        input("\n\nDatos Modificados con Éxito :)")
        con.desconectar()
    except Exception as e:
        print("Error en Modificar: ",e)

def eliminar(id):
    try:
        con=Conexion(host,user,password,db)
        sql="Delete from Registro where idCurso={}".format(id)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Registro Eliminado con Éxito")
        con.desconectar()
    except Exception as e:
        print("Error al Eliminar: ",e)

def mostrarTodos():
    try:
        con=Conexion(host,user,password,db)
        sql="Select * from registro"
        cursor=con.ejecuta_query(sql)
        datos=cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print("Error en Mostrar Todos: ",e)

def consultaParticular(id):
    try:
        con=Conexion(host,user,password,db)
        sql="Select * from registro where idCurso={}".format(id)
        cursor=con.ejecuta_query(sql)
        datos=cursor.fetchone()
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print("Error en Consulta Particular: ",e)

def consultaParcial(cantidad):
    try:
        con=Conexion(host,user,password,db)
        sql="Select * from Registro"
        cursor=con.ejecuta_query(sql)
        datos=cursor.fetchmany(size=cantidad)
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print("Error en Consulta Parcial: ",e)