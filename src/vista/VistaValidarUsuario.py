import os
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorValidarUsuario import ControladorValidarUsuario

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaValidarUsuario.ui")
Form, Window = uic.loadUiType(ruta_ui)

class VistaValidarUsuario(QMainWindow, Form):
    def __init__(self, dni_admin):
        super().__init__()
        self.setupUi(self)
        self.dni_admin = dni_admin

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorValidarUsuario(self, self.dni_admin)

    def rellenar_tabla_pendientes(self, usuarios):
        self.tablaUsuariosPendientes.setRowCount(0)
        self.tablaUsuariosPendientes.setColumnCount(3)
        self.tablaUsuariosPendientes.setHorizontalHeaderLabels(["DNI", "Nombre", "Rol Solicitado"])

        for fila_idx, user in enumerate(usuarios):
            self.tablaUsuariosPendientes.insertRow(fila_idx)
            self.tablaUsuariosPendientes.setItem(fila_idx, 0, QTableWidgetItem(user["dni"]))
            self.tablaUsuariosPendientes.setItem(fila_idx, 1, QTableWidgetItem(user["nombre"]))
            self.tablaUsuariosPendientes.setItem(fila_idx, 2, QTableWidgetItem(user["rol"]))

    def obtener_fila_seleccionada(self):
        return self.tablaUsuariosPendientes.currentRow()

    def obtener_dni_fila(self, fila):
        return self.tablaUsuariosPendientes.item(fila, 0).text()

    def mostrar_aviso(self, mensaje):
        QMessageBox.warning(self, "Aviso", mensaje)