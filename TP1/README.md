# 📊 Editor de CSV con Streamlit

## [Ver aplicación en vivo](https://csv-editor.streamlit.app/)

Una aplicación web completa y fácil de usar para editar archivos CSV, crear tablas desde cero y generar datos aleatorios para pruebas.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)

## 🚀 Características

### 📂 Importar y Editar CSV
- Carga archivos CSV existentes
- Editor interactivo de datos
- Agrega o elimina filas dinámicamente
- Edita celdas directamente en la interfaz
- Descarga el CSV modificado

### ➕ Crear Tablas Desde Cero
- Define el número de columnas y filas
- Personaliza los nombres de las columnas
- Editor completo con capacidad de agregar/eliminar filas
- Ideal para crear datasets nuevos

### 🎲 Generador de Datos Aleatorios
Genera datos de prueba con múltiples tipos:
- **Nombres**: Nombres y apellidos realistas
- **Emails**: Direcciones de correo aleatorias
- **Teléfonos**: Formato argentino (+54 9 11...)
- **Fechas**: Con rangos personalizables
- **Números**: Enteros o decimales con valores min/max
- **Ciudades**: Ciudades de Argentina
- **Productos**: Lista de productos
- **Booleanos**: Valores True/False
- **Texto Lorem**: Frases aleatorias

## 📦 Instalación

### Requisitos previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/csv-editor.git
cd csv-editor
```

### Paso 2: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 3: Ejecutar la aplicación
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 📋 Dependencias

Crea un archivo `requirements.txt` con:
```
streamlit>=1.28.0
pandas>=2.0.0
```

## 🎯 Uso

### Importar y Editar CSV
1. Ve a la pestaña "📂 Importar CSV"
2. Carga tu archivo CSV usando el botón de carga
3. Edita los datos directamente en la tabla
4. Haz clic en "Descargar CSV modificado" para guardar los cambios

### Crear Nueva Tabla
1. Ve a la pestaña "➕ Crear Nueva Tabla"
2. Define el número de columnas y filas
3. Asigna nombres a cada columna
4. Haz clic en "Crear Tabla"
5. Completa los datos en el editor
6. Descarga tu CSV

### Generar Datos Aleatorios
1. Ve a la pestaña "🎲 Generar Datos Aleatorios"
2. Configura el número de filas a generar
3. Define el número de columnas
4. Para cada columna:
   - Asigna un nombre
   - Selecciona el tipo de dato
   - Configura opciones específicas (si aplica)
5. Haz clic en "Generar Datos"
6. Edita si es necesario
7. Descarga el CSV generado

## 🛠️ Tecnologías Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework para crear aplicaciones web
- **[Pandas](https://pandas.pydata.org/)**: Manipulación y análisis de datos
- **Python**: Lenguaje de programación principal


## 📝 Ideas para Futuras Mejoras

- [ ] Limpieza de datos (eliminar duplicados, valores nulos)
- [ ] Filtrado avanzado de datos
- [ ] Estadísticas y visualizaciones
- [ ] Exportar a Excel
- [ ] Combinar múltiples CSV
- [ ] Búsqueda y reemplazo masivo
- [ ] Validación de datos
- [ ] Soporte para más formatos (Excel, JSON)

## 👤 Autor

- GitHub: [@Bayaslian_Santiago](https://github.com/BayaslianSantiago/)
- Email: bayasliansantiago@gmail.com
---

Agradecimientos al Instituto Tecnologico Beltran y a sus docentes.
