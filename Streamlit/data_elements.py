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
    import streamlit as st
    import pandas as pd

    st.subheader("✏️ Data Editor")

    st.code(
        'st.data_editor(data, *, width="stretch", height="auto", '
        'use_container_width=None, hide_index=None, column_order=None, '
        'column_config=None, num_rows="fixed", disabled=False, key=None, '
        'on_change=None, args=None, kwargs=None, row_height=None, placeholder=None)'
    )

    # ----------------------------------------
    # DataFrame base
    # ----------------------------------------
    df = pd.DataFrame({
        "Nombre": ["Ana", "Juan", "Luis"],
        "Edad": [25, 30, 22],
        "Ciudad": ["Buenos Aires", "Córdoba", "Rosario"]
    })

    # =========================================================
    st.header("Base")
    with st.echo():
        st.data_editor(df, key="editor_base") 
        
    st.info("La key sirve sobre todo para el manejo de estados")

    # =========================================================
    st.header("1️⃣ use_container_width")
    with st.echo():
        st.data_editor(
            df,
            use_container_width=False, 
            # cambia si el ancho de la tabla ocupa todo el contenedor
            key="editor_container_width"
        )

    # =========================================================
    st.header("2️⃣ hide_index")
    with st.echo():
        st.data_editor(
            df,
            hide_index=True,
            key="editor_hide_index"
        )
    st.info("Oculta el indice")

    # =========================================================
    st.header("3️⃣ column_order")
    with st.echo():
        st.data_editor(
            df,
            column_order=["Ciudad", "Nombre", "Edad"],
            key="editor_column_order"
        )
    st.info("No acepta dic o condicionales, para eso usar sorted u ordenaciones previas en pandas")

    # =========================================================
    st.header("4️⃣ column_config")
    st.info("Ver column config mas abajo para mas detalle")
    with st.echo():
        st.data_editor(
            df,
            column_config={
                "Nombre": st.column_config.TextColumn(
                    label="Nombre completo",
                    help="Ingrese el nombre",
                    max_chars=15
                ),
                "Edad": st.column_config.NumberColumn(
                    label="Edad",
                    min_value=0,
                    max_value=120,
                    step=1
                ),
                "Ciudad": st.column_config.SelectboxColumn(
                    label="Ciudad",
                    options=["Buenos Aires", "Córdoba", "Rosario", "Mendoza"]
                )
            },
            key="editor_column_config"
        )
    
    # =========================================================
    st.header("5️⃣ num_rows = 'fixed'")

    st.markdown("""
### 🔢 `num_rows` — Control de filas en `st.data_editor`

Define si el usuario puede **agregar** y/o **eliminar** filas en el editor.

---

#### 🧷 Opciones disponibles

- **`"fixed"` (por defecto)**  
  - ❌ No permite agregar ni eliminar filas  
  - ✅ Permite ordenar columnas  

- **`"dynamic"`**  
  - ✅ Permite agregar y eliminar filas  
  - ❌ Desactiva el ordenamiento de columnas  

- **`"add"`**  
  - ✅ Permite **solo agregar** filas  
  - ❌ No permite eliminar filas  
  - ❌ Desactiva el ordenamiento de columnas  

- **`"delete"`**  
  - ❌ No permite agregar filas  
  - ✅ Permite **solo eliminar** filas  
  - ✅ Mantiene el ordenamiento de columnas  

---

💡 **Tip**  
Usá `"fixed"` para vistas de solo edición controlada  
y `"dynamic"` para escenarios tipo CRUD.
""")

    with st.echo():
        st.data_editor(
            df,
            num_rows="dynamic",
            key="editor_num_rows_fixed"
        )

    # =========================================================
    st.header("6️⃣ num_rows = 'dynamic'")
    with st.echo():
        st.data_editor(
            df,
            num_rows="dynamic",
            key="editor_num_rows_dynamic"
        )

    # =========================================================
    st.header("7️⃣ disabled = [Edad]")
    st.info("Disable te permite desactivar la edicion ,por columna/s, todas o ninguna")
    st.text("En este caso deshabilito la edicion para edad")
    with st.echo():
        st.data_editor(
            df,
            disabled=["Edad"],
            key="editor_disabled"
        )

    # =========================================================
    st.header("8️⃣ key explícita")
    with st.echo():
        st.data_editor(
            df,
            key="editor_key_demo"
        )

    # =========================================================
    st.header("9️⃣ on_change")

    def aviso():
        st.success("¡La tabla fue modificada!")

    with st.echo():
        st.data_editor(
            df,
            key="editor_on_change",
            on_change=aviso
        )

    # =========================================================
    st.header("🔟 row_height")
    with st.echo():
        st.data_editor(
            df,
            row_height=60,
            key="editor_row_height"
        )

# ----------------------------------
# st.column_config
# ----------------------------------
def configurar_columnas():
    """
    Configuración de columnas para st.dataframe o st.data_editor
    """
    pass

# ----------------------------------
# st.table
# ----------------------------------
def mostrar_tabla():
    st.info("Es para tablas simples que no requieren navegación")
    st.code("st.table(data=None, *, border=True")


    df = pd.DataFrame({
            "Nombre": ["Ana", "Juan", "Luis"],
            "Edad": [25, 30, 22],
            "Ciudad": ["Buenos Aires", "Córdoba", "Rosario"]
        })

    st.subheader("Ejemplo tabla simple")
    with st.echo():
        st.table(df)

    st.subheader("Paramentro border")
    with st.echo():
        st.table(df,border=True)

    with st.echo():
        st.table(df,border=False)
        
    with st.echo():
        st.table(df,border="horizontal")


