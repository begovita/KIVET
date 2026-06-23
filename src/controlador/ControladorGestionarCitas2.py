from src.modelo.logica.ServicioCitas import ServicioCitas


class ControladorGestionarCitas2:
    def __init__(self, vista, id_cita, nombre_mascota):
        self.vista = vista
        self.id_cita = id_cita
        self.nombre_mascota = nombre_mascota
        self.servicio = ServicioCitas()

        self.preparar_interfaz()

        if hasattr(self.vista, 'btnGuardarCambios'):
            self.vista.btnGuardarCambios.clicked.connect(self.procesar_cambio)

    def preparar_interfaz(self):
        self.vista.actualizar_titulo(self.nombre_mascota)
        self.vista.cargar_horas_disponibles()

        telefono_dueno = self.servicio.obtener_telefono(self.id_cita)
        self.vista.mostrar_advertencia_telefono(telefono_dueno)

    def procesar_cambio(self):
        nueva_fecha = self.vista.obtener_nueva_fecha()
        nueva_hora = self.vista.obtener_nueva_hora()

        try:
            self.servicio.modificar_cita_paciente(self.id_cita, nueva_fecha, nueva_hora)

            telefono = self.servicio.obtener_telefono(self.id_cita)
            mensaje = f"La cita ha sido cambiada al día {nueva_fecha} a las {nueva_hora}.\n\nRECUERDA: Llama ahora al {telefono} para informar del cambio."

            self.vista.mostrar_exito("Cita Actualizada", mensaje)
            self.vista.cerrar_ventana()
        except Exception as e:
            self.vista.mostrar_error(str(e))