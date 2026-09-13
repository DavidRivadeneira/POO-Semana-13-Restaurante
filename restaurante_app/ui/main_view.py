"""Panel de consulta. Toda la información se solicita a RestauranteServicio."""
import tkinter as tk
from tkinter import messagebox, ttk


class MainView(tk.Frame):
    def __init__(self, master, restaurante_servicio, usuario_actual, al_cerrar_sesion):
        super().__init__(master, bg="#f5f1eb")
        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.al_cerrar_sesion = al_cerrar_sesion
        self.definir_estilos()
        self.construir_interfaz()

    def definir_estilos(self):
        estilo = ttk.Style(self)
        estilo.configure("Menu.TButton", background="#eadbc9", foreground="#472d23",
                         font=("Arial", 10, "bold"), padding=(10, 8))
        estilo.map("Menu.TButton", background=[("active", "#dcc5ac")])
        estilo.configure("Cerrar.TButton", background="#9a431f", foreground="white",
                         font=("Arial", 10, "bold"), padding=(10, 8))
        estilo.map("Cerrar.TButton", background=[("active", "#773318")])

    def construir_interfaz(self):
        encabezado = tk.Frame(self, bg="#472d23", padx=26, pady=20)
        encabezado.pack(fill="x")
        tk.Label(encabezado, text="RESTAURANTE APP", bg="#472d23", fg="white",
                 font=("Arial", 20, "bold")).pack(anchor="w")
        tk.Label(encabezado, text=f"Bienvenido/a, {self.usuario_actual.nombre}",
                 bg="#472d23", fg="#f0dcc6", font=("Arial", 11)).pack(anchor="w", pady=(6, 0))

        barra = tk.Frame(self, bg="#eadbc9", padx=18, pady=10)
        barra.pack(fill="x")
        self.boton_productos = self.crear_boton_menu(barra, "Productos", self.mostrar_productos)
        self.boton_usuarios = self.crear_boton_menu(barra, "Usuarios", self.mostrar_usuarios)
        self.boton_ventas = self.crear_boton_menu(barra, "Ventas (pendiente)",
                                                 self.mostrar_funcionalidad_pendiente)
        self.boton_cerrar = ttk.Button(barra, text="Cerrar sesión", style="Cerrar.TButton",
                                       command=self.cerrar_sesion)
        self.boton_cerrar.pack(side="right")

        # Se reserva primero el pie para mantener visibles los conteos.
        self.crear_barra_estado()
        self.contenido = tk.Frame(self, bg="#f5f1eb", padx=26, pady=24)
        self.contenido.pack(fill="both", expand=True)
        self.mostrar_inicio()

    def crear_boton_menu(self, contenedor, texto, comando):
        boton = ttk.Button(contenedor, text=texto, command=comando, style="Menu.TButton")
        boton.pack(side="left", padx=(0, 8))
        return boton

    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def crear_titulo_seccion(self, texto):
        tk.Label(self.contenido, text=texto, bg="#f5f1eb", fg="#472d23",
                 font=("Arial", 18, "bold")).pack(anchor="w", pady=(0, 14))

    def crear_fila_informacion(self, texto):
        fila = tk.Frame(self.contenido, bg="white", padx=14, pady=12)
        fila.pack(fill="x", pady=(0, 8))
        tk.Label(fila, text=texto, bg="white", fg="#472d23", justify="left",
                 wraplength=570, font=("Arial", 11)).pack(anchor="w")

    def mostrar_inicio(self):
        self.limpiar_contenido()
        self.crear_titulo_seccion("Panel principal")
        self.crear_fila_informacion("Selecciona Productos o Usuarios para consultar los registros.")
        self.crear_fila_informacion("Las ventas se incorporarán en una próxima etapa.")

    def mostrar_productos(self):
        self.limpiar_contenido()
        self.crear_titulo_seccion("Productos registrados")
        productos = self.restaurante_servicio.listar_productos()
        if not productos:
            self.crear_fila_informacion("No hay productos registrados.")
        for producto in productos:
            self.crear_fila_informacion(
                f"{producto.codigo} - {producto.nombre} | "
                f"Precio: ${producto.precio:.2f} | Stock: {producto.stock}"
            )

    def mostrar_usuarios(self):
        self.limpiar_contenido()
        self.crear_titulo_seccion("Usuarios registrados")
        usuarios = self.restaurante_servicio.listar_usuarios()
        if not usuarios:
            self.crear_fila_informacion("No hay usuarios registrados.")
        for usuario in usuarios:
            self.crear_fila_informacion(
                f"{usuario.identificacion} - {usuario.nombre} | Usuario: {usuario.usuario}"
            )

    def crear_barra_estado(self):
        barra = tk.Frame(self, bg="#eadbc9", padx=18, pady=10)
        barra.pack(fill="x", side="bottom")
        tk.Label(barra, bg="#eadbc9", fg="#472d23", font=("Arial", 10),
                 text=f"Productos: {self.restaurante_servicio.cantidad_productos()} | "
                      f"Usuarios: {self.restaurante_servicio.cantidad_usuarios()}").pack(side="left")

    def mostrar_funcionalidad_pendiente(self):
        messagebox.showinfo("Ventas pendientes",
                            "Las ventas se incorporarán en una próxima etapa.",
                            parent=self)

    def cerrar_sesion(self):
        self.al_cerrar_sesion()
