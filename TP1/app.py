import streamlit as st
import pandas as pd
from io import StringIO
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Editor de CSV", page_icon="📊", layout="wide")

# ==============================
# FUNCIONES DE GENERACIÓN
# ==============================
def generar_nombres(n):
    nombres = ["Juan", "María", "Carlos", "Ana", "Pedro", "Laura", "Diego", "Sofía", 
               "Miguel", "Lucía", "Fernando", "Valentina", "Roberto", "Camila", "Jorge",
               "Isabella", "Luis", "Martina", "Antonio", "Victoria"]
    apellidos = ["García", "Rodríguez", "Martínez", "López", "González", "Pérez", 
                 "Sánchez", "Ramírez", "Torres", "Flores", "Rivera", "Gómez", "Díaz",
                 "Cruz", "Morales", "Reyes", "Jiménez", "Hernández", "Ruiz", "Vargas"]
    return [f"{random.choice(nombres)} {random.choice(apellidos)}" for _ in range(n)]

def generar_emails(n):
    dominios = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "empresa.com"]
    nombres = ["user", "contact", "info", "admin", "support", "juan", "maria", "carlos"]
    return [f"{random.choice(nombres)}{random.randint(1, 999)}@{random.choice(dominios)}" for _ in range(n)]

def generar_telefonos(n):
    return [f"+54 9 11 {random.randint(1000, 9999)}-{random.randint(1000, 9999)}" for _ in range(n)]

def generar_fechas(n, inicio="2020-01-01", fin="2024-12-31"):
    start = datetime.strptime(inicio, "%Y-%m-%d")
    end = datetime.strptime(fin, "%Y-%m-%d")
    delta = end - start
    return [(start + timedelta(days=random.randint(0, delta.days))).strftime("%Y-%m-%d") for _ in range(n)]

def generar_numeros(n, minimo=1, maximo=100, decimales=False):
    if decimales:
        return [round(random.uniform(minimo, maximo), 2) for _ in range(n)]
    return [random.randint(minimo, maximo) for _ in range(n)]

def generar_ciudades(n):
    ciudades = ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "La Plata", "San Miguel de Tucumán",
                "Mar del Plata", "Salta", "Santa Fe", "San Juan", "Resistencia", "Neuquén",
                "Posadas", "Bahía Blanca", "Paraná", "San Salvador de Jujuy"]
    return [random.choice(ciudades) for _ in range(n)]

def generar_productos(n):
    productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Auriculares", "Webcam", "Micrófono",
                 "Tablet", "Smartphone", "Impresora", "Scanner", "Router", "Disco Duro", "USB",
                 "Cable HDMI", "Adaptador", "Cargador", "Batería", "Mousepad", "Soporte"]
    return [random.choice(productos) for _ in range(n)]

def generar_booleanos(n):
    return [random.choice([True, False]) for _ in range(n)]

def generar_lorem(n):
    palabras = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
                "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
                "magna", "aliqua"]
    return [" ".join(random.choices(palabras, k=random.randint(3, 8))).capitalize() + "." for _ in range(n)]


# ==============================
# INTERFAZ PRINCIPAL
# ==============================
st.title("📊 Editor de Archivos CSV")
st.markdown("Sube tu archivo CSV, créalo desde cero o genera datos aleatorios, edítalos y descárgalos en CSV o JSON.")

tab1, tab2, tab3 = st.tabs(["📂 Importar CSV", "➕ Crear Nueva Tabla", "🎲 Generar Datos Aleatorios"])


