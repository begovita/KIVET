import os
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorAnadirFactura2 import ControladorAnadirFactura2

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaAnadirFactura2.ui")
Form, Window = uic.loadUiType(ruta_ui)

class VistaAnadirFactura2(QMainWindow, Form):
    def __init__(self, dni_admin, id_mascota, nombre_mascota):
        super().__init__()
        self.setupUi(self)

        self.dni_admin = dni_admin
        self.id_mascota = id_mascota
        self.nombre_mascota = nombre_mascota

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorAnadirFactura2(self, self.dni_admin, self.id_mascota, self.nombre_mascota)

    def actualizar_titulo(self, nombre_mascota):
        self.lblTitulo.setText(f"Historial de Facturación: {nombre_mascota}")

    def rellenar_tabla_facturas(self, facturas):
        self.tablaFacturas.setRowCount(0)
        self.tablaFacturas.setColumnCount(4)
        self.tablaFacturas.setHorizontalHeaderLabels(["ID Factura", "ID Cita", "Fecha", "Importe (€)"])

        for fila_idx, f in enumerate(facturas):
            self.tablaFacturas.insertRow(fila_idx)
            self.tablaFacturas.setItem(fila_idx, 0, QTableWidgetItem(str(f.get_id_factura())))
            self.tablaFacturas.setItem(fila_idx, 1, QTableWidgetItem(str(f.get_id_cita())))
            self.tablaFacturas.setItem(fila_idx, 2, QTableWidgetItem(str(f.get_fecha())))
            self.tablaFacturas.setItem(fila_idx, 3, QTableWidgetItem(f"{f.get_importe()} €"))

    def rellenar_combo_citas(self, citas):
        self.cboCita.clear()
        for cita in citas:
            texto_opcion = f"Cita {cita.get_id_cita()} - {cita.get_fecha()}"
            self.cboCita.addItem(texto_opcion, cita.get_id_cita())

    def pedir_ruta_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar Factura", "", "Archivos PDF (*.pdf);;Todos los archivos (*.*)"
        )
        return ruta

    def mostrar_ruta_seleccionada(self, ruta):
        self.lblRuta.setText(ruta)

    def obtener_importe(self):
        importe_str = self.txtImporte.text().replace(',', '.')
        try:
            return float(importe_str)
        except ValueError:
            return None

    def obtener_id_cita_seleccionada(self):
        return self.cboCita.currentData()

    def limpiar_formulario(self):
        self.lblRuta.setText("(Ningún archivo seleccionado)")
        self.txtImporte.clear()

    def mostrar_aviso(self, mensaje):
        QMessageBox.warning(self, "Aviso", mensaje)

    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, "Error", mensaje)

    def mostrar_exito(self, mensaje):
        QMessageBox.information(self, "Éxito", mensaje)