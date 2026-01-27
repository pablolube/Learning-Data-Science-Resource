import streamlit as st

# ======================
# FORMATOS DE HEADER
# ======================

def header_body():
    st.title("title")
    st.header("Header")
    st.subheader("Subeader")
    st.markdown("Markdwon")

def title():
    st.code('st.title(body, anchor=None, *, help=None, width="stretch", text_alignment="left")')
   
    # ==================================================
    # EJEMPLOS DE CADA PARÁMETRO
    # ==================================================

    # 1️⃣ body (texto principal)
    st.title("Dashboard de Ventas")

    # 2️⃣ anchor (ancla para navegación interna)
    st.title("Sección Principal", anchor="seccion-principal")
    st.markdown("[Ir a Sección Principal](#seccion-principal)")

    # 3️⃣ help (tooltip informativo)
    st.title(
        "Modelo de Predicción",
        help="Este título describe el modelo usado"
    )

    # 4️⃣ width (control del ancho)
    st.title(
        "Resumen Ejecutivo",
        width="content"
    )

    # 5️⃣ text_alignment (alineación del texto)
    st.title(
        "KPIs Principales",
        text_alignment="center"
    )

    # ==================================================
    # TODOS LOS PARÁMETROS JUNTOS
    # ==================================================
    st.title(
        body="Informe Final",
        anchor="informe-final",
        help="Resumen completo del análisis",
        width="content",
        text_alignment="center")

def headers():

    # 1️⃣ Header simple
    st.header("Análisis de datos")

    # 2️⃣ Header con negrita y cursiva
    st.header("**Análisis** de *Datos*")

    # 3️⃣ Header con emojis
    st.header("📊 Análisis Exploratorio de Datos")

    # 4️⃣ Header con enlace
    st.header("Documentación oficial de [Streamlit](https://docs.streamlit.io)")

    # 5️⃣ Header con código inline
    st.header("Uso de la función `st.header()`")

    # 6️⃣ Header con listas
    st.header("""
    ### Pasos del proyecto
    - Cargar datos
    - Limpiar información
    - Analizar métricas
    """)

    # 7️⃣ Header con blockquote
    st.header("""
    > *"Sin datos solo eres otra persona con una opinión"*
    """)

    # 8️⃣ Header con separador
    st.header("Resultados finales", divider=True)

    # 9️⃣ Header con help
    st.header(
        "📈 Métricas del modelo",
        help="Sección donde se muestran las métricas principales",
        divider=True
    )

    # ======================
    # PARÁMETROS
    # ======================

    # Anchor
    st.header("Anchor", anchor="anchor-header")

    # Help
    st.header(
        "Help",
        help="Aquí tienes detalle de la ayuda. Documentación oficial de Streamlit."
    )

    # Divider
    st.header("Divider rainbow", divider="rainbow")
    st.header("Divider blue", divider="blue")
    st.header("Divider red", divider="red")
    st.header("Divider default", divider=True)

    # Width
    st.header("Width stretch (default)", divider=True, width="stretch")
    st.header("Width content", divider=True, width="content")
    st.header("Width 200px", divider=True, width=200)
    st.header("Width 500px", divider=True, width=500)

    # Aclaración sobre alineación
    st.info(
        "ℹ️ st.header() NO soporta alineación de texto. "
        "Para alinear texto se debe usar st.markdown() + HTML."
    )

def subheader():
    #Clasico
    st.code(
        'st.subheader(body, anchor=None, *, help=None, divider=False, width="stretch", text_alignment="left")',
        language="python")

    # 1️⃣ body (texto principal)
    st.subheader("Análisis de Ventas")

    # 2️⃣ anchor (ancla para navegación interna)
    st.subheader("anchor", anchor="resultados")

    # 3️⃣ help (tooltip informativo)
    st.subheader(
        "help",
        help="Resultados generados con Random Forest"
    )

    # 4️⃣ divider (línea divisoria)
    st.subheader(
        "Divider",
        divider=True
    )

    # 5️⃣ width (ajusta el ancho)
    st.subheader(
        "width",divider=(True),
        width="content"
    )

    # 6️⃣ text_alignment (alineación del texto)
    st.subheader(
        "Dashboard de KPIs",
        text_alignment="center"
    )

    # ✅ Todos los parámetros juntos
    st.subheader(
        body="Todos los parametros",
        anchor="informe-final",
        help="Este informe resume todos los resultados",
        divider=True,
        width="content",
        text_alignment="center"
    )

