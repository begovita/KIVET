from src.modelo.logica.ServicioMascota import ServicioMascota
from src.vista.VistaAnadirFactura2 import VistaAnadirFactura2

class ControladorAnadirFactura:
    def __init__(self, vista, dni_admin):
        self.vista = vista
        self.dni_admin = dni_admin
        self.servicio = ServicioMascota()  # Usamos el servicio

        self.cargar_todos_los_pacientes()

        if hasattr(self.vista, 'btnVerFacturas'):
            self.vista.btnVerFacturas.clicked.connect(self.abrir_facturacion_paciente)

    def cargar_todos_los_pacientes(self):
        mascotas = self.servicio.obtener_lista_mascotas()
        self.vista.rellenar_tabla_mascotas(mascotas)

    def abrir_facturacion_paciente(self):
        fila = self.vista.obtener_fila_seleccionada()

        if fila == -1:
            self.vista.mostrar_aviso_seleccion()
            return

        id_mascota, nombre = self.vista.obtener_datos_fila(fila)
        self.vista_factura2 = VistaAnadirFactura2(self.dni_admin, id_mascota, nombre)
        self.vista_factura2.show()