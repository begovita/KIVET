from src.modelo.logica.ServicioMascota import ServicioMascota
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

        self.servicio = ServicioMascota()

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

    def configurar_permisos(self):
        self.cargar_mascotas()
        self.vista.aplicar_permisos(self.rol_usuario)

    def cargar_mascotas(self):
        mascotas = self.servicio.obtener_mascotas_dueno(self.dni_usuario)
        self.vista.rellenar_tabla_mascotas(mascotas)

    def abrir_anadir_mascota(self):
        self.vista_anadir = AnadirMascota()
        self.controlador_anadir = ControladorAnadirMascota(self.vista_anadir, self.dni_usuario, self)
        self.vista_anadir.show()

    def abrir_opciones_mascota(self):
        fila = self.vista.obtener_fila_seleccionada()

        if fila == -1:
            self.vista.mostrar_aviso("Por favor, selecciona una mascota de la tabla primero.")
            return

        id_mascota, nombre_mascota = self.vista.obtener_datos_fila(fila)

        self.vista_opciones = Mascota(id_mascota, nombre_mascota, self)
        self.vista_opciones.show()

    def abrir_panel_admin(self):
        self.vista_admin = VistaAdmin(self.dni_usuario)
        self.vista_admin.show()

    def abrir_panel_vet(self):
        self.vista_vet = VistaVeterinario(self.dni_usuario)
        self.vista_vet.show()

    def cerrar_sesion(self):
        self.vista.cerrar_ventana()