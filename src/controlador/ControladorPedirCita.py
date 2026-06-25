from src.modelo.logica.ServicioCitas import ServicioCitas

class ControladorPedirCita:
    def __init__(self, vista, id_mascota, nombre_mascota):
        self.vista = vista
        self.id_mascota = id_mascota
        self.nombre_mascota = nombre_mascota
        self.servicio = ServicioCitas()

        self.vista.preparar_horas_clinica()

        if hasattr(self.vista, 'btnGuardarCita'):
            self.vista.btnGuardarCita.clicked.connect(self.procesar_cita)

    def procesar_cita(self):
        fecha, hora, motivo = self.vista.obtener_datos_cita()

        if not hora:
            self.vista.mostrar_aviso("Por favor, selecciona una hora para la cita.")
            return

        try:
            self.servicio.agendar_cita(fecha, hora, motivo, self.id_mascota)

            self.vista.mostrar_exito(
                f"Cita guardada correctamente para {self.nombre_mascota} el día {fecha} a las {hora}.")
            self.vista.ocultar_ventana()

        except Exception as e:
            self.vista.mostrar_error(str(e))