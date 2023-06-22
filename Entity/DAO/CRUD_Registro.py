from DTO.Conexion import Conexion

host="localhost"
user="root"
password=""
db="Proyecto-Agile-IMC"

def ingresar(reg):
    try:
        con=Conexion(host,user,password,db)
        sql="Insert Into registro set rut='{}',nombre='{}',apellido='{}',mail='{}'," \
            "clave='{}',fechaNacimiento='{}'".format(reg.rut,reg.nombre,
                                       reg.apellido,reg.mail,reg.clave,reg.fechaNacimiento)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos Ingresados con Éxito, presione una tecla para continuar")
        con.desconectar()

    except Exception as e:
        print("Error en la Función Ingresar: ",e)

def modificar(reg):
    try:
        con=Conexion(host,user,password,db)
        sql="UPDATE registro SET rut='{}',nombre='{}',apellido='{}',mail='{}',clave='{}',fechaNacimiento='{}'" \
            "WHERE idCurso={}".format(reg[1],reg[2],reg[3],reg[4],reg[5],,reg[6],reg[0])

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