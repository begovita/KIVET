from PyQt5.QtWidgets import QMessageBox
from src.modelo.dao.MascotaDAO import MascotaDAO
from src.vista.ModificarMascota import ModificarMascota
from src.vista.PedirCita import PedirCita
from src.vista.Informes import Informes
from src.vista.Facturas import Facturas

class ControladorMascota:
    def __init__(self, vista, id_mascota, nombre_mascota, controlador_menu):
        self.vista = vista
        self.id_mascota = id_mascota
        self.nombre_mascota = nombre_mascota
        self.controlador_menu = controlador_menu
        self.dao = MascotaDAO()

        if hasattr(self.vista, 'btnEliminar'):
            self.vista.btnEliminar.clicked.connect(self.eliminar_mascota)

        if hasattr(self.vista, 'btnModificar'):
            self.vista.btnModificar.clicked.connect(self.abrir_modificar)

        if hasattr(self.vista, 'btnPedirCita'):
            self.vista.btnPedirCita.clicked.connect(self.abrir_pedir_cita)

        if hasattr(self.vista, 'btnVerInformes'):
            self.vista.btnVerInformes.clicked.connect(self.abrir_informes)

        if hasattr(self.vista, 'btnVerFacturas'):
            self.vista.btnVerFacturas.clicked.connect(self.abrir_facturas)

    def eliminar_mascota(self):
        respuesta = QMessageBox.question(self.vista, "Confirmar eliminación", f"¿Estás seguro de que quieres eliminar a {self.nombre_mascota}? Esta acción no se puede deshacer.",QMessageBox.Yes | QMessageBox.No)

        if respuesta == QMessageBox.Yes:
            if self.dao.eliminar(self.id_mascota):
                QMessageBox.information(self.vista, "Éxito", f"{self.nombre_mascota} ha sido eliminado/a.")
                self.controlador_menu.cargar_mascotas()
                # se cierra la ventana y vuelve al menu ppal
                self.vista.close()
            else:
                QMessageBox.critical(self.vista, "Error", "No se pudo eliminar la mascota.")

    def abrir_modificar(self):
        self.vista_modificar = ModificarMascota(self.id_mascota, self.nombre_mascota, self.controlador_menu)
        self.vista_modificar.show()
        # no escondo el panel, abro la ventanita encima

    def abrir_pedir_cita(self):
        self.vista_cita = PedirCita(self.id_mascota, self.nombre_mascota)
        self.vista_cita.show()

    def abrir_informes(self):
        self.vista_informes = Informes(self.id_mascota, self.nombre_mascota)
        self.vista_informes.show()

    def abrir_facturas(self):
        self.vista_facturas = Facturas(self.id_mascota, self.nombre_mascota)
        self.vista_facturas.show()