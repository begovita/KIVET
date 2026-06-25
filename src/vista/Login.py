from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
import os
from PyQt5.QtGui import QPixmap
from src.controlador.ControladorLogin import ControladorLogin

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaLogin.ui")
Form, Window = uic.loadUiType(ruta_ui)

class MiVentana(QMainWindow, Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # logo
        directorio_actual = os.path.dirname(__file__)
        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        pixmap = QPixmap(ruta_imagen)
        self.label_3.setPixmap(pixmap)

        self.controlador = ControladorLogin(self)

    def obtener_credenciales_login(self):
        dni = self.nombreUsuario.text().strip()
        contrasena = self.contrasena.text().strip()
        return dni, contrasena

    def obtener_datos_registro(self):
        dni = self.nombreUsuarioNuevo.text().strip()
        contrasena = self.contrasenaNueva.text().strip()
        return dni, contrasena

    def limpiar_formulario_registro(self):
        self.nombreUsuarioNuevo.clear()
        self.contrasenaNueva.clear()

    def ocultar_ventana(self):
        self.hide()

    def mostrar_aviso(self, titulo, mensaje):
        QMessageBox.warning(self, titulo, mensaje)

    def mostrar_exito(self, titulo, mensaje):
        QMessageBox.information(self, titulo, mensaje)

    def mostrar_error(self, titulo, mensaje):
        QMessageBox.critical(self, titulo, mensaje)

if __name__ == "__main__":
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    app.exec_()