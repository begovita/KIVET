import os
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorMenuPpal import ControladorMenuPpal

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaMenuPpal.ui")
Form, Window = uic.loadUiType(ruta_ui)

class MenuPpal(QMainWindow, Form):
    def __init__(self, dni, rol):
        super().__init__()
        self.setupUi(self)

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorMenuPpal(self, dni, rol)

    def aplicar_permisos(self, rol_usuario):
        if hasattr(self, 'btnPanelAdmin'):
            self.btnPanelAdmin.setVisible(False)
        if hasattr(self, 'btnPanelVet'):
            self.btnPanelVet.setVisible(False)

        if rol_usuario == "Administrativo":
            if hasattr(self, 'btnPanelAdmin'):
                self.btnPanelAdmin.setVisible(True)
        elif rol_usuario == "Veterinario":
            if hasattr(self, 'btnPanelVet'):
                self.btnPanelVet.setVisible(True)

    def rellenar_tabla_mascotas(self, mascotas):
        self.tablaMascotas.setRowCount(0)
        self.tablaMascotas.setColumnCount(3)
        self.tablaMascotas.setHorizontalHeaderLabels(["ID", "Nombre", "Especie"])

        for fila_idx, mascota in enumerate(mascotas):
            self.tablaMascotas.insertRow(fila_idx)
            self.tablaMascotas.setItem(fila_idx, 0, QTableWidgetItem(str(mascota.get_id_mascota())))
            self.tablaMascotas.setItem(fila_idx, 1, QTableWidgetItem(mascota.get_nombre()))
            self.tablaMascotas.setItem(fila_idx, 2, QTableWidgetItem(mascota.get_especie()))

    def obtener_fila_seleccionada(self):
        return self.tablaMascotas.currentRow()

    def obtener_datos_fila(self, fila):
        id_mascota = int(self.tablaMascotas.item(fila, 0).text())
        nombre = self.tablaMascotas.item(fila, 1).text()
        return id_mascota, nombre

    def mostrar_aviso(self, mensaje):
        QMessageBox.warning(self, "Aviso", mensaje)

    def cerrar_ventana(self):
        self.close()