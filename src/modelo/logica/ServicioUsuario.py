from src.modelo.dao.UsuarioDAO import UsuarioDAO
from src.modelo.vo.UsuarioVO import UsuarioVO


class ServicioUsuario:
    def __init__(self):
        self.dao = UsuarioDAO()

    def validar_login(self, dni, contrasena):
        return self.dao.validar_credenciales(dni, contrasena)

    def registrar_nuevo_usuario(self, dni, contrasena):
        nombre = dni

        nuevo_usuario = UsuarioVO(dni, contrasena, nombre, "Dueno", "Pendiente")

        exito = self.dao.insertar(nuevo_usuario)
        if not exito:
            raise Exception("No se ha podido registrar. Comprueba que el DNI no exista ya.")

    def obtener_pendientes(self):
        return self.dao.obtener_usuarios_pendientes()

    def validar_y_activar_usuario(self, dni, nombre, rol, telefono):
        exito = self.dao.finalizar_validacion(dni, nombre, rol, telefono)
        if not exito:
            raise Exception("No se pudo activar la cuenta en la base de datos.")