# ----------------------------------
# st.metric
# ----------------------------------
def mostrar_metrica():
    """
    Muestra una métrica con valor y delta
    """

    st.code('st.metric(label, value, delta=None, delta_color="normal", *, help=None, label_visibility="visible", border=False, width="stretch", height="content", chart_data=None, chart_type="line", delta_arrow="auto", format=None)',width="stretch")

    # --------------------------------------------------
    # label (Markdown permitido)
    # --------------------------------------------------
    st.subheader("label (con Markdown)")
    with st.echo():
        st.metric(
            label="**Usuarios activos** 🚀",
            value=1200
        )

    # --------------------------------------------------
    # value (int, float, str, None)
    # --------------------------------------------------
    st.subheader("value (int, float, str, None)")
    with st.echo():
        st.metric("Ventas", 150)

    with st.echo():
        st.metric("Temperatura", 23.5)

    with st.echo():
        st.metric("Estado", "OK")

    with st.echo():
        st.metric("Dato faltante", None)

    # --------------------------------------------------
    # delta (positivo, negativo, None)
    # --------------------------------------------------
    st.subheader("PARAMETRO DELTA")
    with st.echo():
        st.metric("Ingresos", 5000, delta=300)

    with st.echo():
        st.metric("Errores", 12, delta=-4)

    with st.echo():
        st.metric("Sin cambio", 100, delta=None)

    # --------------------------------------------------
    # delta_color
    # --------------------------------------------------
    st.subheader("delta_color")
    with st.echo():
        st.metric("Costo", 2000, delta=-150, delta_color="inverse")

    with st.echo():
        st.metric("Usuarios", 1000, delta=50, delta_color="blue")

    with st.echo():
        st.metric("Neutral", 10, delta=2, delta_color="off")

    # --------------------------------------------------
    # help (tooltip)
    # --------------------------------------------------
    st.subheader("help (tooltip)")
    with st.echo():
        st.metric(
            "Conversión",
            "2.4%",
            help="Porcentaje de usuarios que completaron la acción"
        )

    # --------------------------------------------------
    # label_visibility
    # --------------------------------------------------
    st.subheader("label_visibility")
    with st.echo():
        st.metric(
            "Visible",
            100,
            label_visibility="visible"
        )

    with st.echo():
        st.metric(
            "Hidden",
            100,
            label_visibility="hidden"
        )

    with st.echo():
        st.metric(
            "Collapsed",
            100,
            label_visibility="collapsed"
        )

    # --------------------------------------------------
    # border
    # --------------------------------------------------
    st.subheader("border")
    with st.echo():
        st.metric(
            "Con borde",
            42,
            border=True
        )

    # --------------------------------------------------
    # width
    # --------------------------------------------------
    st.subheader("width")
    with st.echo():
        st.metric(
            "Ancho fijo",
            300,
            width=200 # ancho del rectangulo
        )

    # --------------------------------------------------
    # height
    # --------------------------------------------------
    st.subheader("height")
    with st.echo():
        st.metric(
            "Alto fijo",
            99,
            height=120 #"alto del rectangulo"
        )

    # --------------------------------------------------
    # chart_data
    # --------------------------------------------------
    st.subheader("chart_data")
    with st.echo():
        st.metric(
            "Usuarios por día",
            120,
            delta=10,
            chart_data=[80, 1500, 100, 110, 120] 
            #Esto agrega un grafico
        )

    # --------------------------------------------------
    # chart_type
    # --------------------------------------------------
    st.subheader("chart_type")

    with st.echo():
        
        changes = list(rng(4).standard_normal(20))
        data = [sum(changes[:i]) for i in range(20)]
        delta = round(data[-1], 2)

        row = st.container(horizontal=True)
        with row:
            st.metric(
                "Line", 10, delta, chart_data=data, chart_type="line", border=True
            )
            st.metric(
                "Area", 10, delta, chart_data=data, chart_type="area", border=True
            )
            st.metric(
                "Bar", 10, delta, chart_data=data, chart_type="bar", border=True
            )
    # --------------------------------------------------
    # delta_arrow
    # --------------------------------------------------
    st.subheader("delta_arrow  - Direccion de la flecha")
    with st.echo():
        st.metric(
            "Forzado arriba",
            100,
            delta=-20,
            delta_arrow="up"
        ) # flecha obliga  a ir hacia arriba

    with st.echo():
        st.metric(
            "Forzado abajo",
            100,
            delta=20,
            delta_arrow="down"
        )

    with st.echo():
        st.metric(
            "Sin flecha",
            100,
            delta=20,
            delta_arrow="off" # No muestra flecha pero sigue estan el delta
        )

    # --------------------------------------------------
    # format
    # --------------------------------------------------
    st.subheader("FORMAT")
    with st.echo():
        st.metric(
            "Porcentaje",
            0.256,
            delta=0.034,
            format="percent"
        )

    with st.echo():
        st.metric(
            "Dólares",
            1234.56,
            delta=120,
            format="dollar"
        )

    with st.echo():
        st.metric(
            "Compacto",
            12500,
            delta=2300,
            format="compact"
        )

    with st.echo():
        st.metric(
            "Printf",
            3.14159,
            delta=0.1234,
            format="%.2f"
        )


    st.info("st.metric no maneja formateos para el borde ni la caja, lo que se puede hacer envolverlo en css usndo markdown como muestro a continuacion")
            
    st.markdown(
    """
    <style>
    .metric-box {
        border: 2px solid #4CAF50;
        border-radius: 12px;
        padding: 16px;
        background-color: #0f172a;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    st.markdown('<div class="metric-box">', unsafe_allow_html=True)
    st.metric("Con borde custom", 42, delta=5)
    st.markdown('</div>', unsafe_allow_html=True)


# ----------------------------------
# st.json
# ----------------------------------
def mostrar_json():
    """
    Muestra datos en formato JSON
    """
    pass







