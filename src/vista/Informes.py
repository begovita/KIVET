import os
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from src.controlador.ControladorInformes import ControladorInformes

directorio_actual = os.path.dirname(__file__)
ruta_ui = os.path.join(directorio_actual, "ui", "VistaInformes.ui")
Form, Window = uic.loadUiType(ruta_ui)

class Informes(QMainWindow, Form):
    def __init__(self, id_mascota, nombre_mascota):
        super().__init__()
        self.setupUi(self)

        ruta_imagen = os.path.join(directorio_actual, "imagenes", "logoKiVet.jpg")
        if hasattr(self, 'label_3'):
            if os.path.exists(ruta_imagen):
                self.label_3.setPixmap(QPixmap(ruta_imagen))
                self.label_3.setScaledContents(True)

        self.controlador = ControladorInformes(self, id_mascota, nombre_mascota)

    def rellenar_tabla_informes(self, informes, callback_impresion):
        self.tablaInformes.setRowCount(0)
        self.tablaInformes.setColumnCount(4)
        self.tablaInformes.setHorizontalHeaderLabels(["ID", "Fecha", "Descripción", "Acción"])

        for fila_idx, inf in enumerate(informes):
            self.tablaInformes.insertRow(fila_idx)
            self.tablaInformes.setItem(fila_idx, 0, QTableWidgetItem(str(inf.get_id_documento())))
            self.tablaInformes.setItem(fila_idx, 1, QTableWidgetItem(inf.get_fecha()))
            self.tablaInformes.setItem(fila_idx, 2, QTableWidgetItem(inf.get_descripcion()))

            btn_imprimir = QPushButton("Imprimir")
            id_actual = inf.get_id_documento()

            btn_imprimir.clicked.connect(lambda checked, id_inf=id_actual: callback_impresion(id_inf))

            self.tablaInformes.setCellWidget(fila_idx, 3, btn_imprimir)

    def mostrar_mensaje_impresion(self, id_informe, nombre_mascota):
        QMessageBox.information(
            self,
            "Impresora KiVet",
            f"Conectando con la impresora.\n\nEl informe clínico #{id_informe} de {nombre_mascota} se ha mandado a imprimir."
        )