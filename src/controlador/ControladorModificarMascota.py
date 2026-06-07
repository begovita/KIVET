from PyQt5.QtWidgets import QMessageBox
from src.modelo.dao.MascotaDAO import MascotaDAO


class ControladorModificarMascota:
    def __init__(self, vista, id_mascota, nombre_actual, controlador_menu):
        self.vista = vista
        self.id_mascota = id_mascota
        self.nombre_actual = nombre_actual
        self.controlador_menu = controlador_menu
        self.dao = MascotaDAO()

        # se autorellena la caja del nombre
        self.vista.inputNombre.setText(self.nombre_actual)

        # boton de guardar cambios
        if hasattr(self.vista, 'btnGuardarCambios'):
            self.vista.btnGuardarCambios.clicked.connect(self.guardar_cambios)

    def guardar_cambios(self):
        nuevo_nombre = self.vista.inputNombre.text().strip()
        nueva_especie = self.vista.inputEspecie.text().strip()

        if not nuevo_nombre or not nueva_especie:
            QMessageBox.warning(self.vista, "Error", "Por favor, rellena todos los campos.")
            return

        try:
            # modificar la bbdd
            if self.dao.modificar(self.id_mascota, nuevo_nombre, nueva_especie):
                QMessageBox.information(self.vista, "Éxito", "Datos actualizados correctamente.")

                # se actualiza la tabla de la pagina anterior
                self.controlador_menu.cargar_mascotas()

                self.vista.hide()
            else:
                QMessageBox.critical(self.vista, "Error", "No se pudo modificar la mascota.")
        except Exception as e:
            print(f"Error al modificar {e}")