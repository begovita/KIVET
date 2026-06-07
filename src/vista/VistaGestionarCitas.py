import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorGestionarCitas import ControladorGestionarCitas

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaGestionarCitas.ui")
Form, Window = uic.loadUiType(ruta_ui)

class VistaGestionarCitas(QMainWindow, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorGestionarCitas(self)