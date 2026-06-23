import os
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
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

    def obtener_fecha_texto(self):
        fecha_qt = self.calendarioCitas.selectedDate()
        return fecha_qt.toString("yyyy-MM-dd")

    def rellenar_tabla_citas(self, citas):
        self.tablaCitasVet.setRowCount(0)
        self.tablaCitasVet.setColumnCount(4)
        self.tablaCitasVet.setHorizontalHeaderLabels(["ID Cita", "Hora", "Mascota", "Motivo"])

        for fila_idx, cita in enumerate(citas):
            self.tablaCitasVet.insertRow(fila_idx)
            self.tablaCitasVet.setItem(fila_idx, 0, QTableWidgetItem(str(cita["id_cita"])))
            self.tablaCitasVet.setItem(fila_idx, 1, QTableWidgetItem(cita["hora"]))
            self.tablaCitasVet.setItem(fila_idx, 2, QTableWidgetItem(cita["nombre_mascota"]))
            self.tablaCitasVet.setItem(fila_idx, 3, QTableWidgetItem(cita["motivo"]))

    def obtener_fila_seleccionada(self):
        return self.tablaCitasVet.currentRow()

    def obtener_datos_cita(self, fila):
        id_cita = int(self.tablaCitasVet.item(fila, 0).text())
        nombre_mascota = self.tablaCitasVet.item(fila, 2).text()
        return id_cita, nombre_mascota

    def mostrar_aviso(self, mensaje):
        QMessageBox.warning(self, "Aviso", mensaje)