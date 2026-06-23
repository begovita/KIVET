import os
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorAnadirInformes2 import ControladorAnadirInformes2

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaAnadirInformes2.ui")
Form, Window = uic.loadUiType(ruta_ui)

class VistaAnadirInformes2(QMainWindow, Form):
    def __init__(self, id_mascota, nombre_mascota):
        super().__init__()
        self.setupUi(self)

        self.id_mascota = id_mascota
        self.nombre_mascota = nombre_mascota

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorAnadirInformes2(self, self.id_mascota, self.nombre_mascota)

    def actualizar_titulo(self, nombre_mascota):
        self.lblTitulo.setText(f"Historial clínico de {nombre_mascota}")

    def rellenar_tabla_informes(self, informes):
        self.tablaInformesVet.setRowCount(0)
        self.tablaInformesVet.setColumnCount(3)
        self.tablaInformesVet.setHorizontalHeaderLabels(["Fecha", "Tipo", "Archivo Adjunto"])

        for fila_idx, info in enumerate(informes):
            self.tablaInformesVet.insertRow(fila_idx)
            self.tablaInformesVet.setItem(fila_idx, 0, QTableWidgetItem(str(info.get_fecha())))
            self.tablaInformesVet.setItem(fila_idx, 1, QTableWidgetItem(info.get_tipo_documento()))
            self.tablaInformesVet.setItem(fila_idx, 2, QTableWidgetItem(info.get_descripcion()))

    def pedir_ruta_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar Informe Clínico", "", "Archivos PDF (*.pdf);;Todos los archivos (*.*)"
        )
        return ruta

    def mostrar_ruta_seleccionada(self, ruta):
        self.lblRuta.setText(ruta)

    def obtener_tipo_informe(self):
        return self.cboTipo.currentText()

    def limpiar_formulario(self):
        self.lblRuta.setText("(Ningún archivo seleccionado)")

    def mostrar_aviso(self, mensaje):
        QMessageBox.warning(self, "Aviso", mensaje)

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, "Error", mensaje)

    def mostrar_exito(self, mensaje):
        QMessageBox.information(self, "Éxito", mensaje)