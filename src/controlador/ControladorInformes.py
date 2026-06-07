from PyQt5.QtWidgets import QTableWidgetItem, QPushButton, QMessageBox
from src.modelo.dao.InformeDAO import InformeDAO

class ControladorInformes:
    def __init__(self, vista, id_mascota, nombre_mascota):
        self.vista = vista
        self.id_mascota = id_mascota
        self.nombre_mascota = nombre_mascota
        self.dao = InformeDAO()

        self.cargar_tabla_informes()

    def cargar_tabla_informes(self):
        informes = self.dao.obtener_por_mascota(self.id_mascota)

        self.vista.tablaInformes.setRowCount(0)
        self.vista.tablaInformes.setColumnCount(4)
        self.vista.tablaInformes.setHorizontalHeaderLabels(["ID", "Fecha", "Descripción", "Acción"])

        for fila_idx, inf in enumerate(informes):
            self.vista.tablaInformes.insertRow(fila_idx)

            self.vista.tablaInformes.setItem(fila_idx, 0, QTableWidgetItem(str(inf.get_id_documento())))
            self.vista.tablaInformes.setItem(fila_idx, 1, QTableWidgetItem(inf.get_fecha()))
            self.vista.tablaInformes.setItem(fila_idx, 2, QTableWidgetItem(inf.get_descripcion()))

            btn_imprimir = QPushButton("Imprimir")
            id_actual = inf.get_id_documento()
            btn_imprimir.clicked.connect(lambda checked, id_inf=id_actual: self.ejecutar_impresion(id_inf))

            self.vista.tablaInformes.setCellWidget(fila_idx, 3, btn_imprimir)

    def ejecutar_impresion(self, id_informe):
        QMessageBox.information(
            self.vista,
            "Impresora KiVet",
            f"Conectando con la impresora.\n\nEl informe clínico #{id_informe} de {self.nombre_mascota} se ha mandado a imprimir."
        )