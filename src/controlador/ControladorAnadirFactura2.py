from src.modelo.logica.ServicioFacturacion import ServicioFacturacion

class ControladorAnadirFactura2:
    def __init__(self, vista, dni_admin, id_mascota, nombre_mascota):
        self.vista = vista
        self.dni_admin = dni_admin
        self.id_mascota = id_mascota
        self.nombre_mascota = nombre_mascota

        self.servicio = ServicioFacturacion()
        self.ruta_archivo_seleccionado = None

        self.preparar_interfaz()

        if hasattr(self.vista, 'btnSeleccionarArchivo'):
            self.vista.btnSeleccionarArchivo.clicked.connect(self.abrir_explorador)

        if hasattr(self.vista, 'btnSubirFactura'):
            self.vista.btnSubirFactura.clicked.connect(self.procesar_factura)

    def preparar_interfaz(self):
        self.vista.actualizar_titulo(self.nombre_mascota)
        self.cargar_tabla_facturas()
        self.cargar_desplegable_citas()

    def cargar_tabla_facturas(self):
        facturas = self.servicio.obtener_facturas_paciente(self.id_mascota)
        self.vista.rellenar_tabla_facturas(facturas)

    def cargar_desplegable_citas(self):
        citas = self.servicio.obtener_citas_paciente(self.id_mascota)
        self.vista.rellenar_combo_citas(citas)

    def abrir_explorador(self):
        ruta = self.vista.pedir_ruta_archivo()
        if ruta:
            self.ruta_archivo_seleccionado = ruta
            self.vista.mostrar_ruta_seleccionada(ruta)

    def procesar_factura(self):
        if not self.ruta_archivo_seleccionado:
            self.vista.mostrar_aviso("Selecciona un archivo PDF.")
            return

        importe = self.vista.obtener_importe()
        if importe is None:
            self.vista.mostrar_aviso("El importe debe ser un número válido.")
            return

        id_cita = self.vista.obtener_id_cita_seleccionada()
        if id_cita is None:
            self.vista.mostrar_aviso("No hay citas seleccionadas.")
            return

        try:
            self.servicio.guardar_factura_completa(id_cita, importe, self.ruta_archivo_seleccionado)
            self.vista.mostrar_exito("Factura procesada correctamente.")
            self.ruta_archivo_seleccionado = None
            self.vista.limpiar_formulario()
            self.cargar_tabla_facturas()
        except Exception as e:
            self.vista.mostrar_error(f"Fallo al procesar la factura: {e}")