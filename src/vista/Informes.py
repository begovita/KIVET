import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorInformes import ControladorInformes

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaInformes.ui")
Form, Window = uic.loadUiType(ruta_ui)

class Informes(QMainWindow, Form):
    def __init__(self, id_mascota, nombre_mascota):
        super().__init__()
        self.setupUi(self)

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorInformes(self, id_mascota, nombre_mascota)