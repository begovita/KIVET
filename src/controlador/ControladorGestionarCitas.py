from src.modelo.logica.ServicioCitas import ServicioCitas
from src.vista.VistaGestionarCitas2 import VistaGestionarCitas2


class ControladorGestionarCitas:
    def __init__(self, vista):
        self.vista = vista
        self.servicio = ServicioCitas()

        if hasattr(self.vista, 'calendarioCitas'):
            self.vista.calendarioCitas.selectionChanged.connect(self.procesar_cambio_fecha)

        if hasattr(self.vista, 'btnModificarCita'):
            self.vista.btnModificarCita.clicked.connect(self.abrir_edicion_cita)

        self.procesar_cambio_fecha()

    def procesar_cambio_fecha(self):
        fecha_str = self.vista.obtener_fecha_texto()

        try:
            citas = self.servicio.obtener_citas_dia(fecha_str)
            self.vista.rellenar_tabla_citas(citas)
        except Exception as e:
            print(f"Error en procesar_cambio_fecha: {e}")

    def abrir_edicion_cita(self):
        fila = self.vista.obtener_fila_seleccionada()

        if fila == -1:
            self.vista.mostrar_aviso("Selecciona una cita de la tabla para modificarla.")
            return

        id_cita, nombre_mascota = self.vista.obtener_datos_cita(fila)

        self.vista_editor = VistaGestionarCitas2(id_cita, nombre_mascota)
        self.vista_editor.show()