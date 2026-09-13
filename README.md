# Restaurante App · Semana 13

**Taller práctico: Organización modular de un sistema orientado a objetos en Python**

**Tema:** Conceptos fundamentales de interfaces gráficas de usuario.

| Dato académico | Información |
| --- | --- |
| Estudiante | Juan David Rivadeneira Cuascota |
| Universidad | Universidad Estatal Amazónica |
| Asignatura | Programación Orientada a Objetos |
| Semestre | Segundo semestre |
| Paralelo | F |
| Código del curso | 2626-UEA-L-UFB-030-F |
| Semana | 13 |

## Propósito

Esta versión incorpora una interfaz gráfica inicial con **Tkinter** a
`restaurante_app`. Permite iniciar una sesión simulada, consultar productos y
usuarios cargados desde JSON y cerrar la sesión dentro de la misma ventana.

La organización adapta el proyecto docente Biblioteca App: `Libro` pasa a ser
`Producto`, `BibliotecaServicio` se adapta como `RestauranteServicio` y se añade
la carpeta `ui/`. Las vistas presentan información y reciben eventos; los
servicios mantienen las operaciones y la lectura de archivos.

## Continuidad con la Semana 12

- Se conservan los tres productos, sus códigos, nombres, precios y stock.
- Se conserva el usuario `U001 - ana`, con sus campos `identificacion` y `nombre`.
  Se añaden `usuario` y `contrasena` para el acceso pedagógico de esta semana.
- Se mantienen los constructores tradicionales, las propiedades y las
  validaciones de los modelos. `Producto` conserva sus cuatro atributos.
- Las listas contienen objetos y el servicio devuelve copias de las listas.
  El acceso utiliza un diccionario por nombre de usuario, aplicando la búsqueda
  por clave estudiada en Semana 12. Este índice se construye al cargar los datos.
- La conversión de diccionarios a objetos se concentra ahora en
  `RestauranteServicio`, siguiendo la distribución de responsabilidades docente.
  `ArchivoServicio` se dedica a leer los JSON.

Esta entrega es una **base gráfica simplificada e independiente**. Incluye
únicamente los modelos `Producto` y `Usuario`. La venta completa, el registro y
la edición de datos quedan para próximas semanas. La versión de consola de
Semana 12 permanece en su carpeta; sus ventas históricas no se importan aquí.
El botón **Ventas (pendiente)** solo informa que la función se incorporará después.

## Estructura

```text
Repositorio/
├── README.md
├── .gitignore
└── restaurante_app/
    ├── README.md
    ├── main.py
    ├── datos/
    │   ├── productos.json
    │   └── usuarios.json
    ├── modelos/
    │   ├── __init__.py
    │   ├── producto.py
    │   └── usuario.py
    ├── servicios/
    │   ├── __init__.py
    │   ├── archivo_servicio.py
    │   └── restaurante_servicio.py
    └── ui/
        ├── __init__.py
        ├── login_view.py
        └── main_view.py
```

| Archivo o capa | Responsabilidad |
| --- | --- |
| `modelos/producto.py` | Representar código, nombre, precio y stock; validar sus valores. |
| `modelos/usuario.py` | Representar identificación, nombre y credenciales de demostración. |
| `servicios/archivo_servicio.py` | Leer y validar la estructura básica de los archivos JSON locales. |
| `servicios/restaurante_servicio.py` | Convertir registros en objetos, validar el acceso, listar usuarios y productos y consultar sus cantidades. |
| `ui/login_view.py` | Mostrar los campos de acceso, recibir la acción de ingreso y presentar mensajes. |
| `ui/main_view.py` | Consultar el servicio y mostrar productos, usuarios, conteos y la opción pendiente de ventas. |
| `main.py` | Crear `AplicacionRestaurante`, preparar los servicios y coordinar las vistas dentro de una única ventana. |

## Flujo de la aplicación

```text
main.py → Tkinter + ArchivoServicio + RestauranteServicio
        → LoginView
        → ingreso de usuario y contraseña
        → RestauranteServicio.validar_acceso()
            ├── datos vacíos o incorrectos → mensaje en LoginView
            └── acceso correcto → MainView
                                  ├── Productos registrados
                                  ├── Usuarios registrados
                                  ├── Ventas (pendiente)
                                  └── Cerrar sesión → LoginView
```

`AplicacionRestaurante` crea una sola instancia de `Tk()` y ejecuta un solo
`mainloop()`. `cambiar_vista()` destruye el `Frame` anterior y muestra el nuevo.
Los servicios se preparan una vez y se comparten entre las vistas.

`LoginView` utiliza `Label`, `Entry` y `ttk.Button`. La contraseña se muestra con
asteriscos. Un clic en **Iniciar sesión**, o la tecla **Enter** dentro de los
campos, solicita la validación. Los campos vacíos y las credenciales incorrectas
producen mensajes visibles sin salir del login.

`MainView` muestra una bienvenida, botones de consulta y el número de productos
y usuarios. Las consultas se presentan como filas sencillas con etiquetas,
siguiendo el alcance introductorio docente. El listado de usuarios muestra
identificación, nombre y usuario de acceso. Al cerrar sesión se crean campos vacíos.

## Requisitos y ejecución

Se necesita **Python 3.10 o superior con Tkinter** y un entorno de escritorio.
La aplicación utiliza únicamente la biblioteca estándar; no requiere instalar
paquetes con `pip`.

Desde la raíz del repositorio:

```powershell
python restaurante_app/main.py
```

Desde la carpeta de la aplicación:

```powershell
cd restaurante_app
python main.py
```

En Windows se puede sustituir `python` por `py`:

