from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from src.modelo.dao.MascotaDAO import MascotaDAO
from src.vista.VistaAnadirInformes2 import VistaAnadirInformes2


class ControladorAnadirInformes:
    def __init__(self, vista):
        self.vista = vista
        self.dao_mascotas = MascotaDAO()

        self.cargar_todos_los_pacientes()

        if hasattr(self.vista, 'btnVerHistorial'):
            self.vista.btnVerHistorial.clicked.connect(self.abrir_historial_paciente)

    def cargar_todos_los_pacientes(self):
        try:
            mascotas = self.dao_mascotas.obtener_todas_las_mascotas()

            self.vista.tablaBuscadorMascotas.setRowCount(0)
            self.vista.tablaBuscadorMascotas.setColumnCount(3)
            self.vista.tablaBuscadorMascotas.setHorizontalHeaderLabels(["ID", "Nombre", "Especie"])

            for fila_idx, mascota in enumerate(mascotas):
                self.vista.tablaBuscadorMascotas.insertRow(fila_idx)

                self.vista.tablaBuscadorMascotas.setItem(fila_idx, 0, QTableWidgetItem(str(mascota.get_id_mascota())))
                self.vista.tablaBuscadorMascotas.setItem(fila_idx, 1, QTableWidgetItem(mascota.get_nombre()))
                self.vista.tablaBuscadorMascotas.setItem(fila_idx, 2, QTableWidgetItem(mascota.get_especie()))
        except Exception as e:
            print(f"Error al cargar: {e}")

    def abrir_historial_paciente(self):
        fila_seleccionada = self.vista.tablaBuscadorMascotas.currentRow()

        if fila_seleccionada == -1:
            QMessageBox.warning(self.vista, "Aviso", "Por favor, selecciona un paciente de la lista.")
            return

        item_id = self.vista.tablaBuscadorMascotas.item(fila_seleccionada, 0)
        item_nombre = self.vista.tablaBuscadorMascotas.item(fila_seleccionada, 1)

        id_mascota = int(item_id.text())
        nombre_mascota = item_nombre.text()

        self.vista_historial = VistaAnadirInformes2(id_mascota, nombre_mascota)
        self.vista_historial.show()