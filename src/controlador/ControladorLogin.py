from PyQt5.QtWidgets import QMessageBox
from src.modelo.dao.UsuarioDAO import UsuarioDAO
from src.modelo.vo.UsuarioVO import UsuarioVO
from src.vista.MenuPpal import MenuPpal


class ControladorLogin:
    def __init__(self, vista):
        self.vista = vista
        self.dao = UsuarioDAO()

        # vincular los botones a las funciones
        self.vista.botonAceptar.clicked.connect(self.iniciar_sesion)
        self.vista.botonRegistrarse.clicked.connect(self.registrar_usuario)

    def iniciar_sesion(self):
        # leer los datos de los QLineEdit (usuario y contraseña)
        dni = self.vista.nombreUsuario.text().strip()
        contrasena = self.vista.contrasena.text().strip()

        if not dni or not contrasena:
            QMessageBox.warning(self.vista, "Campos vacíos", "Por favor, introduce DNI y contraseña.")
            return

        rol_obtenido = self.dao.validar_credenciales(dni, contrasena)

        if rol_obtenido:
            QMessageBox.information(self.vista, "Éxito", f"Acceso concedido. Entrando como: {rol_obtenido}")

            self.vista_menu = MenuPpal(dni, rol_obtenido)
            self.vista_menu.show()
            # esconder el Login
            self.vista.hide()
        else:
            QMessageBox.critical(self.vista, "Error de acceso", "DNI incorrecto, contraseña inválida o cuenta pendiente.")

    def registrar_usuario(self):
        # leer los datos
        dni = self.vista.nombreUsuarioNuevo.text().strip()
        contrasena = self.vista.contrasenaNueva.text().strip()

        # dni es nombre temporal
        nombre = dni

        if not dni or not contrasena:
            QMessageBox.warning(self.vista, "Campos vacíos", "Rellena todos los campos para registrarte.")
            return

        # empaquetar y enviar
        nuevo_usuario = UsuarioVO(dni, contrasena, nombre, "Dueno", "Pendiente")

        if self.dao.insertar(nuevo_usuario):
            QMessageBox.information(self.vista, "Registro completado", "Usuario registrado correctamente.")
            self.vista.nombreUsuarioNuevo.clear()
            self.vista.contrasenaNueva.clear()
        else:
            QMessageBox.warning(self.vista, "Error en el registro", "No se ha podido registrar. Comprueba que el DNI no exista ya.")