```powershell
py restaurante_app/main.py
```

Para comprobar que la instalación dispone de Tkinter, ejecutar
`python -m tkinter`: debe abrir una ventana de demostración. Si falta el módulo,
habilitar el componente Tcl/Tk de la instalación de Python.

Las rutas de los JSON se calculan desde la ubicación de `main.py`; también puede
ejecutarse indicando su ruta completa desde otra carpeta. Para terminar la
aplicación, cerrar la ventana con **X**. **Cerrar sesión** regresa al login.

### Credenciales de demostración

| Usuario | Contraseña | Identificación |
| --- | --- | --- |
| `ana` | `1234` | `U001` |

El acceso es una **simulación pedagógica local**. La contraseña incluida es un
dato de prueba almacenado en JSON en texto plano. Los asteriscos solo ocultan
los caracteres del campo; esta práctica no implementa autenticación real.

### Datos incluidos

| Código | Producto | Precio | Stock |
| --- | --- | ---: | ---: |
| P001 | Hamburguesa | $3.50 | 8 |
| P002 | Jugo natural | $1.50 | 12 |
| P003 | Salchipapa | $2.75 | 5 |

`productos.json` contiene `codigo`, `nombre`, `precio` y `stock`.
`usuarios.json` contiene `identificacion`, `nombre`, `usuario` y `contrasena`.
Los datos se cargan al iniciar. Esta versión solo consulta información: no cambia
los JSON ni descuenta existencias. Si se editan los archivos, se debe reiniciar
la aplicación para volver a cargarlos.

Una colección vacía se muestra con un mensaje y cantidad cero. Si no hay usuarios,
ninguna credencial permite ingresar. Un archivo ausente, dañado o con registros
inválidos impide el inicio y se informa mediante un mensaje. También se rechazan
códigos, identificaciones y nombres de acceso duplicados.

## Comprobación del funcionamiento

| Paso | Acción | Resultado esperado |
| --- | --- | --- |
| 1 | Ejecutar `main.py`. | Aparece primero la pantalla de acceso. |
| 2 | Pulsar Iniciar sesión con campos vacíos. | Mensaje «Ingrese usuario y contraseña». |
| 3 | Escribir `ana` y una contraseña incorrecta. | Mensaje «Credenciales incorrectas»; permanece en el login. |
| 4 | Ingresar `ana` y `1234`. | Aparece el panel principal en la misma ventana. |
| 5 | Pulsar Productos. | Aparecen los tres productos con los precios y stock de la tabla anterior. |
| 6 | Pulsar Usuarios. | Aparece `U001 - ana`, con usuario de acceso `ana`. |
| 7 | Observar la barra inferior. | Indica 3 productos y 1 usuario. |
| 8 | Pulsar Ventas (pendiente). | Aparece un mensaje que indica que se incorporarán después. |
| 9 | Pulsar Cerrar sesión. | Regresa al login con campos vacíos, dentro de la misma ventana. |
| 10 | Volver a ingresar y consultar. | Se repite el flujo sin crear otra ventana principal. |

La separación se puede revisar en el código: las vistas llaman a
`RestauranteServicio` y no importan `json` ni abren archivos. `main.py` contiene
la única creación de `Tk()` y la única llamada a `mainloop()`.

### Revisión realizada

Se verificó la aplicación con **Python 3.14.3 y Tkinter 8.6.15 en Windows**.
Se comprobaron los mensajes del login, el acceso válido, los botones de consulta,
los datos mostrados, el aviso solicitado por Ventas y el retorno al login.
También se repitió el acceso y cierre de sesión para comprobar que se conservan
la ventana principal y el servicio. Las comprobaciones internas se realizaron
fuera de la carpeta de entrega.

| Criterio de Semana 13 | Evidencia verificable |
| --- | --- |
| 1. Estructura y separación de responsabilidades | Carpetas obligatorias, modelos Producto y Usuario y servicios independientes de las vistas. |
| 2. Interfaz de acceso | Campos de usuario y contraseña, mensajes visibles y llamada a `validar_acceso()`. |
| 3. Panel y consultas mediante servicios | Botones Productos y Usuarios, datos cargados por el servicio y Ventas identificada como pendiente. |
| 4. Ejecución y flujo | Entrada en `main.py`, una ventana, un ciclo y regreso al login sin perder la aplicación. |
| 5. Documentación | Propósito, continuidad, estructura, responsabilidades, flujo y pasos de ejecución en este README. |

## Entrega en GitHub

Repositorio de esta actividad:
[POO-Semana-13-Restaurante](https://github.com/DavidRivadeneira/POO-Semana-13-Restaurante).

La consigna requiere un **nuevo repositorio público de Semana 13**. Publicar
el contenido de esta carpeta conservando `restaurante_app/` y sus subcarpetas,
con el README principal visible en la raíz. No entregar solamente un ZIP.

Antes de entregar, abrir el enlace sin iniciar sesión y comprobar que los
archivos sean visibles. En Moodle/EVA se entrega únicamente el enlace del nuevo
repositorio público. Guardar el proyecto localmente no completa ese paso.

## Referencias de trabajo

- Guía de Semana 13: fundamentos de GUI, ventana única y separación de capas.
- Diapositivas de Semana 13: componentes básicos de Tkinter y manejo de eventos.
- Consigna y rúbrica de Semana 13 publicadas en el EVA.
- [Biblioteca App de Semana 13](https://github.com/kevin10lascano-sketch/Clase-Semana-13-POO): referencia estructural y funcional revisada y ejecutada antes de la adaptación.
- Proyecto personal de Semana 12: origen de los productos, usuario y organización modular.
