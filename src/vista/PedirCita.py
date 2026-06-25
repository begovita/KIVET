import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorPedirCita import ControladorPedirCita

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaPedirCita.ui")
Form, Window = uic.loadUiType(ruta_ui)

class PedirCita(QMainWindow, Form):
    def __init__(self, id_mascota, nombre_mascota):
        super().__init__()
        self.setupUi(self)

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorPedirCita(self, id_mascota, nombre_mascota)

    def preparar_horas_clinica(self):
        if hasattr(self, 'inputHora'):
            self.inputHora.clear()
            horas_clinica = [
                "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
                "12:00", "12:30", "13:00", "16:00", "16:30", "17:00",
                "17:30", "18:00", "18:30", "19:00", "19:30"
            ]
            self.inputHora.addItems(horas_clinica)

    def obtener_datos_cita(self):
        fecha = self.inputFecha.date().toString("yyyy-MM-dd")
        hora = self.inputHora.currentText()
        motivo = self.inputMotivo.text().strip()
        return fecha, hora, motivo

    def mostrar_aviso(self, mensaje):
        QMessageBox.warning(self, "Aviso", mensaje)

    def mostrar_exito(self, mensaje):
        QMessageBox.information(self, "Éxito", mensaje)

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, "Error de Inserción", mensaje)

    def ocultar_ventana(self):
        self.hide()