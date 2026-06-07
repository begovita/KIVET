class UsuarioVO:
    def __init__(self, dni, contrasena, nombre, rol, estado="Pendiente"):
        self._dni = dni
        self._contrasena = contrasena
        self._nombre = nombre
        self._rol = rol
        self._estado = estado

    # getters
    def get_dni(self): return self._dni
    def get_contrasena(self): return self._contrasena
    def get_nombre(self): return self._nombre
    def get_rol(self): return self._rol
    def get_estado(self): return self._estado

    # setters
    def set_dni(self, dni): self._dni = dni
    def set_contrasena(self, contrasena): self._contrasena = contrasena
    def set_nombre(self, nombre): self._nombre = nombre
    def set_rol(self, rol): self._rol = rol
    def set_estado(self, estado): self._estado = estado

    def __str__(self):
        return f"UsuarioVO(DNI: {self._dni}, Nombre: {self._nombre}, Rol: {self._rol}, Estado: {self._estado})"