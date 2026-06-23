import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaAnadirMascota.ui")
Form, Window = uic.loadUiType(ruta_ui)

class AnadirMascota(QMainWindow, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

    def obtener_datos_mascota(self):
        nombre = self.inputNombre.text().strip()
        especie = self.inputEspecie.text().strip()
        return nombre, especie

    def mostrar_aviso(self, mensaje):
        QMessageBox.warning(self, "Aviso", mensaje)

    def mostrar_exito(self, mensaje):
        QMessageBox.information(self, "Éxito", mensaje)

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, "Error", mensaje)

    def cerrar_ventana(self):
        self.close()

