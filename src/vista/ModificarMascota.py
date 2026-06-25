import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorModificarMascota import ControladorModificarMascota

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaModificarMascota.ui")
Form, Window = uic.loadUiType(ruta_ui)

class ModificarMascota(QMainWindow, Form):
    def __init__(self, id_mascota, nombre_actual, controlador_menu):
        super().__init__()
        self.setupUi(self)

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorModificarMascota(self, id_mascota, nombre_actual, controlador_menu)

    def cargar_datos_actuales(self, nombre_actual):
        self.inputNombre.setText(nombre_actual)

    def obtener_nuevos_datos(self):
        nuevo_nombre = self.inputNombre.text().strip()
        nueva_especie = self.inputEspecie.text().strip()
        return nuevo_nombre, nueva_especie

    def mostrar_aviso(self, mensaje):
        QMessageBox.warning(self, "Error", mensaje)

    def mostrar_exito(self, mensaje):
        QMessageBox.information(self, "Éxito", mensaje)

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, "Error", mensaje)

    def ocultar_ventana(self):
        self.hide()