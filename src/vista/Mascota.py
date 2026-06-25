import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorMascota import ControladorMascota

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaMascota.ui")
Form, Window = uic.loadUiType(ruta_ui)

class Mascota(QMainWindow, Form):
    def __init__(self, id_mascota, nombre_mascota, controlador_menu):
        super().__init__()
        self.setupUi(self)

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorMascota(self, id_mascota, nombre_mascota, controlador_menu)

    def confirmar_eliminacion(self, nombre_mascota):
        respuesta = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Estás seguro de que quieres eliminar a {nombre_mascota}? Esta acción no se puede deshacer.",
            QMessageBox.Yes | QMessageBox.No
        )
        return respuesta == QMessageBox.Yes

    def mostrar_exito(self, mensaje):
        QMessageBox.information(self, "Éxito", mensaje)

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, "Error", mensaje)

    def cerrar_ventana(self):
        self.close()