# Individual Project - MaIA (Machine Learning & Artificial Intelligence)

## Taller 1: Dash Framework



### Descripción

Este proyecto consiste en el desarrollo de una aplicación interactiva utilizando Dash, un framework para crear aplicaciones web analíticas basadas en Python. El objetivo de este primer taller es familiarizarse con la estructura de una aplicación Dash, los componentes interactivos y la creación de gráficos, visualizando la demanda energética en Austria.

### Estructura del Repositorio

La estructura real del proyecto es la siguiente:

```text
individual-project-MaIA/
├── README.md               # Documentación del proyecto
├── main.py                 # Archivo inicial/Hello-World de UV
├── pyproject.toml          # Dependencias y configuración del proyecto gestionado con uv
├── .gitignore              # Archivos a ignorar por git
├── *.pem                   # Llaves de acceso a instancias EC2 (ignoradas por git)
└── taller1/                # Directorio del Taller 1
    ├── app.py              # Código principal de la aplicación Dash
    ├── datos_energia.csv   # Dataset de energía utilizado por el dashboard
    └── assets/             # Recursos estáticos de la aplicación (CSS, imágenes)
```

### Requisitos Previos

- Python 3.12+ (según lo definido en `pyproject.toml`)
- [uv](https://github.com/astral-sh/uv) (Gestor de paquetes y entornos virtuales de Python ultrarrápido)

### Instalación

Este proyecto utiliza `uv` y `pyproject.toml` para la gestión de dependencias, lo que simplifica enormemente la instalación.

1. **Clona el repositorio** (o descarga los archivos):
   ```bash
   git clone <url-del-repositorio>
   cd individual-project-MaIA
   ```

2. **Instala las dependencias y crea el entorno virtual** automáticamente con `uv`:
   ```bash
   uv sync
   ```
   *Esto leerá el archivo `pyproject.toml` e instalará `dash`, `pandas`, `plotly` y `numpy` en un entorno virtual administrado por uv (`.venv`).*

### Ejecución

Para iniciar la aplicación Dash usando el entorno configurado, ejecuta desde la raíz del proyecto:

```bash
uv run python taller1/app.py
```

La aplicación se ejecutará en modo de desarrollo (`debug=True`) y estará configurada para escuchar en todas las interfaces de red (`host="0.0.0.0"`). 

Para acceder a la aplicación desde tu navegador:
- **En entorno local:** Entra a [http://127.0.0.1:8050](http://127.0.0.1:8050) o [http://localhost:8050](http://localhost:8050)
- **En una instancia EC2:** Entra a `http://<IP_PUBLICA_DE_TU_EC2>:8050` (Asegúrate de que el puerto 8050 esté abierto en el Security Group de AWS).

### Contribución

Todos los ejercicios y desarrollos específicos de este taller deben realizarse dentro de la carpeta `taller1`. Se espera documentar el código y seguir las buenas prácticas de programación. Cada ejercicio puede requerir:
- Modificación del archivo `app.py`
- Adición de recursos visuales en `taller1/assets/`