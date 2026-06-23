import os
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorFacturas import ControladorFacturas

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaFacturas.ui")
Form, Window = uic.loadUiType(ruta_ui)

class Facturas(QMainWindow, Form):
    def __init__(self, id_mascota, nombre_mascota):
        super().__init__()
        self.setupUi(self)

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorFacturas(self, id_mascota, nombre_mascota)

    def rellenar_tabla_facturas(self, facturas, callback_impresion):
        self.tablaFacturas.setRowCount(0)
        self.tablaFacturas.setColumnCount(4)
        self.tablaFacturas.setHorizontalHeaderLabels(["Nº Factura", "Fecha", "Importe", "Acción"])

        for fila_idx, fac in enumerate(facturas):
            self.tablaFacturas.insertRow(fila_idx)
            self.tablaFacturas.setItem(fila_idx, 0, QTableWidgetItem(str(fac.get_id_factura())))
            self.tablaFacturas.setItem(fila_idx, 1, QTableWidgetItem(fac.get_fecha()))
            self.tablaFacturas.setItem(fila_idx, 2, QTableWidgetItem(f"{fac.get_importe()} €"))

            btn_imprimir = QPushButton("Imprimir Factura")
            id_actual = fac.get_id_factura()

            btn_imprimir.clicked.connect(lambda checked, id_fac=id_actual: callback_impresion(id_fac))

            self.tablaFacturas.setCellWidget(fila_idx, 3, btn_imprimir)

    def mostrar_mensaje_impresion(self, id_factura, nombre_mascota):
        QMessageBox.information(
            self,
            "Impresora KiVet",
            f"Conectando con la impresora.\n\nLa factura #{id_factura} de {nombre_mascota} se ha mandado a imprimir."
        )