import os
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorAnadirInformes import ControladorAnadirInformes

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaAnadirInformes.ui")
Form, Window = uic.loadUiType(ruta_ui)

class VistaAnadirInformes(QMainWindow, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorAnadirInformes(self)

    def rellenar_tabla_mascotas(self, mascotas):
        self.tablaBuscadorMascotas.setRowCount(0)
        self.tablaBuscadorMascotas.setColumnCount(3)
        self.tablaBuscadorMascotas.setHorizontalHeaderLabels(["ID", "Nombre", "Especie"])
        for fila_idx, mascota in enumerate(mascotas):
            self.tablaBuscadorMascotas.insertRow(fila_idx)
            self.tablaBuscadorMascotas.setItem(fila_idx, 0, QTableWidgetItem(str(mascota.get_id_mascota())))
            self.tablaBuscadorMascotas.setItem(fila_idx, 1, QTableWidgetItem(mascota.get_nombre()))
            self.tablaBuscadorMascotas.setItem(fila_idx, 2, QTableWidgetItem(mascota.get_especie()))

    def obtener_fila_seleccionada(self):
        return self.tablaBuscadorMascotas.currentRow()

    def mostrar_aviso_seleccion(self):
        QMessageBox.warning(self, "Aviso", "Por favor, selecciona un paciente de la lista.")

    def obtener_datos_fila(self, fila):
        id_mascota = int(self.tablaBuscadorMascotas.item(fila, 0).text())
        nombre = self.tablaBuscadorMascotas.item(fila, 1).text()
        return id_mascota, nombre