import pymysql

class Conexion:
    def __int__(self,host,user,passwd,db):
        self.db = pymysql.connect(
            host = host,
            user = user,
            password=passwd,
            db=db
        )
        self.cursor= self.db.cursor()
    def ejecuta_query(self,sql):
        self.cursor.execute(sql)
        return self.cursor
    def desconectar(self):
        self.db.close()
    def commit(self):
        self.db.commit()
    def rollback(self):
        self.db.rollback()