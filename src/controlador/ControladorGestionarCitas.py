from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from src.modelo.dao.CitaDAO import CitaDAO
from src.vista.VistaGestionarCitas2 import VistaGestionarCitas2


class ControladorGestionarCitas:
    def __init__(self, vista):
        self.vista = vista
        self.dao_citas = CitaDAO()

        # conectar el clic en el calendario para que recargue la tabla
        if hasattr(self.vista, 'calendarioCitas'):
            self.vista.calendarioCitas.selectionChanged.connect(self.cargar_citas_del_dia)

        # boton
        if hasattr(self.vista, 'btnModificarCita'):
            self.vista.btnModificarCita.clicked.connect(self.abrir_edicion_cita)

        self.cargar_citas_del_dia()

    def cargar_citas_del_dia(self):
        try:
            fecha_qt = self.vista.calendarioCitas.selectedDate()
            fecha_str = fecha_qt.toString("yyyy-MM-dd")

            citas = self.dao_citas.obtener_citas_por_fecha(fecha_str)

            self.vista.tablaCitasVet.setRowCount(0)
            self.vista.tablaCitasVet.setColumnCount(4)
            self.vista.tablaCitasVet.setHorizontalHeaderLabels(["ID Cita", "Hora", "Mascota", "Motivo"])

            for fila_idx, cita in enumerate(citas):
                self.vista.tablaCitasVet.insertRow(fila_idx)

                self.vista.tablaCitasVet.setItem(fila_idx, 0, QTableWidgetItem(str(cita["id_cita"])))
                self.vista.tablaCitasVet.setItem(fila_idx, 1, QTableWidgetItem(cita["hora"]))
                self.vista.tablaCitasVet.setItem(fila_idx, 2, QTableWidgetItem(cita["nombre_mascota"]))
                self.vista.tablaCitasVet.setItem(fila_idx, 3, QTableWidgetItem(cita["motivo"]))

        except Exception as e:
            print(f"Error en cargar_citas_del_dia: {e}")

    def abrir_edicion_cita(self):
        fila_seleccionada = self.vista.tablaCitasVet.currentRow()

        if fila_seleccionada == -1:
            QMessageBox.warning(self.vista, "Aviso", "Selecciona una cita de la tabla para modificarla.")
            return

        item_id = self.vista.tablaCitasVet.item(fila_seleccionada, 0)
        item_mascota = self.vista.tablaCitasVet.item(fila_seleccionada, 2)

        id_cita = int(item_id.text())
        nombre_mascota = item_mascota.text()

        self.vista_editor = VistaGestionarCitas2(id_cita, nombre_mascota)
        self.vista_editor.show()