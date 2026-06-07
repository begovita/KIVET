class FacturaVO:
    def __init__(self, id_factura, id_cita, importe, fecha=None, archivo_pdf=None):
        self._id_factura = id_factura
        self._id_cita = id_cita
        self._importe = importe
        self._fecha = fecha
        self._archivo_pdf = archivo_pdf

    def get_id_factura(self): return self._id_factura
    def get_id_cita(self): return self._id_cita
    def get_importe(self): return self._importe
    def get_fecha(self): return self._fecha
    def get_archivo_pdf(self): return self._archivo_pdf