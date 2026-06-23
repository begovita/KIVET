from src.modelo.logica.ServicioAdmin import ServicioAdmin
from src.vista.VistaAnadirFactura import VistaAnadirFactura
from src.vista.VistaValidarUsuario import VistaValidarUsuario

class ControladorAdmin:
    def __init__(self, vista, dni_admin):
        self.vista = vista
        self.dni_admin = dni_admin
        self.servicio = ServicioAdmin()
        self.conectar_botones()

    def conectar_botones(self):
        self.vista.btnValidarCuentas.clicked.connect(self.abrir_flujo_validar)
        self.vista.btnAnadirFacturas.clicked.connect(self.abrir_flujo_facturas)
        self.vista.btnTotalFacturadoMes.clicked.connect(self.procesar_facturacion)
        self.vista.btnCopiaSeguridad.clicked.connect(self.procesar_backup)
        self.vista.btnRestaurarCopia.clicked.connect(self.procesar_restore)

    def procesar_facturacion(self):
        total = self.servicio.calcular_facturacion_mensual()
        self.vista.mostrar_total(total)

    def procesar_backup(self):
        ruta = self.vista.pedir_ruta_guardado()
        if ruta:
            try:
                self.servicio.ejecutar_backup(ruta)
                self.vista.mostrar_exito("Copia realizada con éxito.")
            except Exception as e:
                self.vista.mostrar_error(f"Error: {e}")

    def procesar_restore(self):
        ruta = self.vista.pedir_ruta_lectura()
        if ruta and self.vista.confirmar_accion():
            try:
                self.servicio.ejecutar_restore(ruta)
                self.vista.mostrar_exito("Restauración completada.")
            except Exception as e:
                self.vista.mostrar_error(f"Error: {e}")

    def abrir_flujo_validar(self):
        self.vista_validar = VistaValidarUsuario(self.dni_admin)
        self.vista_validar.show()

    def abrir_flujo_facturas(self):
        self.vista_anadir_facturas = VistaAnadirFactura(self.dni_admin)
        self.vista_anadir_facturas.show()