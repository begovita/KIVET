import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorAnadirFactura import ControladorAnadirFactura

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaAnadirFactura.ui")
Form, Window = uic.loadUiType(ruta_ui)

class VistaAnadirFactura(QMainWindow, Form):
    def __init__(self, dni_admin):
        super().__init__()
        self.setupUi(self)
        self.dni_admin = dni_admin

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorAnadirFactura(self, self.dni_admin)