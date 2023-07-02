from Entity.DAO.CRUD_Login import consultaParticular


class LoginController:
    def __init__(self):
        pass

    def inicioSesion(self, email, passwd):
        usuario = consultaParticular(email)
        if usuario is not None:
            if usuario[2] == passwd:
                return True
            else:
                return False
        else:
            return False
