# Individual Project - MaIA (Machine Learning & Artificial Intelligence)

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Dash](https://img.shields.io/badge/Dash-Plotly-008DE4?logo=plotly&logoColor=white)](https://dash.plotly.com/)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?logo=mlflow&logoColor=white)](https://mlflow.org/)
[![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Package Manager](https://img.shields.io/badge/uv-Package%20Manager-DE5FE9?logo=astral&logoColor=white)](https://github.com/astral-sh/uv)
[![Testing](https://img.shields.io/badge/Tox-Pytest%20%7C%20Mypy-green?logo=pytest&logoColor=white)](https://tox.wiki/)

Repositorio de proyectos y talleres prácticos de la **Maestría en Inteligencia Artificial (MaIA)** - Universidad de los Andes. Este repositorio cubre el ciclo de vida completo de aplicaciones de Machine Learning en producción (MLOps): desde la exploración y visualización de datos, versionamiento y seguimiento de experimentos, hasta el empaquetamiento modular, desarrollo de APIs de inferencia y despliegue de microservicios containerizados con Docker.

---

## 📑 Tabla de Contenidos

1. [Estructura del Repositorio](#-estructura-del-repositorio)
2. [Descripción de Talleres](#-descripción-de-talleres)
   - [Taller 1: Dashboard de Demanda Energética con Dash](#taller-1-dashboard-de-demanda-energética-con-dash)
   - [Taller 2: Flujo de Trabajo Colaborativo en Git & GitHub](#taller-2-flujo-de-trabajo-colaborativo-en-git--github)
   - [Taller 3: Versionamiento de Datos con DVC](#taller-3-versionamiento-de-datos-con-dvc)
   - [Taller 4: Experiment Tracking con MLflow](#taller-4-experiment-tracking-con-mlflow)
   - [Taller 5: Empaquetamiento de Modelos de Machine Learning](#taller-5-empaquetamiento-de-modelos-de-machine-learning)
   - [Taller 6: API REST de Inferencia con FastAPI & Tox](#taller-6-api-rest-de-inferencia-con-fastapi--tox)
   - [Taller 7: Containerización con Docker](#taller-7-containerización-con-docker)
   - [Taller 8: Arquitectura Multi-Contenedor (Dash + FastAPI)](#taller-8-arquitectura-multi-contenedor-dash--fastapi)
   - [Taller 9: Despliegue de API de Inferencia en Contenedores](#taller-9-despliegue-de-api-de-inferencia-en-contenedores)
3. [Requisitos Previos](#-requisitos-previos)
4. [Instalación y Configuración](#-instalación-y-configuración)
5. [Guía de Ejecución](#-guía-de-ejecución)
6. [Pruebas y Calidad de Código](#-pruebas-y-calidad-de-código)

---

## 📂 Estructura del Repositorio

```text
individual-project-MaIA/
├── README.md                     # Documentación general del repositorio
├── pyproject.toml                # Configuración de dependencias raíz con uv
├── main.py                       # Script punto de entrada general
├── edit_companero.txt            # Evidencia de colaboración remota en Git (Taller 2)
│
├── taller1/                      # Taller 1: Visualización Interactiva con Dash
│   ├── app.py                    # Aplicación Dash interactiva de series de tiempo
│   ├── datos_energia.csv         # Dataset de demanda energética en Austria
│   └── assets/                   # Estilos CSS y recursos estáticos
│
├── taller3/                      # Taller 3: Data Version Control (DVC)
│   └── *.pem                     # Llaves y credenciales de entorno AWS EC2
│
├── taller4/                      # Taller 4: Seguimiento de Experimentos con MLflow
│   ├── mlflow-diab.py / .ipynb   # Experimento con Scikit-Learn (Random Forest)
│   └── mlflow-mnist.py / .ipynb  # Experimento de Deep Learning (TensorFlow / Keras)
│
├── Taller5/                      # Taller 5: Empaquetamiento de Modelo de ML (Bank Churn)
│   ├── dev/                      # Notebooks y scripts de exploración y desarrollo
│   ├── package-src/              # Código fuente modular del paquete 'modelo_abandono'
│   │   ├── model/                # Pipeline, transformers, predict y train scripts
│   │   ├── pyproject.toml        # Configuración de empaquetamiento (setuptools / wheel)
│   │   └── tox.ini               # Automatización de pruebas y compilación del paquete
│   ├── test/                     # Validación de inferencia con el paquete empaquetado
│   └── bankchurn_test.csv        # Dataset de prueba para predicciones
│
├── taller6/                      # Taller 6: API REST con FastAPI y Testing
│   ├── app/                      # Código de la aplicación FastAPI (endpoints, schemas, config)
│   │   ├── api.py                # Definición de rutas (/health, /predict)
│   │   ├── main.py               # Instancia de FastAPI, middlewares y CORS
│   │   ├── config.py             # Configuración centralizada con Pydantic Settings
│   │   ├── schemas/              # Esquemas de validación de datos con Pydantic
│   │   └── tests/                # Pruebas unitarias y de integración con pytest
│   ├── model-pkg/                # Distribuciones Wheel del modelo de ML (v0.0.1 y v0.0.2)
│   ├── tox.ini                   # Automatización de entornos de prueba, linting y tipado
│   └── requirements.txt          # Dependencias de ejecución y producción
│
├── taller7/                      # Taller 7: Containerización de API con Docker
│   └── docker-api-starter/       # Configuración y Dockerfile de la API bankchurn
│       ├── Dockerfile            # Imagen optimizada en Python 3.12-slim con usuario seguro
│       └── bankchurn-api/        # Código fuente del microservicio backend
│
├── taller8/                      # Taller 8: Arquitectura Multi-Contenedor (Frontend + Backend)
│   ├── bankchurn-api/            # Microservicio de inferencia (FastAPI + Docker)
│   └── docker-dash-starter/      # Frontend interactivo en Dash containerizado
│       ├── Dockerfile            # Dockerfile para la interfaz web Dash
│       └── app/                  # UI para captura de variables y visualización de predicciones
│
└── taller9/                      # Taller 9: Despliegue de API de Inferencia Containerizada
    ├── Dockerfile                # Dockerfile de producción con dependencias de compilación C/C++
    └── bankchurn-api/            # Servicio de predicción con modelo empaquetado v0.0.2
```

---

## 🛠️ Descripción de Talleres

### Taller 1: Dashboard de Demanda Energética con Dash
- **Objetivo**: Construir una aplicación web analítica e interactiva con **Dash** y **Plotly** para el análisis y proyección de series temporales de demanda energética en Austria.
- **Aspectos Clave**:
  - Manipulación y agregación temporal con `pandas`.
  - Gráficos interactivos con intervalos de confianza y proyecciones dinámicas.
  - Diseño responsivo con estilos personalizados en `taller1/assets/`.

### Taller 2: Flujo de Trabajo Colaborativo en Git & GitHub
- **Objetivo**: Implementar prácticas profesionales de trabajo en equipo utilizando control de versiones.
- **Aspectos Clave**:
  - Flujo de ramas de trabajo (`feature branching`), Pull Requests y revisión cruzada de código.
  - Resolución de conflictos y sincronización remota (`edit_companero.txt`).

### Taller 3: Versionamiento de Datos con DVC
- **Objetivo**: Gestionar el ciclo de vida y versionamiento de datasets desacoplados del código fuente.
- **Aspectos Clave**:
  - Configuración de almacenamiento remoto en la nube (AWS EC2 / S3).
  - Rastreabilidad de versiones de datos junto con el historial de Git.

### Taller 4: Experiment Tracking con MLflow
- **Objetivo**: Registrar, comparar y reproducir experimentos de Machine Learning y Deep Learning.
- **Aspectos Clave**:
  - **Scikit-Learn (`mlflow-diab.py`)**: Regresión con Random Forest sobre el dataset Diabetes, registrando hiperparámetros (`num_trees`, `max_depth`, `max_feat`), métricas (`MSE`) y artefactos del modelo.
  - **TensorFlow / Keras (`mlflow-mnist.py`)**: Red neuronal densa para clasificación de dígitos MNIST, integrando `mlflow.keras.autolog()` y paso dinámico de hiperparámetros vía CLI con `argparse`.

### Taller 5: Empaquetamiento de Modelos de Machine Learning
- **Objetivo**: Transformar un pipeline de Machine Learning en un paquete de Python distribuible e instalable (`.whl`).
- **Aspectos Clave**:
  - Caso de uso: Predicción de abandono bancario (**Bank Churn Prediction**).
  - Creación de transformadores y pipelines reproducibles con Scikit-Learn.
  - Empaquetamiento formal con `setup.py`, `pyproject.toml` y `MANIFEST.in`.
  - Versionamiento semántico del modelo (`v0.0.1` -> `v0.0.2`) ajustando variables predictoras (`Months_Inactive_12_mon`).
  - Pruebas automatizadas de inferencia y serialización con `joblib`.

### Taller 6: API REST de Inferencia con FastAPI & Tox
- **Objetivo**: Desarrollar un microservicio de inferencia de alto rendimiento con validación robusta y testing automatizado.
- **Aspectos Clave**:
  - Integración del paquete `modelo_abandono` mediante wheels (`model-pkg/`).
  - Validación de esquemas y tipos en request/response usando **Pydantic**.
  - Endpoints implementados:
    - `GET /api/v1/health`: Verificación de estado de la API y versiones del modelo.
    - `POST /api/v1/predict`: Inferencia síncrona sobre registros de clientes bancarios.
  - Documentación interactiva automática en `/docs` (Swagger UI) y `/redoc`.
  - Configuración de **Tox** para ejecutar `pytest`, validación de tipos estáticos con `mypy` y linters (`flake8`, `black`, `isort`).

### Taller 7: Containerización con Docker
- **Objetivo**: Empaquetar el servicio de inferencia en una imagen Docker ligera, portable y segura.
- **Aspectos Clave**:
  - Imagen base `python:3.12-slim`.
  - Principio de mínimo privilegio: Ejecución bajo usuario sin privilegios `api-user`.
  - Instalación de dependencias y herramientas de compilación C/C++ (`build-essential`).
  - Exposición segura de puertos para comunicación de red (puerto `8001`).

### Taller 8: Arquitectura Multi-Contenedor (Dash + FastAPI)
- **Objetivo**: Conectar una interfaz de usuario interactiva con una API de inferencia en microservicios desacoplados.
- **Aspectos Clave**:
  - **Frontend**: Aplicación Dash (`docker-dash-starter`) que presenta un formulario interactivo para capturar variables de clientes.
  - **Backend**: API FastAPI (`bankchurn-api`) encargada del preprocesamiento y predicción.
  - Comunicación entre contenedores mediante variables de entorno configurables (`API_URL`, `API_PORT`).

### Taller 9: Despliegue de API de Inferencia en Contenedores
- **Objetivo**: Despliegue optimizado y modular del servicio de inferencia bancaria en contenedores Docker listos para la nube.
- **Aspectos Clave**:
  - Dockerfile estructurado con separación de capas y scripts de inicio (`run.sh`).
  - Integración del modelo actualizado `v0.0.2` para inferencia en tiempo real.

---

## 💻 Requisitos Previos

- **Python 3.12+**
- **[uv](https://github.com/astral-sh/uv)** (Gestor moderno y ultrarrápido de paquetes de Python)
- **[Docker](https://www.docker.com/)** (Para la ejecución de contenedores en los Talleres 7, 8 y 9)
- **Git**

---

## 🚀 Instalación y Configuración

1. **Clonar el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd individual-project-MaIA
   ```

2. **Crear el entorno virtual e instalar dependencias con `uv`**:
   ```bash
   uv sync
   ```
   *Esto generará automáticamente el entorno virtual `.venv` con las dependencias base (`dash`, `plotly`, `pandas`, `numpy`).*

---

## ⚡ Guía de Ejecución

### 1. Ejecutar Taller 1 (Dashboard Dash)
```bash
uv run python taller1/app.py
```
- Acceder en el navegador: [http://localhost:8050](http://localhost:8050)

---

### 2. Ejecutar Taller 4 (Experimentos con MLflow)
Asegúrate de tener un servidor de MLflow activo o ejecutar localmente:
```bash
# Experimento Scikit-Learn Diabetes
python taller4/mlflow-diab.py

# Experimento MNIST Deep Learning
python taller4/mlflow-mnist.py --batch_size 128 --epochs 5 --learning_rate 0.05
```
- Iniciar la UI de MLflow:
  ```bash
  mlflow ui
  ```
- Acceder a la interfaz de experimentos: [http://localhost:5000](http://localhost:5000)

---

### 3. Ejecutar Taller 5 (Empaquetamiento y Prueba de Modelo)
```bash
# Construir paquete wheel
cd Taller5/package-src
python setup.py bdist_wheel sdist

# Ejecutar script de prueba de predicción
cd ../
python test-package.py
```

---

### 4. Ejecutar Taller 6 (API FastAPI)
```bash
# Instalar dependencias del taller 6
cd taller6
pip install -r requirements.txt

# Ejecutar el servidor Uvicorn
python app/main.py
```
- Acceder a la documentación Swagger: [http://localhost:8001/docs](http://localhost:8001/docs)
- Endpoint de salud: [http://localhost:8001/api/v1/health](http://localhost:8001/api/v1/health)

---

### 5. Ejecutar con Docker (Talleres 7, 8 y 9)

#### Taller 7 / 9 (API de Inferencia con Docker)
```bash
cd taller9
docker build -t bankchurn-api:v0.0.2 -f Dockerfile .
docker run -d -p 8001:8001 --name bankchurn_service bankchurn-api:v0.0.2
```
- Probar endpoint en: [http://localhost:8001/docs](http://localhost:8001/docs)

#### Taller 8 (Frontend Dash + Backend FastAPI)
```bash
# 1. Iniciar backend API
cd taller8/bankchurn-api
docker build -t bankchurn-api:v1 -f Dockerfile .
docker run -d -p 8001:8001 --name api_backend bankchurn-api:v1

# 2. Iniciar frontend Dash conectado a la API
cd ../docker-dash-starter
docker build -t bankchurn-dash:v1 -f Dockerfile .
docker run -d -p 8050:8050 -e API_URL=host.docker.internal -e API_PORT=8001 --name dash_frontend bankchurn-dash:v1
```
- Abrir la interfaz web en: [http://localhost:8050](http://localhost:8050)

---

## 🧪 Pruebas y Calidad de Código

El proyecto utiliza **Tox** para asegurar la calidad de código, tipado y pruebas unitarias:

```bash
# Ejecutar todas las pruebas y verificaciones en taller 6
cd taller6
tox

# Ejecutar únicamente las pruebas unitarias con pytest
tox -e test_app

# Ejecutar análisis estático (flake8, isort, black, mypy)
tox -e checks
```

---

## 👥 Autores y Créditos

- **Estudiante**: Mateo Hernández Gualdrón
- **Programa**: Maestría en Inteligencia Artificial (MaIA)
- **Institución**: Universidad de los Andes
- **Curso**: Despliegue de Modelos de Machine Learning / MLOps