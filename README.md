
# Procesamiento de Datos para Base de Datos de Ventas

## Descripción
Este repositorio contiene los scripts necesarios para procesar datos de ventas, crear una base de datos MySQL y cargar los datos procesados en tablas relacionales. Las principales funcionalidades incluyen:
- **Transformación de datos:** Procesamiento de datos brutos desde un archivo CSV.
- **Creación de la base de datos y las tablas:** Diseño de una estructura relacional con claves foráneas para mantener la integridad de los datos.
- **Inserción de datos en la base de datos:** Automatización de la carga de datos procesados.

## Requisitos
- Python 3.8 o superior.
- MySQL Server instalado y en ejecución.
- Las dependencias de Python están listadas en `requirements.txt`.

## Instalación
### Paso 1: Instalar las dependencias
Ejecuta el siguiente comando para instalar las dependencias necesarias:
```bash
pip install -r requirements.txt
```

### Paso 2: Configurar las credenciales de la base de datos
Crea un archivo `.env` en el directorio raíz del proyecto con las siguientes variables:

```plaintext
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=sales
DB_PORT=3306
```

> **Nota:** Asegúrate de incluir `.env` en tu archivo `.gitignore` para evitar que las credenciales sean subidas al repositorio.

## Uso
### Paso 1: Procesar los datos de entrada
Ejecuta el script `processes.py` para transformar los datos brutos en un archivo CSV listo para insertar en la base de datos:
```bash
python etl/processes.py
```

Esto generará un archivo `sales.csv` en el directorio `data/`.

### Paso 2: Crear la base de datos y las tablas
Ejecuta el script `create_tables.py` para crear la base de datos `sales` y las tablas necesarias:
```bash
python etl/create_tables.py
```

### Paso 3: Insertar los datos en la base de datos
Ejecuta el script `insert_data.py` para insertar los datos procesados en las tablas de la base de datos:
```bash
python etl/insert_data.py
```

Esto cargará los datos de `sales.csv` en las tablas relacionales, asegurando la integridad referencial.

## Estructura del Repositorio
```
data-processing/
│
├── data/                          # Datos de entrada y salida
│   ├── shopping_trends.csv        # Archivo CSV de datos brutos
│   ├── sales.csv                  # Archivo CSV procesado
│
├── etl/                           # Scripts ETL
│   ├── processes.py               # Script para procesar datos de entrada
│   ├── create_tables.py           # Script para crear la base de datos y las tablas
│   ├── insert_data.py             # Script para insertar datos en la base de datos
│
├── requirements.txt               # Dependencias de Python
├── .gitignore                     # Archivos ignorados por Git
└── README.md                      # Documentación del repositorio
```

## Notas Importantes
- Los scripts están diseñados para ser ejecutados en orden: primero `processes.py`, luego `create_tables.py` y finalmente `insert_data.py`.
- El archivo `sales.csv` será generado automáticamente por el script `processes.py`.
