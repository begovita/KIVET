import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorVeterinario import ControladorVeterinario

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaVeterinario.ui")
Form, Window = uic.loadUiType(ruta_ui)

class VistaVeterinario(QMainWindow, Form):
    def __init__(self, dni_veterinario):
        super().__init__()
        self.setupUi(self)
        self.dni_veterinario = dni_veterinario

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorVeterinario(self, self.dni_veterinario)