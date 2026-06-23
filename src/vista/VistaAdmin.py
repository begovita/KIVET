import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorAdmin import ControladorAdmin

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaAdmin.ui")
Form, Window = uic.loadUiType(ruta_ui)

class VistaAdmin(QMainWindow, Form):
    def __init__(self, dni_admin):
        super().__init__()
        self.setupUi(self)
        self.dni_admin = dni_admin

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorAdmin(self, dni_admin)

    def mostrar_total(self, total):
        QMessageBox.information(self, "Facturación", f"Total mensual: {total:.2f} €")

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, "Error", mensaje)

    def mostrar_exito(self, mensaje):
        QMessageBox.information(self, "Éxito", mensaje)

    def pedir_ruta_guardado(self):
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar", "", "*.sql")
        return ruta

    def pedir_ruta_lectura(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Abrir", "", "*.sql")
        return ruta

    def confirmar_accion(self):
        return QMessageBox.question(self, "Atención", "¿Continuar?") == QMessageBox.Yes