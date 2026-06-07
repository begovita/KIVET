class MascotaVO:
    def __init__(self, nombre, especie, dni_dueno, id_mascota=None):
        self._id_mascota = id_mascota
        self._nombre = nombre
        self._especie = especie
        self._dni_dueno = dni_dueno

    # getters
    def get_id_mascota(self): return self._id_mascota
    def get_nombre(self): return self._nombre
    def get_especie(self): return self._especie
    def get_dni_dueno(self): return self._dni_dueno

    # setters
    def set_id_mascota(self, id_mascota): self._id_mascota = id_mascota
    def set_nombre(self, nombre): self._nombre = nombre
    def set_especie(self, especie): self._especie = especie
    def set_dni_dueno(self, dni_dueno): self._dni_dueno = dni_dueno

    def __str__(self):
        return f"MascotaVO(ID: {self._id_mascota}, Nombre: {self._nombre}, Especie: {self._especie})"