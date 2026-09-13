"""Producto de Semana 12 adaptado a la consulta gráfica de Semana 13."""
from math import isfinite


class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @staticmethod
    def validar_texto(valor, campo):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"El campo {campo} no puede estar vacío.")
        return valor.strip()

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = self.validar_texto(valor, "código")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = self.validar_texto(valor, "nombre")

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if isinstance(valor, bool):
            raise ValueError("El precio debe ser un número válido.")
        try:
            precio = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un número válido.") from None
        if not isfinite(precio) or precio < 0:
            raise ValueError("El precio debe ser finito y no negativo.")
        self._precio = precio

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if type(valor) is not int or valor < 0:
            raise ValueError("El stock debe ser un entero no negativo.")
        self._stock = valor
