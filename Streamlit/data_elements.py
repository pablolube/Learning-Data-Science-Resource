import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng
import datetime



# ----------------------------------
# st.dataframe
# ----------------------------------
def mostrar_dataframe():

    # ----------------------------------------
    # DataFrame base
    # ----------------------------------------
    df = pd.DataFrame({
        "Nombre": ["Ana", "Juan", "Luis"],
        "Edad": [25, 30, 22],
        "Ciudad": ["Buenos Aires", "Córdoba", "Rosario"]
    })

    # ========================================
    # data
    # ========================================
    st.code('st.dataframe(data=df)')
    st.subheader("Parámetro: data")

    with st.echo():
        st.dataframe(data=df)

    # ========================================
    # width
    # ========================================
    st.code('st.dataframe(df, width="stretch")')
    st.subheader("Parámetro: width")

    with st.echo():
        st.dataframe(df, width="stretch")

    # ========================================
    # height
    # ========================================
    
    st.subheader("Parámetro: height")

    with st.echo():
        st.dataframe(df, height=150)

    # ========================================
    # use_container_width
    # ========================================
     
    st.subheader("Parámetro: use_container_width")

    with st.echo():
        st.dataframe(df, use_container_width=True)
    with st.echo():
        st.dataframe(df, use_container_width=False)

    # ========================================
    # hide_index
    # ========================================
    st.subheader("Parámetro: hide index")  
    with st.echo():
        st.dataframe(df, hide_index=True)

    # ========================================
    # column_order
    # ========================================
    st.subheader("Parámetro: column_order")

    with st.echo():
        st.dataframe(
            df,
            column_order=["Ciudad", "Nombre", "Edad"]
        )

    # ========================================
    # column_config
    # ========================================
    st.code('st.dataframe(df, column_config={...})')
    st.subheader("Parámetro: column_config")

    with st.echo():
        st.dataframe(
            df,
            column_config={
                "Nombre": st.column_config.TextColumn("👤 Nombre"),
                "Edad": st.column_config.NumberColumn("🎂 Edad"),
                "Ciudad": st.column_config.TextColumn("🏙️ Ciudad")
            }
        )


    st.title("📘 Apunte completo: st.column_config")

    # -------------------------------------------------
    # DataFrame de ejemplo
    # -------------------------------------------------
    df = pd.DataFrame({
        "Texto": ["Ana", "Juan", "Luis"],
        "Numero": [25, 30, 22],
        "Activo": [True, False, True],
        "Categoria": ["A", "B", "A"],
        "Etiquetas": [["x", "y"], ["y"], ["x", "z"]],
        "Fecha": [
            datetime.date(2024, 1, 1),
            datetime.date(2024, 2, 15),
            datetime.date(2024, 3, 20)
        ],
        "Hora": [
            datetime.time(10, 30),
            datetime.time(14, 0),
            datetime.time(18, 45)
        ],
        "Link": [
            "https://streamlit.io",
            "https://python.org",
            "https://pandas.pydata.org"
        ],
        "Imagen": [
            "https://placehold.co/50x50",
            "https://placehold.co/50x50",
            "https://placehold.co/50x50"
        ],
        "Linea": [[10, 20, 30], [5, 15, 25], [20, 10, 5]],
        "Area": [[5, 10, 15], [10, 5, 0], [3, 8, 12]],
        "Barras": [[1, 3, 2], [4, 2, 1], [2, 2, 2]],
        "Progreso": [40, 70, 90]
    })
    
    # -------------------------------------------------
    # DataFrame con TODAS las configuraciones de columna
    # -------------------------------------------------
    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True,

        #SE LO ENVIAS COMO UN DICCIONARIO
        column_config={

            # Texto
            "Texto": st.column_config.TextColumn(
                label="📝 Texto",
                help="Columna de texto",
                max_chars=20
            ),

            # Número
            "Numero": st.column_config.NumberColumn(
                label="🔢 Número",
                min_value=0,
                max_value=26,
                format="%d"
            ),

            # Checkbox
            "Activo": st.column_config.CheckboxColumn(
                label="✅ Activo"
            ),

            # Selectbox
            "Categoria": st.column_config.SelectboxColumn(
                label="📂 Categoría",
                options=["A", "B", "C"]
            ),

            # Multiselect
            "Etiquetas": st.column_config.MultiselectColumn(
                label="🏷️ Etiquetas",
                options=["x", "y", "z"]
            ),

            # Fecha
            "Fecha": st.column_config.DateColumn(
                label="📅 Fecha",
                format="DD/MM/YYYY"
            ),

            # Hora
            "Hora": st.column_config.TimeColumn(
                label="⏰ Hora",
                format="HH:mm"
            ),

            # Link
            "Link": st.column_config.LinkColumn(
                label="🔗 Enlace",
                validate="^https://"
            ),

            # Imagen
            "Imagen": st.column_config.ImageColumn(
                label="🖼️ Imagen"
            ),

            # Gráfico de línea
            "Linea": st.column_config.LineChartColumn(
                label="📈 Línea",
                y_min=0,
                y_max=40
            ),

            # Gráfico de área
            "Area": st.column_config.AreaChartColumn(
                label="📊 Área",
                y_min=0,
                y_max=20
            ),

            # Gráfico de barras
            "Barras": st.column_config.BarChartColumn(
                label="📉 Barras",
                y_min=0,
                y_max=5
            ),

            # Progreso
            "Progreso": st.column_config.ProgressColumn(
                label="⏳ Progreso",
                min_value=0,
                max_value=100
            )
        }
    )

    # ========================================
    # key -- FUNDAMENTAL PARA EL STATE
    # ========================================
    st.subheader("Parámetro: key")

    with st.echo():
        st.dataframe(df, key="tabla_unica")

    # ========================================
    # on_select
    # ========================================
    st.subheader("Parámetro: on_select")

    with st.echo():
        st.dataframe(df, on_select="ignore")

    # ========================================
    # selection_mode
    # ========================================
    st.subheader("Parámetro: multi-select")

    with st.echo():
        selection = st.dataframe(
            df,
            on_select="rerun",
            selection_mode="multi-row",
            key="tabla_rerun"
        )

        st.write("Selección actual:")
        st.write(selection)

    # ========================================
    # row_height
    # ========================================
    st.subheader("Parámetro: row_height")

    with st.echo():
        st.dataframe(df, row_height=50)
    
   

    # ========================================
    # placeholder
    # ========================================
    st.code('st.dataframe(data=None, placeholder="Cargando datos...")')
    st.subheader("Parámetro: placeholder")

    with st.echo():
        st.dataframe(
            data=None,
            placeholder="Cargando datos..."
        )

    
    """
    Muestra un DataFrame interactivo
    """
    pass

# ----------------------------------
# st.data_editor
# ----------------------------------
def editor_dataframe():
    """
    Editor interactivo de DataFrame
    Permite modificar valores
    """
    pass


# ----------------------------------
# st.column_config
# ----------------------------------
def configurar_columnas():
    """
    Configuración de columnas para st.dataframe o st.data_editor
    """
    pass


# ----------------------------------
# add (uso típico con st.session_state o listas)
# ----------------------------------
def agregar_elemento():
    """
    Agrega un elemento (ej: fila, valor, estado)
    """
    pass


# ----------------------------------
# st.table
# ----------------------------------
def mostrar_tabla():
    """
    Muestra una tabla estática (no interactiva)
    """
    pass


# ----------------------------------
# st.metric
# ----------------------------------
def mostrar_metrica():
    """
    Muestra una métrica con valor y delta
    """
    pass


# ----------------------------------
# st.json
# ----------------------------------
def mostrar_json():
    """
    Muestra datos en formato JSON
    """
    pass