# -------------------------------
# TAB 1 - IMPORTAR CSV
# -------------------------------
with tab1:
    uploaded_file = st.file_uploader("Selecciona un archivo CSV", type=['csv'])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            
            st.success(f"✅ Archivo cargado: {uploaded_file.name}")
            st.info(f"Filas: {len(df)} | Columnas: {len(df.columns)}")

            st.subheader("Edita los datos:")
            edited_df = st.data_editor(df, use_container_width=True, num_rows="dynamic", key="data_editor_import")

            st.subheader("Descargar archivo modificado:")

            # DESCARGA CSV Y JSON
            col_csv, col_json = st.columns(2)

            with col_csv:
                csv_buffer = StringIO()
                edited_df.to_csv(csv_buffer, index=False)
                st.download_button(
                    label="⬇️ Descargar CSV modificado",
                    data=csv_buffer.getvalue(),
                    file_name=f"editado_{uploaded_file.name}",
                    mime="text/csv",
                    type="primary",
                    key="download_csv_tab1"
                )

            with col_json:
                json_data = edited_df.to_json(orient="records", indent=4, force_ascii=False)
                st.download_button(
                    label="⬇️ Descargar JSON modificado",
                    data=json_data,
                    file_name=f"editado_{uploaded_file.name.replace('.csv', '.json')}",
                    mime="application/json",
                    type="secondary",
                    key="download_json_tab1"
                )

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Filas totales", len(edited_df))
            with col2:
                st.metric("Columnas totales", len(edited_df.columns))

        except Exception as e:
            st.error(f"❌ Error al procesar el archivo: {str(e)}")
    else:
        st.info("👆 Sube un archivo CSV para comenzar")


# -------------------------------
# TAB 2 - CREAR NUEVA TABLA
# -------------------------------
with tab2:
    st.subheader("Crear Nueva Tabla")
    col1, col2 = st.columns(2)
    with col1:
        num_cols = st.number_input("Número de columnas", min_value=1, max_value=20, value=3)
    with col2:
        num_rows = st.number_input("Número de filas iniciales", min_value=1, max_value=100, value=5)

    st.write("**Nombres de columnas:**")
    col_names = []
    cols = st.columns(min(num_cols, 4))
    for i in range(num_cols):
        with cols[i % 4]:
            col_name = st.text_input(f"Columna {i+1}", value=f"Columna_{i+1}", key=f"col_{i}")
            col_names.append(col_name)

    if st.button("🆕 Crear Tabla", type="primary"):
        new_df = pd.DataFrame({col: [""] * num_rows for col in col_names})
        st.session_state['created_df'] = new_df
        st.success("✅ Tabla creada exitosamente!")
        st.rerun()

    if 'created_df' in st.session_state:
        st.subheader("Edita tu tabla:")
        edited_new_df = st.data_editor(
            st.session_state['created_df'],
            use_container_width=True,
            num_rows="dynamic",
            key="data_editor_new"
        )
        st.session_state['created_df'] = edited_new_df

        st.subheader("Descargar tabla creada:")
        col_csv, col_json = st.columns(2)

        with col_csv:
            csv_buffer_new = StringIO()
            edited_new_df.to_csv(csv_buffer_new, index=False)
            st.download_button(
                label="⬇️ Descargar CSV",
                data=csv_buffer_new.getvalue(),
                file_name="tabla_nueva.csv",
                mime="text/csv",
                type="primary",
                key="download_csv_tab2"
            )

        with col_json:
            json_data_new = edited_new_df.to_json(orient="records", indent=4, force_ascii=False)
            st.download_button(
                label="⬇️ Descargar JSON",
                data=json_data_new,
                file_name="tabla_nueva.json",
                mime="application/json",
                type="secondary",
                key="download_json_tab2"
            )

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Filas totales", len(edited_new_df))
        with col2:
            st.metric("Columnas totales", len(edited_new_df.columns))

        if st.button("🗑️ Borrar y empezar de nuevo"):
            del st.session_state['created_df']
            st.rerun()


