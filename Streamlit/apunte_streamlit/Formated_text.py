import streamlit as st
import math
import pandas as pd

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
        text_alignment="center")

def code():
    # Código de ejemplo que vamos a mostrar en st.code
    codigo_python = """
    def saludar(nombre):
        print(f"Hola {nombre}")

    saludar("Pablo")
    """

    # -------------------------------
    # EJEMPLO COMPLETO DE st.code
    # -------------------------------

    st.code(
        codigo_python,          # body -> el código que se va a mostrar
        language="python",       # language -> lenguaje para resaltado de sintaxis
        line_numbers=True,       # muestra números de línea
        wrap_lines=True,         # ajusta líneas largas (no hace scroll horizontal)
        height="content",        # altura automática según el contenido podes darle el contenido en pixeles
        width="stretch"          # ocupa todo el ancho disponible
    )

    # -------------------------------
    # VARIACIONES PARA ENTENDER CADA PARÁMETRO
    # -------------------------------

    st.write("Sin números de línea:")
    st.code(codigo_python, language="python", line_numbers=False)

    st.write("Sin ajuste de líneas (wrap_lines=False):")
    st.code(codigo_python, language="python", wrap_lines=False)

    st.write("Altura fija (height=200):")
    st.code(codigo_python, language="python", height=200)

    st.write("Ancho automático (width='auto'):")
    st.code(codigo_python, language="python", width="stretch")

def divider():
    st.text('You can achieve the same effect with st.write("---") or even just "---" in your script (via magic).')
    st.text('la función st.divider() de Streamlit no permite cambiar color, tipo de línea o grosor más allá de lo que documenta la API. Según la documentación oficial, st.divider() solo tiene un parámetro width (puede ser "stretch" o un número de pixeles) y no expone opciones para color, estilo de borde o grosor personalizado.')
    st.divider(width=10)
    st.divider()
    st.code('width ("stretch" or int)')
    st.divider(width=100)

def echo():
    
    st.set_page_config(page_title="Demo st.echo", layout="centered")

    st.title("🔁 Ejemplos de st.echo() en Streamlit")
    st.write("`st.echo()` muestra el código y ejecuta lo que está dentro.")

    st.divider()

    # --------------------------------------------------
    # EJEMPLO 1: Código simple
    # --------------------------------------------------
    st.subheader("1️⃣ Código básico")

    with st.echo():
        st.write("Hola, esto es un ejemplo simple de st.echo()")
        x = 10
        st.write("El valor de x es:", x)

    st.divider()

    # --------------------------------------------------
    # EJEMPLO 2: Condicionales
    # --------------------------------------------------
    st.subheader("2️⃣ Condicionales")

    with st.echo():
        edad = 20

        if edad >= 18:
            st.success("Sos mayor de edad")
        else:
            st.error("Sos menor de edad")

    st.divider()

    # --------------------------------------------------
    # EJEMPLO 3: Bucles
    # --------------------------------------------------
    st.subheader("3️⃣ Bucles")

    with st.echo():
        for i in range(5):
            st.write(f"Número: {i}")

    st.divider()

    # --------------------------------------------------
    # EJEMPLO 4: Funciones
    # --------------------------------------------------
    st.subheader("4️⃣ Funciones")

    with st.echo():
        def saludar(nombre):
            return f"Hola {nombre} 👋"

        mensaje = saludar("Pablo")
        st.write(mensaje)

    st.divider()

    # --------------------------------------------------
    # EJEMPLO 5: Widgets
    # --------------------------------------------------
    st.subheader("5️⃣ Widgets interactivos")

    with st.echo():
        nombre = st.text_input("Escribí tu nombre")
        if nombre:
            st.write(f"Hola {nombre}! 😄")

    st.divider()

    # --------------------------------------------------
    # EJEMPLO 6: Gráficos simples
    # --------------------------------------------------
    st.subheader("6️⃣ Gráfico simple")

    with st.echo():
        import pandas as pd

        datos = pd.DataFrame({
            "x": [1, 2, 3, 4, 5],
            "y": [10, 20, 30, 25, 15]
        })

        st.line_chart(datos)

    st.divider()

    st.info("Todo el código que ves arriba está siendo ejecutado y mostrado gracias a st.echo()")

def latex():
    st.code('st.latex(body, *, help=None, width="stretch")')
    st.text("Devuelve el codigo en formato latex")
    st.latex(r'''a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

def text():
    st.code('st.text(body, *, help=None, width="content", text_alignment="left")')
    st.text("st.text() es muy básico: muestra texto plano sin formato ni desplazamiento (scroll)") 

def pagina_help():
    st.markdown("""
    ### ℹ️ ¿Qué hace `st.help()`?

    Muestra información introspectiva de un objeto:
    - Nombre
    - Tipo
    - Firma
    - Docstring
    - Métodos
    - Atributos
    - Documentación interna

    👉 Ideal para explorar objetos en tiempo real dentro de la app.
    """)

    st.title("📘 Casos de uso de st.help()")
    st.write("Exploración, aprendizaje y debug interactivo")

    # --------------------------------------------------
    # 1️⃣ Función propia
    # --------------------------------------------------
    def suma(a, b):
        """Suma dos números y devuelve el resultado."""
        return a + b

    st.header("1️⃣ Explorar una función propia")
    st.help(suma)

    # --------------------------------------------------
    # 2️⃣ Función de Streamlit
    # --------------------------------------------------
    st.header("2️⃣ Explorar una función de Streamlit")
    st.help(st.text_area)

    # --------------------------------------------------
    # 4️⃣ Clase propia
    # --------------------------------------------------
    class Persona:
        """Representa una persona"""

        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def saludar(self):
            """Devuelve un saludo"""
            return f"Hola, soy {self.nombre}"

    st.header("4️⃣ Explorar una clase")
    st.help(Persona)

    # --------------------------------------------------
    # 5️⃣ Instancia de objeto
    # --------------------------------------------------
    persona = Persona("Ana", 30)

    st.header("5️⃣ Explorar una instancia de objeto")
    st.help(persona)

    # --------------------------------------------------
    # 6️⃣ Librería externa (pandas)
    # --------------------------------------------------
    st.header("6️⃣ Explorar librerías externas (pandas)")
    st.help(pd.DataFrame)

    # --------------------------------------------------
    # 7️⃣ Selector interactivo (modo educativo)
    # --------------------------------------------------
    st.header("7️⃣ Selector interactivo de objetos")

    opcion = st.selectbox(
        "Seleccioná qué querés explorar:",
        (
            st.text,
            st.markdown,
            st.code,
            st.dataframe,
            pd.read_csv
        )
    )

    st.help(opcion)

def html():
   

    st.title("Ejemplo de st.html()")

    st.html(
        """
        <div style="
            border: 2px solid #4CAF50;
            padding: 16px;
            border-radius: 8px;
            background-color: #f0fff4;
            font-family: Arial;
        ">
            <h3>📦 Caja HTML incrustada</h3>
            <p>
                Este contenido está renderizado usando <b>st.html()</b>.
            </p>
            <ul>
                <li>HTML puro</li>
                <li>CSS inline</li>
                <li>Sin JavaScript</li>
            </ul>
        </div>
        """
    )
    
    st.markdown("""
    ### 🔐 Parámetro `unsafe_allow_javascript`

    - Por defecto, `unsafe_allow_javascript = False`
    - ❌ **No se ejecuta JavaScript**
    - ✅ Solo se renderiza **HTML + CSS**
    - 🛡️ Es un comportamiento **seguro**

    👉 Usar `True` **solo** en casos muy controlados y con código propio.
    """)
