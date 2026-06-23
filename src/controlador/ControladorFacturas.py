from src.modelo.logica.ServicioFacturacion import ServicioFacturacion

class ControladorFacturas:
    def __init__(self, vista, id_mascota, nombre_mascota):
        self.vista = vista
        self.id_mascota = id_mascota
        self.nombre_mascota = nombre_mascota

        self.servicio = ServicioFacturacion()

        self.cargar_tabla_facturas()

    def cargar_tabla_facturas(self):
        facturas = self.servicio.obtener_facturas_paciente(self.id_mascota)


        self.vista.rellenar_tabla_facturas(facturas, self.procesar_impresion)

    def procesar_impresion(self, id_factura):
        self.vista.mostrar_mensaje_impresion(id_factura, self.nombre_mascota)