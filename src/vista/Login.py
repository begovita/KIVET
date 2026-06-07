from PyQt5.QtWidgets import QApplication, QMainWindow
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

if __name__ == "__main__":
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    app.exec_()