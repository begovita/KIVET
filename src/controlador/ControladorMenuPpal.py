from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from src.modelo.dao.MascotaDAO import MascotaDAO
from src.vista.AnadirMascota import AnadirMascota
from src.controlador.ControladorAnadirMascota import ControladorAnadirMascota
from src.vista.Mascota import Mascota
from src.vista.VistaVeterinario import VistaVeterinario
from src.vista.VistaAdmin import VistaAdmin


class ControladorMenuPpal:
    def __init__(self, vista, dni_usuario, rol_usuario):
        self.vista = vista
        self.dni_usuario = dni_usuario
        self.rol_usuario = rol_usuario

        # instancio el MascotaDAO
        self.dao_mascotas = MascotaDAO()

        self.configurar_permisos()

        if hasattr(self.vista, 'btnAnadirMascota'):
            self.vista.btnAnadirMascota.clicked.connect(self.abrir_anadir_mascota)

        if hasattr(self.vista, 'btnCerrarSesion'):
            self.vista.btnCerrarSesion.clicked.connect(self.cerrar_sesion)

        if hasattr(self.vista, 'btnVerMascota'):
            self.vista.btnVerMascota.clicked.connect(self.abrir_opciones_mascota)

        if hasattr(self.vista, 'btnPanelAdmin'):
            self.vista.btnPanelAdmin.clicked.connect(self.abrir_panel_admin)

        if hasattr(self.vista, 'btnPanelVet'):
            self.vista.btnPanelVet.clicked.connect(self.abrir_panel_vet)

    #solo salen los botones de admin y vet si eres admin o vet
    def configurar_permisos(self):
        self.cargar_mascotas()

        if hasattr(self.vista, 'btnPanelAdmin'):
            self.vista.btnPanelAdmin.setVisible(False)
        if hasattr(self.vista, 'btnPanelVet'):
            self.vista.btnPanelVet.setVisible(False)

        if self.rol_usuario == "Administrativo":
            self.vista.btnPanelAdmin.setVisible(True)
        elif self.rol_usuario == "Veterinario":
            self.vista.btnPanelVet.setVisible(True)

    def cargar_mascotas(self):
        # pido los datos a mysql
        mascotas = self.dao_mascotas.obtener_mascotas_por_dni(self.dni_usuario)

        # tabla
        self.vista.tablaMascotas.setRowCount(0)
        self.vista.tablaMascotas.setColumnCount(3)
        self.vista.tablaMascotas.setHorizontalHeaderLabels(["ID", "Nombre", "Especie"])

        # se rellena la tabla
        for fila_idx, mascota in enumerate(mascotas):
            self.vista.tablaMascotas.insertRow(fila_idx)

            # columna 0 id
            item_id = QTableWidgetItem(str(mascota.get_id_mascota()))
            self.vista.tablaMascotas.setItem(fila_idx, 0, item_id)

            # columna 1 nombre
            item_nombre = QTableWidgetItem(mascota.get_nombre())
            self.vista.tablaMascotas.setItem(fila_idx, 1, item_nombre)

            # columna 2 especie
            item_especie = QTableWidgetItem(mascota.get_especie())
            self.vista.tablaMascotas.setItem(fila_idx, 2, item_especie)

    def abrir_anadir_mascota(self):
        self.vista_anadir = AnadirMascota()
        self.controlador_anadir = ControladorAnadirMascota(self.vista_anadir, self.dni_usuario, self)
        self.vista_anadir.show()

    def abrir_opciones_mascota(self):
        fila_seleccionada = self.vista.tablaMascotas.currentRow()

        if fila_seleccionada == -1:
            QMessageBox.warning(self.vista, "Aviso", "Por favor, selecciona una mascota de la tabla primero.")
            return

        # saco id y nombre en las columnas 0 y 1
        item_id = self.vista.tablaMascotas.item(fila_seleccionada, 0)
        item_nombre = self.vista.tablaMascotas.item(fila_seleccionada, 1)

        id_mascota = int(item_id.text())
        nombre_mascota = item_nombre.text()

        # le paso los datos y el propio controlador
        self.vista_opciones = Mascota(id_mascota, nombre_mascota, self)
        self.vista_opciones.show()

    def abrir_panel_admin(self):
        self.vista_admin = VistaAdmin(self.dni_usuario)
        self.vista_admin.show()


    def abrir_panel_vet(self):
        self.vista_vet = VistaVeterinario(self.dni_usuario)
        self.vista_vet.show()

    def cerrar_sesion(self):
        self.vista.close()
