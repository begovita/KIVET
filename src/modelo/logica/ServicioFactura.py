from src.modelo.dao.FacturaDAO import FacturaDAO

class ServicioFactura:
    def __init__(self):
        self.dao = FacturaDAO()

    def obtener_total_facturado(self):
        return self.dao.obtener_total_facturado_mes_actual()