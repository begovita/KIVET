import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorAnadirFactura2 import ControladorAnadirFactura2

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaAnadirFactura2.ui")
Form, Window = uic.loadUiType(ruta_ui)

class VistaAnadirFactura2(QMainWindow, Form):
    def __init__(self, dni_admin, id_mascota, nombre_mascota):
        super().__init__()
        self.setupUi(self)

        self.dni_admin = dni_admin
        self.id_mascota = id_mascota
        self.nombre_mascota = nombre_mascota

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorAnadirFactura2(self, self.dni_admin, self.id_mascota, self.nombre_mascota)