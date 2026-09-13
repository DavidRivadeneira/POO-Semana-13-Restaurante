"""Carga objetos y concentra las operaciones de usuarios y productos."""
from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:
    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio
        self._usuarios = []
        self._productos = []
        self._usuarios_por_acceso = {}
        self.cargar_datos()

    def cargar_datos(self):
        # ArchivoServicio lee diccionarios; este servicio los convierte en objetos.
        usuarios_json = self.archivo_servicio.leer_json("usuarios.json")
        productos_json = self.archivo_servicio.leer_json("productos.json")
        try:
            usuarios = [Usuario(d["identificacion"], d["nombre"], d["usuario"],
                                d["contrasena"]) for d in usuarios_json]
            productos = [Producto(d["codigo"], d["nombre"], d["precio"],
                                  d["stock"]) for d in productos_json]
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError(f"Registro inválido en los datos del restaurante: {error}") from error

        # Reutiliza la búsqueda por clave aprendida en Semana 12 para el login.
        indice = {usuario.usuario: usuario for usuario in usuarios}
        if len(indice) != len(usuarios):
            raise ValueError("Existen nombres de acceso duplicados en usuarios.json.")
        if len({u.identificacion for u in usuarios}) != len(usuarios):
            raise ValueError("Existen identificaciones duplicadas en usuarios.json.")
        if len({p.codigo for p in productos}) != len(productos):
            raise ValueError("Existen códigos duplicados en productos.json.")

        self._usuarios = usuarios
        self._productos = productos
        self._usuarios_por_acceso = indice

    def validar_acceso(self, usuario, contrasena):
        usuario = usuario.strip()
        contrasena = contrasena.strip()
        if not usuario or not contrasena:
            return None
        registrado = self._usuarios_por_acceso.get(usuario)
        if registrado is not None and registrado.contrasena == contrasena:
            return registrado
        return None

    def listar_usuarios(self):
        return self._usuarios.copy()

    def listar_productos(self):
        return self._productos.copy()

    def cantidad_usuarios(self):
        return len(self._usuarios)

    def cantidad_productos(self):
        return len(self._productos)
