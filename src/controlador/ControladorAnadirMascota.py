from src.modelo.logica.ServicioMascota import ServicioMascota


class ControladorAnadirMascota:
    def __init__(self, vista, dni_dueno, controlador_menu):
        self.vista = vista
        self.dni_dueno = dni_dueno
        self.controlador_menu = controlador_menu
        self.servicio = ServicioMascota()

        self.vista.btnGuardarMascota.clicked.connect(self.procesar_guardado)

    def procesar_guardado(self):
        nombre, especie = self.vista.obtener_datos_mascota()

        if not nombre or not especie:
            self.vista.mostrar_aviso("Por favor, rellena nombre y especie.")
            return

        try:
            self.servicio.anadir_mascota(nombre, especie, self.dni_dueno)
            self.vista.mostrar_exito("Mascota añadida correctamente.")

            self.controlador_menu.cargar_mascotas()

            self.vista.cerrar_ventana()

        except Exception as e:
            self.vista.mostrar_error(str(e))