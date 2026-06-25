from src.modelo.logica.ServicioMascota import ServicioMascota
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

        self.servicio = ServicioMascota()

        if hasattr(self.vista, 'btnEliminar'):
            self.vista.btnEliminar.clicked.connect(self.procesar_eliminacion)

        if hasattr(self.vista, 'btnModificar'):
            self.vista.btnModificar.clicked.connect(self.abrir_modificar)

        if hasattr(self.vista, 'btnPedirCita'):
            self.vista.btnPedirCita.clicked.connect(self.abrir_pedir_cita)

        if hasattr(self.vista, 'btnVerInformes'):
            self.vista.btnVerInformes.clicked.connect(self.abrir_informes)

        if hasattr(self.vista, 'btnVerFacturas'):
            self.vista.btnVerFacturas.clicked.connect(self.abrir_facturas)

    def procesar_eliminacion(self):
        if self.vista.confirmar_eliminacion(self.nombre_mascota):
            try:
                self.servicio.eliminar_mascota(self.id_mascota)

                self.vista.mostrar_exito(f"{self.nombre_mascota} ha sido eliminado/a.")
                self.controlador_menu.cargar_mascotas()
                self.vista.cerrar_ventana()
            except Exception as e:
                self.vista.mostrar_error(str(e))

    def abrir_modificar(self):
        self.vista_modificar = ModificarMascota(self.id_mascota, self.nombre_mascota, self.controlador_menu)
        self.vista_modificar.show()

    def abrir_pedir_cita(self):
        self.vista_cita = PedirCita(self.id_mascota, self.nombre_mascota)
        self.vista_cita.show()

    def abrir_informes(self):
        self.vista_informes = Informes(self.id_mascota, self.nombre_mascota)
        self.vista_informes.show()

    def abrir_facturas(self):
        self.vista_facturas = Facturas(self.id_mascota, self.nombre_mascota)
        self.vista_facturas.show()