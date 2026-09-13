"""Lee JSON locales; no construye vistas ni aplica reglas del restaurante."""
import json
from pathlib import Path


class ArchivoServicio:
    def __init__(self, carpeta_datos):
        self.carpeta_datos = Path(carpeta_datos)

    def leer_json(self, nombre_archivo):
        ruta = self.carpeta_datos / nombre_archivo
        try:
            with ruta.open("r", encoding="utf-8-sig") as archivo:
                datos = json.load(archivo)
        except (OSError, ValueError) as error:
            raise ValueError(f"No se pudo leer {nombre_archivo}: {error}") from error
        if not isinstance(datos, list) or any(not isinstance(fila, dict) for fila in datos):
            raise ValueError(f"{nombre_archivo} debe contener una lista de registros.")
        return datos
