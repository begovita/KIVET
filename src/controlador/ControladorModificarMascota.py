from src.modelo.logica.ServicioMascota import ServicioMascota

class ControladorModificarMascota:
    def __init__(self, vista, id_mascota, nombre_actual, controlador_menu):
        self.vista = vista
        self.id_mascota = id_mascota
        self.nombre_actual = nombre_actual
        self.controlador_menu = controlador_menu
        self.servicio = ServicioMascota()

        self.vista.cargar_datos_actuales(self.nombre_actual)

        if hasattr(self.vista, 'btnGuardarCambios'):
            self.vista.btnGuardarCambios.clicked.connect(self.procesar_modificacion)

    def procesar_modificacion(self):
        nuevo_nombre, nueva_especie = self.vista.obtener_nuevos_datos()

        if not nuevo_nombre or not nueva_especie:
            self.vista.mostrar_aviso("Por favor, rellena todos los campos.")
            return

        try:
            self.servicio.modificar_mascota(self.id_mascota, nuevo_nombre, nueva_especie)

            self.vista.mostrar_exito("Datos actualizados correctamente.")
            self.controlador_menu.cargar_mascotas()
            self.vista.ocultar_ventana()

        except Exception as e:
            self.vista.mostrar_error(f"Error al modificar: {e}")