class InformeVO:
    def __init__(self, id_documento, tipo_documento, id_mascota, fecha=None, descripcion=None):
        self._id_documento = id_documento
        self._tipo_documento = tipo_documento
        self._id_mascota = id_mascota
        self._fecha = fecha
        self._descripcion = descripcion

    def get_id_documento(self): return self._id_documento
    def get_tipo_documento(self): return self._tipo_documento
    def get_id_mascota(self): return self._id_mascota
    def get_fecha(self): return self._fecha
    def get_descripcion(self): return self._descripcion