# -------------------------------
# TAB 3 - GENERAR DATOS ALEATORIOS
# -------------------------------
with tab3:
    st.subheader("🎲 Generador de Datos Aleatorios")
    col1, col2 = st.columns(2)
    with col1:
        num_filas = st.number_input("Número de filas a generar", min_value=1, max_value=10000, value=100)
    with col2:
        num_columnas_random = st.number_input("Número de columnas", min_value=1, max_value=10, value=3)

    st.markdown("---")
    st.write("**Configura cada columna:**")

    columnas_config = []

    for i in range(num_columnas_random):
        with st.expander(f"📋 Columna {i+1}", expanded=(i==0)):
            col_a, col_b = st.columns(2)
            with col_a:
                nombre_col = st.text_input(f"Nombre", value=f"Columna_{i+1}", key=f"random_col_name_{i}")
            with col_b:
                tipo_dato = st.selectbox(
                    f"Tipo de dato",
                    ["Nombres", "Emails", "Teléfonos", "Fechas", "Números Enteros", 
                     "Números Decimales", "Ciudades", "Productos", "Booleanos", "Texto Lorem"],
                    key=f"random_col_type_{i}"
                )

            opciones = {}
            if tipo_dato in ["Números Enteros", "Números Decimales"]:
                col_min, col_max = st.columns(2)
                with col_min:
                    opciones['min'] = st.number_input("Mínimo", value=1, key=f"random_min_{i}")
                with col_max:
                    opciones['max'] = st.number_input("Máximo", value=100, key=f"random_max_{i}")
            elif tipo_dato == "Fechas":
                col_inicio, col_fin = st.columns(2)
                with col_inicio:
                    opciones['inicio'] = st.date_input("Fecha inicio", value=datetime(2020,1,1), key=f"random_inicio_{i}").strftime("%Y-%m-%d")
                with col_fin:
                    opciones['fin'] = st.date_input("Fecha fin", value=datetime(2024,12,31), key=f"random_fin_{i}").strftime("%Y-%m-%d")

            columnas_config.append({'nombre': nombre_col, 'tipo': tipo_dato, 'opciones': opciones})

    st.markdown("---")

    if st.button("🎲 Generar Datos", type="primary", use_container_width=True):
        data_random = {}
        for config in columnas_config:
            nombre = config['nombre']
            tipo = config['tipo']
            opciones = config['opciones']
            if tipo == "Nombres": data_random[nombre] = generar_nombres(num_filas)
            elif tipo == "Emails": data_random[nombre] = generar_emails(num_filas)
            elif tipo == "Teléfonos": data_random[nombre] = generar_telefonos(num_filas)
            elif tipo == "Fechas": data_random[nombre] = generar_fechas(num_filas, opciones.get('inicio'), opciones.get('fin'))
            elif tipo == "Números Enteros": data_random[nombre] = generar_numeros(num_filas, opciones.get('min'), opciones.get('max'))
            elif tipo == "Números Decimales": data_random[nombre] = generar_numeros(num_filas, opciones.get('min'), opciones.get('max'), True)
            elif tipo == "Ciudades": data_random[nombre] = generar_ciudades(num_filas)
            elif tipo == "Productos": data_random[nombre] = generar_productos(num_filas)
            elif tipo == "Booleanos": data_random[nombre] = generar_booleanos(num_filas)
            elif tipo == "Texto Lorem": data_random[nombre] = generar_lorem(num_filas)

        st.session_state['random_df'] = pd.DataFrame(data_random)
        st.success(f"✅ Generados {num_filas} registros con {len(columnas_config)} columnas!")
        st.rerun()

    if 'random_df' in st.session_state:
        st.markdown("---")
        st.subheader("Vista previa y descarga:")

        edited_random_df = st.data_editor(
            st.session_state['random_df'],
            use_container_width=True,
            num_rows="dynamic",
            key="data_editor_random"
        )
        st.session_state['random_df'] = edited_random_df

        col_csv, col_json = st.columns(2)

        with col_csv:
            csv_random = StringIO()
            edited_random_df.to_csv(csv_random, index=False)
            st.download_button(
                label="⬇️ Descargar CSV generado",
                data=csv_random.getvalue(),
                file_name="datos_aleatorios.csv",
                mime="text/csv",
                type="primary",
                use_container_width=True,
                key="download_csv_tab3"
            )

        with col_json:
            json_random = edited_random_df.to_json(orient="records", indent=4, force_ascii=False)
            st.download_button(
                label="⬇️ Descargar JSON generado",
                data=json_random,
                file_name="datos_aleatorios.json",
                mime="application/json",
                type="secondary",
                use_container_width=True,
                key="download_json_tab3"
            )

        if st.button("🗑️ Limpiar datos", use_container_width=True):
            del st.session_state['random_df']
            st.rerun()
