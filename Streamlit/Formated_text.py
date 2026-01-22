import streamlit as st


import streamlit as st

def badge():
    # ==================================================
    # REFERENCIA DEL MÉTODO
    # ==================================================
    st.code(
        'st.badge(label, *, icon=None, color="blue", width="content", help=None)',
        language="python"
    )

    # ==================================================
    # EJEMPLOS DE CADA PARÁMETRO
    # ==================================================

    # 1️⃣ label (texto del badge)
    st.badge("Nuevo")

    # label con Markdown permitido
    st.badge("**Beta** `v1.2`")

    # 2️⃣ icon (emoji o Material Symbol)
    st.badge("Alerta", icon="🚨")
    st.badge("Aprobado", icon=":material/check:")

    # 3️⃣ color (color del badge)
    st.badge("Error", color="red")
    st.badge("Warning", color="orange")
    st.badge("OK", color="green")
    st.badge("Info", color="blue")

    # 4️⃣ width
    st.badge("Content width", width="content")   # default
    st.badge("Stretch width", width="stretch")   # ocupa todo el ancho
    st.badge("200px width", width=10)    #me corta la palabra
            # ancho fijo

    # 5️⃣ help (tooltip)
    st.badge(
        "Con ayuda",
        help="Este badge muestra un **tooltip** con Markdown"
    )

    # ==================================================
    # TODOS LOS PARÁMETROS JUNTOS
    # ==================================================
    st.badge(
        label="Éxito",
        icon=":material/thumb_up:",
        color="green",
        width="content",
        help="Operación completada correctamente"
    )

    # ==================================================
    # COMPARACIÓN CON MARKDOWN (BADGES EN LÍNEA)
    # ==================================================
    st.markdown(
        ":violet-badge[:material/star: Favorito] "
        ":orange-badge[⚠️ Revisión] "
        ":gray-badge[Deprecated]"
    )
    etiquetas = ["Nuevo", "Beta", "Activo"]

    cols = st.columns(len(etiquetas))
    for col, etiqueta in zip(cols, etiquetas):
        with col:
            st.badge(etiqueta)

def caption():
    st.code('st.caption(body, unsafe_allow_html=False, *, help=None, width="stretch", text_alignment="left")')
    st.caption("Caption") # No aclaro porque los parametros son iguales al resto
    st.subheader("Casos de uso: ")
    # ==================================================
    # CASOS DE USO DE st.caption()
    # ==================================================

    # 1️⃣ Pie de gráfico
    st.line_chart([10, 20, 15, 30])
    st.caption("Fuente: datos simulados (2024)")

    # 2️⃣ Aclaración debajo de un título
    st.header("Análisis de Ventas")
    st.caption("Los valores están expresados en miles de USD")

    # 3️⃣ Nota / advertencia corta
    st.caption("⚠️ Este dashboard se actualiza cada 24 horas")

    # 4️⃣ Documentación / apunte técnico
    st.caption("`st.caption()` se usa para texto secundario o explicativo")

    # 5️⃣ Tooltip con help
    st.caption(
        "Métrica normalizada",
        help="Se calcula como **valor actual / valor máximo**"
    )

    # 6️⃣ Alineación del texto
    st.caption(
        "Texto centrado",
        text_alignment="center"
    )

    st.caption(
        "Texto justificado para explicaciones largas que ocupan más espacio",
        text_alignment="justify"
    )

    # 7️⃣ Control de ancho
    st.caption(
        "Texto ajustado al contenido",
        width="content"
    )

    st.caption(
        "Texto con ancho fijo",
        width=300
    )

    # 8️⃣ Markdown (énfasis, código, emojis)
    st.caption(
        "Resultado **experimental** 🧪 — versión `v2.1`"
    )

    # 9️⃣ HTML (solo si es necesario)
    st.caption(
        "<span style='color:gray;'>Texto con HTML</span>",
        unsafe_allow_html=True
    )

    # ==================================================
    # EJEMPLO RESUMEN (estilo apunte)
    # ==================================================
    st.caption(
        """
        **st.caption()**
        • Texto pequeño  
        • Notas, pies de gráfico y aclaraciones  
        • Soporta Markdown, tooltip, alineación y ancho
        """,
        text_alignment="center"
)

def code():
    pass
def divider():
    pass
def echo():
    pass
def latex():
    pass
def text():
    pass
def help():
    pass
def html():
    pass