from PyQt5.QtWidgets import QMessageBox
from src.modelo.vo.MascotaVO import MascotaVO
from src.modelo.dao.MascotaDAO import MascotaDAO


class ControladorAnadirMascota:
    # lo recibe to para actualizar la tabla
    def __init__(self, vista, dni_dueno, controlador_menu):
        self.vista = vista
        self.dni_dueno = dni_dueno
        self.controlador_menu = controlador_menu
        self.dao = MascotaDAO()

        # boton de guardar
        self.vista.btnGuardarMascota.clicked.connect(self.guardar_mascota)

    def guardar_mascota(self):
        nombre = self.vista.inputNombre.text().strip()
        especie = self.vista.inputEspecie.text().strip()

        if not nombre or not especie:
            QMessageBox.warning(self.vista, "Error", "Por favor, rellena nombre y especie.")
            return

        # empaqueto en el VO
        # ID es None porque MySQL lo genera solo
        nueva_mascota = MascotaVO(nombre, especie, self.dni_dueno)

        if self.dao.insertar(nueva_mascota):
            QMessageBox.information(self.vista, "Éxito", "Mascota añadida correctamente.")

            # actualizar la tabla
            self.controlador_menu.cargar_mascotas()

            # cerrar la ventana
            self.vista.close()
        else:
            QMessageBox.critical(self.vista, "Error", "No se pudo guardar la mascota.")