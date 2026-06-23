from src.modelo.logica.ServicioInformes import ServicioInformes

class ControladorAnadirInformes2:
    def __init__(self, vista, id_mascota, nombre_mascota):
        self.vista = vista
        self.id_mascota = id_mascota
        self.nombre_mascota = nombre_mascota
        self.servicio = ServicioInformes()
        self.ruta_archivo_seleccionado = None

        self.preparar_interfaz()

        if hasattr(self.vista, 'btnSeleccionarArchivo'):
            self.vista.btnSeleccionarArchivo.clicked.connect(self.abrir_explorador_archivos)

        if hasattr(self.vista, 'btnSubirInforme'):
            self.vista.btnSubirInforme.clicked.connect(self.procesar_nuevo_informe)

    def preparar_interfaz(self):
        self.vista.actualizar_titulo(self.nombre_mascota)
        self.cargar_tabla_historial()

    def cargar_tabla_historial(self):
        informes = self.servicio.obtener_informes_paciente(self.id_mascota)
        self.vista.rellenar_tabla_informes(informes)

    def abrir_explorador_archivos(self):
        ruta = self.vista.pedir_ruta_archivo()
        if ruta:
            self.ruta_archivo_seleccionado = ruta
            self.vista.mostrar_ruta_seleccionada(ruta)

    def procesar_nuevo_informe(self):
        if not self.ruta_archivo_seleccionado:
            self.vista.mostrar_aviso("Por favor, selecciona un archivo PDF primero.")
            return

        tipo = self.vista.obtener_tipo_informe()

        try:
            self.servicio.guardar_informe_completo(tipo, self.id_mascota, self.ruta_archivo_seleccionado)
            self.vista.mostrar_exito("El informe clínico se ha subido correctamente.")
            self.ruta_archivo_seleccionado = None
            self.vista.limpiar_formulario()
            self.cargar_tabla_historial()
        except Exception as e:
            self.vista.mostrar_error(f"Fallo al procesar el informe: {e}")