def markdown():
    st.code('st.markdown(body, unsafe_allow_html=False, *, help=None, width="stretch", text_alignment="left")')

    # 1️⃣ Markdown básico
    st.markdown("""
    # Título
    ## Subtítulo
    **Negrita** | *Cursiva* | `Código`
    - Item 1
    - Item 2
    """)

    # 2️⃣ Emojis (shortcodes)
    st.markdown("Esto es genial :+1: :sunglasses:")

    # 3️⃣ Logo de Streamlit
    st.markdown("Hecho con :streamlit:")

    
    

    # 4️⃣ Símbolos tipográficos automáticos
    st.markdown("Operadores: <- -> <-> -- >= <= ~=")

    # 5️⃣ Google Material Symbols (rounded)
    st.markdown("Iconos: :material/home: :material/search: :material/settings:")

    # 6️⃣ LaTeX (fórmula en línea)
    st.markdown("Latex Fórmula en línea: $E = mc^2$")

    # 7️⃣ LaTeX (bloque)
    st.markdown(""" Latex Formula en bloque
    $$
    \\sum_{i=1}^{n} x_i = \\bar{x}
    $$
    """)

    # 8️⃣ Texto con color
    st.markdown(":red[Texto rojo] :green[Texto verde] :blue[Texto azul]")

    # 9️⃣ Texto con fondo de color
    st.markdown(":yellow-background[Texto con fondo amarillo]")

    # 🔟 Texto con color primario del theme
    st.markdown(":primary[Texto con color primario]")

    # 1️⃣1️⃣ Badges de color
    st.markdown(
        ":green-badge[OK] "
        ":orange-badge[WARNING] "
        ":red-badge[ERROR]"
    )

    # 1️⃣2️⃣ Texto pequeño
    st.markdown(":small[Este texto se ve más pequeño]")

    # ==================================================
    # EJEMPLO COMBINADO (estilo apunte)
    # ==================================================
    st.markdown("""
  
    ### Observación :material/info:

    :blue-badge[Markdown] permite usar  
    - emojis :rocket:
    - fórmulas $a^2 + b^2 = c^2$
    - :orange[texto coloreado]
    - :gray-background[fondos]
    - :small[texto pequeño]

    Hecho con :streamlit:
    """)

    # ==================================================
    # EJEMPLOS DE CADA PARÁMETRO
    # ==================================================

    # 1️⃣ body (texto en Markdown)
    st.markdown("""
    ### Título en Markdown
    - **Negrita**
    - *Cursiva*
    - `Código`
    """)

    # 2️⃣ unsafe_allow_html (permite HTML)
    st.markdown(
        "<h3 style='color:blue;'>Título con HTML</h3>",
        unsafe_allow_html=True
    )

    # 3️⃣ help (tooltip informativo)
    st.markdown(
        "**Modelo entrenado**",
        help="Este texto explica el modelo utilizado"
    )

    # 4️⃣ width (control del ancho)
    st.markdown(
        "Texto con ancho ajustado al contenido",
        width="content"
    )

    # 5️⃣ text_alignment (alineación del texto)
    st.markdown(
        "Texto centrado",
        text_alignment="center"
    )

    # ==================================================
    # TODOS LOS PARÁMETROS JUNTOS
    # ==================================================
    st.markdown(
        body="""
        :blue-badge[INFO]  
        **Markdown con todos los parámetros**
        """,
        unsafe_allow_html=False,
        help="Ejemplo completo de st.markdown",
        width="content",
        text_alignment="center"
    )

def observaciones_formato():
    st.info(
    """
    **Observación**

    `st.title()`, `st.header()` y `st.subheader()` **no permiten**
    cambiar color, tipo de letra o tamaño desde sus parámetros.

    Para personalizar el formato se debe usar:
    - `st.markdown()` con **HTML + CSS**
    - `unsafe_allow_html=True`

    Ejemplo:
    `<h1 style='color:red; text-align:center;'>Título</h1>`
    """
    )