from src.modelo.logica.ServicioMascota import ServicioMascota
from src.vista.VistaAnadirInformes2 import VistaAnadirInformes2

class ControladorAnadirInformes:
    def __init__(self, vista):
        self.vista = vista
        self.servicio = ServicioMascota() # reutilizo el servidio

        self.cargar_todos_los_pacientes()

        if hasattr(self.vista, 'btnVerHistorial'):
            self.vista.btnVerHistorial.clicked.connect(self.abrir_historial_paciente)

    def cargar_todos_los_pacientes(self):
        mascotas = self.servicio.obtener_lista_mascotas()
        self.vista.rellenar_tabla_mascotas(mascotas)

    def abrir_historial_paciente(self):
        fila = self.vista.obtener_fila_seleccionada()

        if fila == -1:
            self.vista.mostrar_aviso_seleccion()
            return

        id_mascota, nombre = self.vista.obtener_datos_fila(fila)

        self.vista_historial = VistaAnadirInformes2(id_mascota, nombre)
        self.vista_historial.show()