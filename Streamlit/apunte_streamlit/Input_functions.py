import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date,time,timedelta
import datetime
from datetime import datetime


# =========================
# BUTTONS
# =========================


def button():

    # -------------------------------------------------
    # Function signature
    # -------------------------------------------------

    st.code(
        'st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, '
        'type="secondary", icon=None, icon_position="left", disabled=False, '
        'use_container_width=None, width="content", shortcut=None)'
    )

    # =================================================
    # LABEL PARAMETER
    # =================================================

    st.subheader("Parámetro label")

    with st.expander("Ejemplos del parámetro label"):

        with st.echo():

            # Texto simple
            st.button("Enviar")
            st.button("Guardar cambios")

            # Markdown básico
            st.button("**Guardar**")
            st.button("*Cancelar*")
            st.button("~~Eliminar~~")
            st.button("`Run`")
            st.button("💾 **Guardar** cambios")

            # Link
            st.button("[Ir a Google](https://google.com)")

            # Imagen como icono
            st.button(
                "![Logo](https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png)"
            )

            # Markdown no soportado
            st.markdown("❌ Markdown complejo:")
            st.button("1. Opción uno")

            # Escapando markdown
            st.markdown("✅ Escapado:")
            st.button("1\\. Opción uno")

            # Ejemplo recomendado
            st.button("🚀 **Ejecutar** proceso")


    # =================================================
    # ON_CLICK PARAMETER
    # =================================================

    st.subheader("Parámetro on_click")

    with st.expander("Ejemplo callback"):

        with st.echo():

            st.info("Ejecuta una función cuando se presiona el botón")

            def saludar():
                st.write("Hola 👋")

            st.button("Saludar", on_click=saludar)


    # =================================================
    # ICON PARAMETER
    # =================================================

    st.subheader("Parámetro icon")

    with st.expander("Ejemplos de iconos"):

        with st.echo():

            # Material icon
            st.button("Configuración", icon=":material/settings:")

            # Spinner
            st.button("Cargando...", icon="spinner")

            # Enviar
            st.button("Enviar formulario", icon=":material/send:")


    # =================================================
    # ICON_POSITION PARAMETER
    # =================================================

    st.subheader("Parámetro icon_position")

    with st.expander("Posición del icono"):

        with st.echo():

            # Icono a la izquierda (default)
            st.button(
                "Guardar",
                icon=":material/save:",
                icon_position="left"
            )

            # Icono a la derecha
            st.button(
                "Guardar",
                icon=":material/save:",
                icon_position="right"
            )


    # =================================================
    # DISABLED PARAMETER
    # =================================================

    st.subheader("Parámetro disabled")

    with st.expander("Botón deshabilitado"):

        with st.echo():

            st.button("Botón activo")

            st.button(
                "Botón deshabilitado",
                disabled=True
            )


    # =================================================
    # SHORTCUT PARAMETER
    # =================================================

    st.subheader("Parámetro shortcut")

    with st.expander("Ejemplos de atajos de teclado"):

        with st.echo():

            # Tecla simple
            st.button(
                "Presionar con K",
                shortcut="K"
            )

            # Tecla función
            st.button(
                "Pantalla completa",
                shortcut="F11"
            )

            # Tecla especial
            st.button(
                "Enviar",
                shortcut="Enter"
            )

            # Con modificadores
            st.button(
                "Buscar",
                shortcut="Ctrl+K"
            )

            st.button(
                "Abrir opciones",
                shortcut="Cmd+Shift+O"
            )


    # =================================================
    # NOTAS IMPORTANTES SHORTCUT
    # =================================================

    st.info("""
    📌 Reglas importantes para shortcut:

    ❌ No se pueden usar: C ni R (ni con modificadores)
    ❌ No se permiten signos como . , ;

    ✅ Teclas especiales soportadas:
    Backspace, Delete, Enter, Esc, Tab, Space,
    Home, End, PageUp, PageDown,
    Left, Right, Up, Down

    ✅ Modificadores:
    Ctrl, Cmd, Meta, Mod, Shift, Alt, Option

    👉 Ctrl, Cmd, Meta y Mod son equivalentes
    👉 Alt y Option son equivalentes
    """)


    st.subheader("Parámetro type")

    with st.expander("Ejemplos de boton type"):

        with st.echo():
            st.button("Botón Primario", type="primary")
            st.button("Botón Secundario", type="secondary")
            st.button("Botón Terciario", type="tertiary")

def download_button():

    st.code(
        'st.download_button(label, data, file_name=None, mime=None, key=None, help=None, on_click="rerun", args=None, kwargs=None, *, type="secondary", icon=None, icon_position="left", disabled=False, use_container_width=None, width="content", shortcut=None)'
    )

    st.divider()

    # ================= LABEL =================

    st.subheader("📝 Parámetro label")

    with st.expander("Ejemplos del parámetro label"):

        st.caption("El label acepta texto y Markdown básico")

        with st.echo():
            st.download_button(
                label="Descargar archivo simple",
                data="Hola mundo"
            )

        with st.echo():
            st.download_button(
                label="**Descargar en negrita**",
                data="Texto con markdown"
            )

        with st.echo():
            st.download_button(
                label="Descargar con `código inline`",
                data="Ejemplo código"
            )

        with st.echo():
            st.download_button(
                label="[Documentación Streamlit](https://streamlit.io)",
                data="Link como label"
            )

    st.divider()

    # ================= DATA =================

    st.subheader("📦 Parámetro data")

    with st.expander("Ejemplos del parámetro data"):

        st.caption("Puede ser string, bytes, file-like o una función")

        # String
        with st.echo():
            st.download_button(
                label="Descargar string",
                data="Este es un texto simple",
                file_name="texto.txt"
            )

        # Bytes
        with st.echo():
            st.download_button(
                label="Descargar bytes",
                data=b"Contenido binario",
                file_name="binario.bin")
        # Callable
        def generar_archivo():
            return "Archivo generado al presionar"

        with st.echo():
            st.download_button(
                label="Descargar con callable",
                data=generar_archivo,
                file_name="generado.txt"
            )

    st.divider()

    # ================= FILE NAME =================

    st.subheader("📁 Parámetro file_name")

    with st.expander("Ejemplos del parámetro file_name"):

        with st.echo():
            st.download_button(
                label="Archivo TXT",
                data="Contenido TXT",
                file_name="archivo.txt"
            )

        with st.echo():
            st.download_button(
                label="Archivo CSV",
                data="col1,col2\n1,2\n3,4",
                file_name="datos.csv"
            )

        with st.echo():
            st.download_button(
                label="Archivo JSON",
                data='{"nombre": "Pablo", "edad": 35}',
                file_name="data.json"
            )

    st.divider()

    # ================= MIME =================

    st.subheader("📄 Parámetro mime")

    with st.expander("Ejemplos del parámetro mime"):

        st.info("""
        El MIME indica el tipo de archivo que se descarga.

        Sirve para:
        ✔ Identificar el formato  
        ✔ Abrirlo con el programa correcto  
        ✔ Evitar errores  

        Ejemplos:
        - text/plain
        - text/csv
        - application/json
        """)

        with st.echo():
            st.download_button(
                label="Texto plano",
                data="Texto simple",
                file_name="texto.txt",
                mime="text/plain"
            )

        with st.echo():
            st.download_button(
                label="CSV explícito",
                data="a,b\n1,2",
                file_name="archivo.csv",
                mime="text/csv"
            )

        with st.echo():
            st.download_button(
                label="JSON explícito",
                data='{"x": 10}',
                file_name="archivo.json",
                mime="application/json"
            )

    st.divider()

    # ================= ON_CLICK =================

    st.subheader("⚡ Parámetro on_click")

    with st.expander("Ejemplos del parámetro on_click"):

        st.info("""
        Controla qué ocurre cuando el usuario descarga el archivo:

        🔁 "rerun" → Descarga + recarga la app (default)  
        🚫 "ignore" → Solo descarga (sin rerun)  
        ⚙ Función → Descarga + ejecuta una acción  
        """)

        def aviso():
            st.session_state["mensaje"] = "✅ Archivo descargado!"

        # Rerun (default)
        with st.echo():
            st.download_button(
                label="Descarga con rerun (default)",
                data="Archivo default"
            )

        # Ignore
        with st.echo():
            st.download_button(
                label="Descarga sin rerun",
                data="Sin refrescar app",
                on_click="ignore"
            )

        # Callable
        with st.echo():
            st.download_button(
                label="Descarga con callback",
                data="Con función",
                on_click=aviso
            )

        if "mensaje" in st.session_state:
            st.success(st.session_state["mensaje"])

def form_submit_button():
    st.code('st.form_submit_button(label="Submit", help=None, on_click=None, args=None, kwargs=None, *, key=None, type="secondary", icon=None, icon_position="left", disabled=False, use_container_width=None, width="content", shortcut=None)')
    st.subheader(" Parámetro label")
    with st.expander("Ejemplos del parámetro "):
        with st.echo():
            with st.form("form_type"):
                st.info('Tiene que estar dentro de un st.form ')
                st.warning("Aqui iria tu formulario")
                st.form_submit_button("REGISTRATE")
    st.info('Para los parametros on_click, key, type, icon, icon_position, disabled, use_container_width, width, shortcut ver anteriores titulo que los explico dado que son lo mism para todos)')

# =========================
# LINKS
# =========================

def link_button():
    st.code('st.link_button(label, url, *, help=None, type="secondary", icon=None, icon_position="left", disabled=False, use_container_width=None, width="content", shortcut=None)')
    st.subheader(" Parámetro label")
    with st.echo():
            st.link_button("Go to gallery", "https://streamlit.io/gallery")

    
    st.subheader("Ejemplos de st.link_button")

    # ================= BOTÓN COMPLETO =================

    st.subheader("Botón con todos los parámetros")
    with st.echo():
        st.link_button(
            label="**Ir a Streamlit Docs**",
            url="https://docs.streamlit.io",
            help="Abrir la documentación oficial de Streamlit",
            type="primary",                      # Color de relleno principal
            icon=":material/open_in_new:",       # Icono material
            icon_position="left",
            disabled=False,
            width="content",
            shortcut="Ctrl+D"
        )

    st.divider()

    # ================= COLORES (TYPE) =================

    st.subheader("Formato visual con type (relleno)")

    with st.echo():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.link_button(
                "Primary (relleno fuerte)",
                "https://streamlit.io",
                type="primary"
            )

        with col2:
            st.link_button(
                "Secondary (normal)",
                "https://streamlit.io",
                type="secondary"
            )

        with col3:
            st.link_button(
                "Tertiary (solo texto)",
                "https://streamlit.io",
                type="tertiary"
            )

    st.divider()

    # ================= ICONOS =================

    st.subheader("Con iconos")
    with st.echo():
        st.link_button(
            "Con emoji",
            "https://google.com",
            icon="🚀",
            type="primary"
        )
    st.divider()

    # ================= WIDTH =================

    st.subheader("Control de ancho")
    with st.echo():
        st.link_button(
            "Ancho automático (content)",
            "https://streamlit.io",
            width="content"
        )
    with st.echo():
        st.link_button(
            "Ancho completo (stretch)",
            "https://streamlit.io",
            width="stretch",
            type="primary"
        )
    with st.echo():
        st.link_button(
            "Ancho fijo 300px",
            "https://streamlit.io",
            width=300,
            type="secondary"
        )

    st.divider()

    # ================= DISABLED =================

    st.subheader("Botón deshabilitado")

    st.link_button(
        "No disponible",
        "https://streamlit.io",
        disabled=True,
        type="primary"
    )

def page_link():
    dash_path='/workspaces/Learning-Data-Science-Resource/Streamlit/pages/02_dashboard.py'
    home_path="/workspaces/Learning-Data-Science-Resource/Streamlit/pages/01_home.py"
    # -------------------------------------------------
    # Function signature
    # -------------------------------------------------

    st.code(
        'st.page_link(page, *, label=None, icon=None, icon_position="left", help=None, '
        'disabled=False, use_container_width=None, width="content", query_params=None)'
    )

    # =================================================
    # PAGE PARAMETER
    # =================================================

    st.subheader("Parámetro page")

    with st.expander("Ejemplos del parámetro page"):

        with st.echo():

            # Página interna por ruta (recomendado)
            st.page_link(
                home_path,
                label="Ir a Home"
            )
            # Usando Path
            st.page_link(
                Path(dash_path),
                label="Ir a Dashboard"
            )

            # URL externa
            st.page_link(
                "https://streamlit.io",
                label="Ir a Streamlit (externo)"
            )

    # =================================================
    # LABEL PARAMETER
    # =================================================

    st.subheader("Parámetro label")

    with st.expander("Ejemplos del parámetro label"):

        with st.echo():

            # Texto simple
            st.page_link(home_path, label="Inicio")

            # Markdown básico
            st.page_link(home_path, label="**Inicio**")
            st.page_link(home_path, label="*Volver*")
            st.page_link(home_path, label="~~Salir~~")
            st.page_link(home_path, label="`Home`")

            # Emoji
            st.page_link(home_path, label="🏠 Inicio")

            # Link como texto
            st.page_link(
                home_path,
                label="[Home](https://streamlit.io)"
            )

            # Markdown no soportado
            st.markdown("❌ Markdown complejo:")
            st.page_link(home_path, label="1. Opción uno")

            # Escapado
            st.markdown("✅ Escapado:")
            st.page_link(home_path, label="1\\. Opción uno")

            # Recomendado
            st.page_link(home_path, label="🚀 **Ir al inicio**")

    # =================================================
    # ICON PARAMETER
    # =================================================

    st.subheader("Parámetro icon")

    with st.expander("Ejemplos de iconos"):

        with st.echo():

            # Emoji
            st.page_link(
                home_path,
                label="Alertas",
                icon="🚨"
            )

            # Material icon
            st.page_link(
                home_path,
                label="Configuración",
                icon=":material/settings:"
            )

            # Spinner
            st.page_link(
                home_path,
                label="Cargando",
                icon="spinner"
            )

    # =================================================
    # ICON_POSITION PARAMETER
    # =================================================

    st.subheader("Parámetro icon_position")

    with st.expander("Posición del icono"):

        with st.echo():

            # Izquierda (default)
            st.page_link(
                home_path,
                label="Guardar",
                icon=":material/save:",
                icon_position="left"
            )

            # Derecha
            st.page_link(
                home_path,
                label="Guardar",
                icon=":material/save:",
                icon_position="right"
            )

    # =================================================
    # HELP PARAMETER
    # =================================================

    st.subheader("Parámetro help")

    with st.expander("Ejemplo con tooltip"):

        with st.echo():

            st.page_link(
                home_path,
                label="Ayuda",
                help="Ir a la página de ayuda"
            )

    # =================================================
    # DISABLED PARAMETER
    # =================================================

    st.subheader("Parámetro disabled")

    with st.expander("Ejemplo deshabilitado"):

        with st.echo():

            st.page_link(
                home_path,
                label="Disponible",
                disabled=False
            )

            st.page_link(
                home_path,
                label="No disponible",
                disabled=True
            )

    # =================================================
    # WIDTH PARAMETER
    # =================================================

    st.subheader("Parámetro width")

    with st.expander("Ejemplos de ancho"):

        with st.echo():

            # Ancho automático
            st.page_link(
                home_path,
                label="Ancho contenido",
                width="content"
            )

            # Ancho completo
            st.page_link(
                home_path,
                label="Ancho completo",
                width="stretch"
            )

            # Ancho fijo
            st.page_link(
                home_path,
                label="Ancho 300px",
                width=300
            )

    # =================================================
    # QUERY_PARAMS PARAMETER
    # =================================================

    st.subheader("Parámetro query_params")
    
    st.markdown(""" Informacion importante sobre query params se le puede enviar listas,diccionarios, str
            En Streamlit se usan mucho para:

-  ✅ Filtros
-  ✅ Estados (selecciones del usuario)
-  ✅ Navegación dinámica
-  ✅ Compartir links con configuración guardada
    """)

    with st.expander("Ejemplos con parámetros de consulta"):

        with st.echo():

            # Diccionario
            st.page_link(
                dash_path,
                label="Dashboard con filtros",
                query_params={
                    "year": "2024",
                    "region": "sur"
                }
            )

            # Lista de tuplas
            st.page_link(
                dash_path,
                label="Con parámetros repetidos",
                query_params=[
                    ("tag", "ventas"),
                    ("tag", "costos")
                ]
            )

# =========================
# SELECTIONS
# =========================
def selection_example():

    # -------------------------------------------------
    # st.checkbox
    # -------------------------------------------------
    st.checkbox("Checkbox")
    st.multiselect("multiselect",options=["Manzana", "Banana", "Cereza"])
    st.selectbox("Selectbox",options=["Argentina", "Brasil", "Chile"])
    st.pills("Pills",options=["Efectivo", "Tarjeta", "Transferencia"])
    st.radio("Radio",options=["Masculino", "Femenino", "Otro"])
    st.color_picker("color_picker", value="#FF0000")
    st.feedback("thumbs")
    st.segmented_control("segmented_control",options=["Pequeño", "Mediano", "Grande"])
    st.select_slider("select_slider",options=list(range(18, 66)))
    st.toggle("Activar notificaciones")

def checkbox():

    # -------------------------------------------------
    # Function signature
    # -------------------------------------------------

    st.code(
        'st.checkbox(label, value=False, key=None, help=None, on_change=None, '
        'args=None, kwargs=None, *, disabled=False, '
        'label_visibility="visible", width="content")'
    )

    # =================================================
    # LABEL PARAMETER
    # =================================================

    st.subheader("Parámetro label")

    with st.expander("Ejemplos del parámetro label"):

        with st.echo():

            # Texto simple
            st.checkbox("Aceptar términos")

            # Markdown básico
            st.checkbox("**Acepto condiciones**")
            st.checkbox("*Recordarme*")
            st.checkbox("~~Eliminar cuenta~~")
            st.checkbox("`Modo debug`")

            # Emoji
            st.checkbox("📩 Recibir notificaciones")

            # Link como label
            st.checkbox("[Ver política de privacidad](https://streamlit.io)")

            # Markdown no soportado
            st.markdown("❌ Markdown complejo:")
            st.checkbox("1. Opción uno")

            # Escapado
            st.markdown("✅ Escapado:")
            st.checkbox("1\\. Opción uno")

            # Recomendado
            st.checkbox("✅ **Confirmar acción**")


    # =================================================
    # VALUE PARAMETER
    # =================================================

    st.subheader("Parámetro value")

    with st.expander("Checkbox preseleccionado"):

        with st.echo():

            # No marcado (default)
            st.checkbox("Opción apagada")

            # Marcado por defecto
            st.checkbox("Opción encendida", value=True)


    # =================================================
    # KEY PARAMETER
    # =================================================

    st.subheader("Parámetro key")

    with st.expander("Uso de key único"):

        with st.echo():

            st.checkbox("Filtro A", key="filtro_a")
            st.checkbox("Filtro B", key="filtro_b")


    # =================================================
    # HELP PARAMETER
    # =================================================

    st.subheader("Parámetro help")

    with st.expander("Tooltip informativo"):

        with st.echo():

            st.checkbox(
                "Habilitar modo experto",
                help="Activa opciones avanzadas del sistema"
            )


    # =================================================
    # ON_CHANGE PARAMETER
    # =================================================

    st.subheader("Parámetro on_change")

    with st.expander("Callback cuando cambia el valor"):

        with st.echo():

            def aviso():
                st.session_state["msg"] = "Checkbox cambiado!"

            st.checkbox(
                "Activar alerta",
                on_change=aviso
            )

            if "msg" in st.session_state:
                st.success(st.session_state["msg"])


    # =================================================
    # ARGS & KWARGS PARAMETER
    # =================================================

    st.subheader("Parámetros args y kwargs")

    with st.expander("Pasar datos al callback"):

        with st.echo():

            def mostrar(valor, tipo=None):
                st.write("Valor:", valor)
                st.write("Tipo:", tipo)

            st.checkbox(
                "Enviar datos",
                on_change=mostrar,
                args=(True,),
                kwargs={"tipo": "checkbox"}
            )


    # =================================================
    # DISABLED PARAMETER
    # =================================================

    st.subheader("Parámetro disabled")

    with st.expander("Checkbox deshabilitado"):

        with st.echo():

            st.checkbox("Activo")

            st.checkbox(
                "Deshabilitado",
                disabled=True
            )


    # =================================================
    # LABEL_VISIBILITY PARAMETER
    # =================================================

    st.subheader("Parámetro label_visibility")

    with st.expander("Control de visibilidad del label"):

        with st.echo():

            # Visible (default)
            st.checkbox(
                "Visible",
                label_visibility="visible"
            )

            # Oculto pero mantiene espacio
            st.checkbox(
                "Hidden",
                label_visibility="hidden"
            )

            # Totalmente colapsado
            st.checkbox(
                "Collapsed",
                label_visibility="collapsed"
            )


    # =================================================
    # WIDTH PARAMETER
    # =================================================

    st.subheader("Parámetro width")

    with st.expander("Control de ancho"):

        with st.echo():

            # Ajustado al contenido
            st.checkbox(
                "Ancho contenido",
                width="content"
            )

            # Ancho completo
            st.checkbox(
                "Ancho stretch",
                width="stretch"
            )

            # Ancho fijo
            st.checkbox(
                "Ancho 300px",
                width=300
            )


    # =================================================
    # CASOS DE USO REALES
    # =================================================

    st.subheader("Casos de uso comunes")

    with st.expander("Ejemplos prácticos"):

        with st.echo():

            # Filtro
            mostrar_activos = st.checkbox("Mostrar solo activos")

            if mostrar_activos:
                st.write("Mostrando registros activos")

            # Aceptar términos
            aceptado = st.checkbox("Acepto los términos y condiciones")

            if aceptado:
                st.success("Puedes continuar")

            # Configuración
            modo_oscuro = st.checkbox("🌙 Modo oscuro")

            if modo_oscuro:
                st.write("Modo oscuro activado")


    # =================================================
    # RETURN VALUE
    # =================================================

    st.info("""
    📌 st.checkbox() devuelve un booleano:

    ✅ True  → si está marcado  
    ❌ False → si no está marcado  

    👉 Ideal para filtros, configuraciones y validaciones
    """)

def color_picker():
    st.code('st.color_picker(label, value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", width="content")')
    
    with st.expander('Parametro Label'):
        with st.echo():
            color=st.color_picker('Label')
            st.text(color)
    st.info('El resto de los parametros son  iguales a la anterior funcion revisar ahi')
          
def feedback():

    # -------------------------------------------------
    # Function signature
    # -------------------------------------------------

    st.code(
        'st.feedback(options="thumbs", *, key=None, default=None, disabled=False, '
        'on_change=None, args=None, kwargs=None, width="content")'
    )

    # =================================================
    # THUMBS OPTION
    # =================================================

    st.subheader("👍 Opciones: thumbs (default)")

    with st.expander("Ejemplo thumbs y su estado"):

        with st.echo():

            thumbs_value = st.feedback("thumbs", key="thumbs_main")

            st.write("Estado devuelto:", thumbs_value)

            if thumbs_value == 1:
                st.success("Usuario dio 👍 positivo")
            elif thumbs_value == 0:
                st.error("Usuario dio 👎 negativo")
            else:
                st.info("Aún sin respuesta")


    # =================================================
    # FACES OPTION
    # =================================================

    st.subheader("🙂 Opciones: faces")

    with st.expander("Ejemplo faces y su estado"):

        with st.echo():

            faces_value = st.feedback("faces", key="faces_main")

            st.write("Estado devuelto:", faces_value)

            if faces_value is not None:
                st.write(f"Nivel de satisfacción: {faces_value + 1} de 5")
            else:
                st.info("Aún sin respuesta")


    # =================================================
    # STARS OPTION
    # =================================================

    st.subheader("⭐ Opciones: stars")

    with st.expander("Ejemplo stars y su estado"):

        with st.echo():

            stars_value = st.feedback("stars", key="stars_main")

            st.write("Estado devuelto:", stars_value)

            if stars_value is not None:
                st.write(f"Rating: {stars_value + 1} estrellas")
            else:
                st.info("Aún sin respuesta")


    # =================================================
    # DISABLED STATE
    # =================================================

    st.subheader("Estado disabled")

    with st.expander("Feedback deshabilitado"):

        with st.echo():

            st.feedback("thumbs", disabled=True, key="thumbs_disabled")
            st.feedback("faces", disabled=True, key="faces_disabled")
            st.feedback("stars", disabled=True, key="stars_disabled")


    # =================================================
    # DEFAULT VALUE
    # =================================================

    st.subheader("Valor por defecto (default)")

    with st.expander("Feedback precargado"):

        with st.echo():

            st.feedback("thumbs", default=1, key="thumbs_default")
            st.feedback("faces", default=2, key="faces_default")
            st.feedback("stars", default=4, key="stars_default")


    # =================================================
    # IMPORTANT NOTES
    # =================================================

    st.info("""
    📌 Valores que devuelve st.feedback():

    👍 thumbs:
        None → sin elegir
        1 → positivo
        0 → negativo

    🙂 faces:
        None → sin elegir
        0 → muy mal
        1 → mal
        2 → neutro
        3 → bien
        4 → excelente

    ⭐ stars:
        None → sin elegir
        0 → 1 estrella
        1 → 2 estrellas
        2 → 3 estrellas
        3 → 4 estrellas
        4 → 5 estrellas

    👉 Siempre devuelve índices (empieza en 0)

    ⚠ Cada feedback necesita un key único si se repite en la app
    """)

def multiselect():

    # -------------------------------------------------
    # Function signature
    # -------------------------------------------------

    st.code(
        'st.multiselect(label, options, default=None, format_func=None, key=None, help=None, '
        'on_change=None, args=None, kwargs=None, *, max_selections=None, placeholder=None, '
        'disabled=False, label_visibility="visible", accept_new_options=False, width="stretch")'
    )

    # =================================================
    # LABEL PARAMETER
    # =================================================

    st.subheader("Parámetro label")

    with st.expander("Ejemplos de label"):

        with st.echo():

            st.multiselect("Seleccioná frutas", ["Manzana", "Banana", "Naranja"])
            st.multiselect("**Elegí colores**", ["Rojo", "Azul", "Verde"])
            st.multiselect("`Tags`", ["Python", "SQL", "Power BI"])
            st.multiselect("🛒 Productos", ["Pan", "Leche", "Huevos"])


    # =================================================
    # OPTIONS PARAMETER (ITERABLES)
    # =================================================

    st.subheader("Parámetro options (Iterable)")

    with st.expander("Lista (list)"):

        with st.echo():

            opciones_lista = ["Argentina", "Brasil", "Chile"]

            st.multiselect(
                "Países (lista)",
                opciones_lista
            )

    with st.expander("Set"):

        with st.echo():

            opciones_set = {"Python", "Java", "C++", "SQL"}

            st.multiselect(
                "Lenguajes (set)",
                opciones_set
            )

    with st.expander("Tupla (tuple)"):

        with st.echo():

            opciones_tupla = ("Enero", "Febrero", "Marzo")

            st.multiselect(
                "Meses (tupla)",
                opciones_tupla
            )

    with st.expander("DataFrame"):

        with st.echo():

  

            df = pd.DataFrame({
                "Ciudades": ["Buenos Aires", "Córdoba", "Rosario"]
            })

            st.multiselect(
                "Ciudades (DataFrame)",
                df
            )


    # =================================================
    # DEFAULT PARAMETER
    # =================================================

    st.subheader("Parámetro default")

    with st.expander("Valores preseleccionados"):

        with st.echo():

            st.multiselect(
                "Frutas favoritas",
                ["Manzana", "Banana", "Naranja"],
                default=["Banana", "Naranja"]
            )


    # =================================================
    # FORMAT_FUNC PARAMETER
    # =================================================

    st.subheader("Parámetro format_func")

    with st.expander("Formatear visualización de opciones"):

        with st.echo():

            numeros = [1, 2, 3, 4]

            st.multiselect(
                "Números con formato",
                numeros,
                format_func=lambda x: f"Opción #{x}"
            )


    # =================================================
    # HELP PARAMETER
    # =================================================

    st.subheader("Parámetro help")

    with st.expander("Tooltip de ayuda"):

        with st.echo():

            st.multiselect(
                "Seleccioná hobbies",
                ["Leer", "Deporte", "Música"],
                help="Podés elegir más de una opción"
            )


    # =================================================
    # ON_CHANGE PARAMETER
    # =================================================

    st.subheader("Parámetro on_change")

    with st.expander("Callback al cambiar selección"):

        with st.echo():

            def aviso():
                st.write("Selección cambiada!")

            st.multiselect(
                "Elegí categorías",
                ["A", "B", "C"],
                on_change=aviso,
                key="multiselect_callback"
            )


    # =================================================
    # MAX_SELECTIONS PARAMETER
    # =================================================

    st.subheader("Parámetro max_selections")

    with st.expander("Limitar cantidad máxima"):

        with st.echo():

            st.multiselect(
                "Elegí hasta 2 sabores",
                ["Chocolate", "Vainilla", "Frutilla"],
                max_selections=2
            )


    # =================================================
    # PLACEHOLDER PARAMETER
    # =================================================

    st.subheader("Parámetro placeholder")

    with st.expander("Texto cuando no hay selección"):

        with st.echo():

            st.multiselect(
                "Elegí opciones",
                ["Uno", "Dos", "Tres"],
                placeholder="Seleccioná una o más opciones..."
            )


    # =================================================
    # DISABLED PARAMETER
    # =================================================

    st.subheader("Parámetro disabled")

    with st.expander("Multiselect deshabilitado"):

        with st.echo():

            st.multiselect(
                "Activo",
                ["A", "B", "C"]
            )

            st.multiselect(
                "Deshabilitado",
                ["A", "B", "C"],
                disabled=True
            )


    # =================================================
    # LABEL_VISIBILITY PARAMETER
    # =================================================

    st.subheader("Parámetro label_visibility")

    with st.expander("Visible, hidden y collapsed"):

        with st.echo():

            st.multiselect(
                "Visible",
                ["X", "Y"],
                label_visibility="visible"
            )

            st.multiselect(
                "Hidden",
                ["X", "Y"],
                label_visibility="hidden"
            )

            st.multiselect(
                "Collapsed",
                ["X", "Y"],
                label_visibility="collapsed"
            )


    # =================================================
    # ACCEPT_NEW_OPTIONS PARAMETER
    # =================================================

    st.subheader("Parámetro accept_new_options")

    with st.expander("Permitir agregar nuevas opciones"):

        with st.echo():

            st.multiselect(
                "Etiquetas",
                ["Bug", "Feature", "Mejora"],
                accept_new_options=True,
                placeholder="Escribí una nueva etiqueta"
            )




    # =================================================
    # IMPORTANT NOTES
    # =================================================

    st.info("""
    📌 Notas importantes sobre st.multiselect():

    • options acepta cualquier Iterable:
        - list
        - set
        - tuple
        - DataFrame (usa la primera columna)

    • Devuelve una lista con las selecciones

    • default debe ser una lista de valores existentes

    • max_selections limita la cantidad de elecciones

    • accept_new_options permite crear nuevas opciones dinámicamente

    ⚠ Si repetís multiselects similares, usá key único
    """)

def pills():

    # -------------------------------------------------
    # Function signature
    # -------------------------------------------------

    st.code(
        'st.pills(label, options, *, selection_mode="single", default=None, '
        'format_func=None, key=None, help=None, on_change=None, args=None, '
        'kwargs=None, disabled=False, label_visibility="visible", width="content")'
    )

    # =================================================
    # LABEL
    # =================================================

    st.subheader("Parámetro label")

    with st.expander("Formato de label con Markdown"):

        with st.echo():

            st.pills(
                "**Seleccioná categoría** 🚀",
                ["A", "B", "C"]
            )


    # =================================================
    # OPTIONS (LIST)
    # =================================================

    st.subheader("Options como lista")

    with st.expander("Iterable tipo list"):

        with st.echo():

            opciones = ["Python", "SQL", "Power BI", "Excel"]

            valor = st.pills("Tecnologías", opciones)

            st.write("Seleccionado:", valor)


    # =================================================
    # OPTIONS (SET)
    # =================================================

    st.subheader("Options como set")

    with st.expander("Iterable tipo set"):

        with st.echo():

            opciones = {"Rojo", "Verde", "Azul"}

            st.write(
                st.pills("Colores", opciones)
            )


    # =================================================
    # OPTIONS (DATAFRAME)
    # =================================================

    st.subheader("Options desde DataFrame")

    with st.expander("Iterable tipo DataFrame (primera columna)"):

        with st.echo():

            df = pd.DataFrame({
                "Lenguajes": ["Python", "R", "Julia"]
            })

            st.write(
                st.pills("Lenguajes", df)
            )


    # =================================================
    # SELECTION MODE
    # =================================================

    st.subheader("selection_mode")

    with st.expander("Single (default)"):

        with st.echo():

            st.write(
                st.pills(
                    "Una sola opción",
                    ["A", "B", "C"],
                    selection_mode="single"
                )
            )

    with st.expander("Multi"):

        with st.echo():

            st.write(
                st.pills(
                    "Varias opciones",
                    ["A", "B", "C"],
                    selection_mode="multi"
                )
            )


    # =================================================
    # DEFAULT
    # =================================================

    st.subheader("default")

    with st.expander("Valor inicial"):

        with st.echo():

            st.pills(
                "Default single",
                ["Uno", "Dos", "Tres"],
                default="Dos"
            )

            st.pills(
                "Default multi",
                ["Uno", "Dos", "Tres"],
                selection_mode="multi",
                default=["Uno", "Tres"]
            )


    # =================================================
    # FORMAT_FUNC
    # =================================================

    st.subheader("format_func")

    with st.expander("Modificar cómo se muestran las opciones"):

        with st.echo():

            niveles = [1, 2, 3]

            def formato(n):
                return f"Nivel {n} ⭐"

            st.write(
                st.pills(
                    "Prioridad",
                    niveles,
                    format_func=formato
                )
            )


    # =================================================
    # KEY
    # =================================================

    st.subheader("key")

    with st.expander("Clave única del widget"):

        with st.echo():

            st.pills(
                "Con key",
                ["A", "B"],
                key="pills_unicas"
            )


    # =================================================
    # HELP
    # =================================================

    st.subheader("help")

    with st.expander("Tooltip informativo"):

        with st.echo():

            st.pills(
                "Estado del proyecto",
                ["Activo", "Pausado", "Finalizado"],
                help="Elegí el estado actual"
            )


    # =================================================
    # ON_CHANGE
    # =================================================

    st.subheader("on_change")

    with st.expander("Callback al cambiar selección"):

        with st.echo():

            def aviso():
                st.toast("¡Cambió la selección!")

            st.pills(
                "Cambios",
                ["X", "Y", "Z"],
                on_change=aviso,
                key="callback_pills"
            )


    # =================================================
    # DISABLED
    # =================================================

    st.subheader("disabled")

    with st.expander("Widget deshabilitado"):

        with st.echo():

            st.pills(
                "Bloqueado",
                ["A", "B", "C"],
                disabled=True
            )


    # =================================================
    # LABEL VISIBILITY
    # =================================================

    st.subheader("label_visibility")

    with st.expander("hidden"):

        with st.echo():

            st.pills(
                "Etiqueta oculta",
                ["Uno", "Dos"],
                label_visibility="hidden"
            )

    with st.expander("collapsed"):

        with st.echo():

            st.pills(
                "Etiqueta colapsada",
                ["Uno", "Dos"],
                label_visibility="collapsed"
            )


    # =================================================
    # WIDTH
    # =================================================

    st.subheader("width")

    with st.expander("stretch"):

        with st.echo():

            st.pills(
                "Ancho completo",
                ["A", "B", "C"],
                width="stretch"
            )

    with st.expander("pixeles"):

        with st.echo():

            st.pills(
                "Ancho fijo",
                ["A", "B", "C"],
                width=300
            )


    # =================================================
    # NOTAS IMPORTANTES
    # =================================================

    st.info("""
    📌 Retorno de st.pills():

    selection_mode="single":
        → valor seleccionado o None

    selection_mode="multi":
        → lista de valores seleccionados (o lista vacía)

    📌 format_func solo cambia visualización (no el valor real)

    📌 options admite:
        - list
        - set
        - DataFrame (primera columna)
    """)

def radio():


    st.code(
        'st.radio(label, options, index=0, format_func=special_internal_function, '
        'key=None, help=None, on_change=None, args=None, kwargs=None, *, '
        'disabled=False, horizontal=False, label_visibility="visible", width="content")'
    )

    # =================================================
    # LABEL
    # =================================================

    st.subheader("Parámetro label")

    with st.expander("Formato del label con Markdown"):

        with st.echo():

            st.radio(
                "**Seleccioná una opción** 📌",
                ["Opción A", "Opción B", "Opción C"]
            )


    # =================================================
    # OPTIONS (LIST)
    # =================================================

    st.subheader("Options como lista")

    with st.expander("Iterable tipo list"):

        with st.echo():

            opciones = ["Python", "SQL", "Power BI"]

            valor = st.radio("Tecnologías", opciones)

            st.write("Seleccionado:", valor)


    # =================================================
    # OPTIONS (SET)
    # =================================================

    st.subheader("Options como set")

    with st.expander("Iterable tipo set"):

        with st.echo():

            colores = {"Rojo", "Verde", "Azul"}

            st.write(
                st.radio("Colores", colores)
            )


    # =================================================
    # OPTIONS (DATAFRAME)
    # =================================================

    st.subheader("Options desde DataFrame")

    with st.expander("Iterable tipo DataFrame (primera columna)"):

        with st.echo():

            df = pd.DataFrame({
                "Opciones": ["Alta", "Media", "Baja"]
            })

            st.write(
                st.radio("Prioridad", df)
            )


    # =================================================
    # INDEX (DEFAULT SELECTION)
    # =================================================

    st.subheader("index")

    with st.expander("Selección por defecto"):

        with st.echo():

            st.radio(
                "Con default en índice 1",
                ["Uno", "Dos", "Tres"],
                index=1
            )

            st.radio(
                "Sin selección inicial",
                ["Uno", "Dos", "Tres"],
                index=None
            )


    # =================================================
    # FORMAT_FUNC
    # =================================================

    st.subheader("format_func")

    with st.expander("Modificar visualización de opciones"):

        with st.echo():

            niveles = [1, 2, 3]

            def formato(n):
                return f"Nivel {n} ⭐"

            st.write(
                st.radio(
                    "Dificultad",
                    niveles,
                    format_func=formato
                )
            )


    # =================================================
    # KEY
    # =================================================

    st.subheader("key")

    with st.expander("Clave única"):

        with st.echo():

            st.radio(
                "Con key",
                ["A", "B"],
                key="radio_unica"
            )


    # =================================================
    # HELP
    # =================================================

    st.subheader("help")

    with st.expander("Tooltip"):

        with st.echo():

            st.radio(
                "Estado",
                ["Activo", "Pausado", "Finalizado"],
                help="Estado actual del proceso"
            )


    # =================================================
    # ON_CHANGE
    # =================================================

    st.subheader("on_change")

    with st.expander("Callback"):

        with st.echo():

            def aviso():
                st.toast("Cambiaste la selección")

            st.radio(
                "Cambios",
                ["X", "Y", "Z"],
                on_change=aviso,
                key="radio_callback"
            )


    # =================================================
    # DISABLED
    # =================================================

    st.subheader("disabled")

    with st.expander("Radio deshabilitado"):

        with st.echo():

            st.radio(
                "Bloqueado",
                ["A", "B", "C"],
                disabled=True
            )


    # =================================================
    # HORIZONTAL
    # =================================================

    st.subheader("horizontal")

    with st.expander("Mostrar en fila"):

        with st.echo():

            st.radio(
                "En horizontal",
                ["Izquierda", "Centro", "Derecha"],
                horizontal=True
            )


    # =================================================
    # LABEL VISIBILITY
    # =================================================

    st.subheader("label_visibility")

    with st.expander("hidden"):

        with st.echo():

            st.radio(
                "Etiqueta oculta",
                ["Uno", "Dos"],
                label_visibility="hidden"
            )

    with st.expander("collapsed"):

        with st.echo():

            st.radio(
                "Etiqueta colapsada",
                ["Uno", "Dos"],
                label_visibility="collapsed"
            )


    # =================================================
    # WIDTH
    # =================================================

    st.subheader("width")

    with st.expander("stretch"):

        with st.echo():

            st.radio(
                "Ancho completo",
                ["A", "B", "C"],
                width="stretch"
            )

    with st.expander("pixeles"):

        with st.echo():

            st.radio(
                "Ancho fijo",
                ["A", "B", "C"],
                width=280
            )


    # =================================================
    # NOTAS IMPORTANTES
    # =================================================

    st.info("""
    📌 Retorno de st.radio():

    → Devuelve la opción seleccionada (no el índice)

    📌 index:
        0,1,2... → preselecciona opción
        None → ninguna seleccionada

    📌 options admite:
        - list
        - set
        - DataFrame (primera columna)

    📌 format_func solo cambia visualización

    📌 horizontal=True es ideal para filtros rápidos
    """)

def segmented_control():
# =================================================
    # FIRMA DEL MÉTODO
    # =================================================
    st.code(
        'st.segmented_control(label, options, *, selection_mode="single", '
        'default=None, format_func=None, key=None, help=None, '
        'on_change=None, args=None, kwargs=None, '
        'disabled=False, label_visibility="visible", width="content")',
        language="python"
    )

    # =================================================
    # LABEL
    # =================================================
    st.subheader("Parámetro label")

    with st.expander("Label con Markdown"):

        with st.echo():
            st.segmented_control(
                "**Elegí una categoría** 🧩",
                ["Frontend", "Backend", "Data"]
            )

    # =================================================
    # OPTIONS
    # =================================================
    st.subheader("Parámetro options")

    with st.expander("Options como lista"):

        with st.echo():
            opciones = ["Python", "SQL", "Power BI"]

            valor = st.segmented_control(
                "Tecnologías",
                opciones
            )

            st.write("Seleccionado:", valor)

    # =================================================
    # SELECTION_MODE
    # =================================================
    st.subheader("Parámetro selection_mode")

    with st.expander("Selección simple vs múltiple"):

        with st.echo():
            seleccion = st.segmented_control(
                "Lenguajes",
                ["Python", "Java", "C++"],
                selection_mode="multi"
            )

            st.write("Seleccionados:", seleccion)

    # =================================================
    # DEFAULT
    # =================================================
    st.subheader("Parámetro default")

    with st.expander("Valor seleccionado por defecto"):

        with st.echo():
            st.segmented_control(
                "Nivel",
                ["Junior", "Semi Senior", "Senior"],
                default="Semi Senior"
            )

    # =================================================
    # FORMAT_FUNC
    # =================================================
    st.subheader("Parámetro format_func")

    with st.expander("Modificar cómo se muestran los valores"):

        with st.echo():
            opciones = [1, 2, 3]

            st.segmented_control(
                "Prioridad",
                opciones,
                format_func=lambda x: f"Nivel {x}"
            )

    # =================================================
    # KEY
    # =================================================
    st.subheader("Parámetro key")

    with st.expander("Identificador único del widget"):

        with st.echo():
            st.segmented_control(
                "Modo",
                ["Auto", "Manual"],
                key="modo_selector"
            )

            st.write("Estado:", st.session_state.modo_selector)

    # =================================================
    # HELP
    # =================================================
    st.subheader("Parámetro help")

    with st.expander("Tooltip de ayuda"):

        with st.echo():
            st.segmented_control(
                "Ambiente",
                ["Producción", "Testing"],
                help="Seleccioná el entorno de ejecución"
            )

    # =================================================
    # ON_CHANGE + ARGS / KWARGS
    # =================================================
    st.subheader("Parámetros on_change, args y kwargs")

    with st.expander("Ejecutar función al cambiar"):

        def aviso(mensaje):
            st.toast(mensaje)

        with st.echo():
            st.segmented_control(
                "Estado del sistema",
                ["Activo", "Pausado", "Detenido"],
                key="estado",
                on_change=aviso,
                args=("Estado modificado",)
            )

    # =================================================
    # DISABLED
    # =================================================
    st.subheader("Parámetro disabled")

    with st.expander("Widget deshabilitado"):

        with st.echo():
            st.segmented_control(
                "Plan",
                ["Free", "Pro", "Enterprise"],
                disabled=True
            )

    # =================================================
    # LABEL_VISIBILITY
    # =================================================
    st.subheader("Parámetro label_visibility")

    with st.expander("Ocultar el label"):

        with st.echo():
            st.segmented_control(
                "Invisible",
                ["A", "B", "C"],
                label_visibility="collapsed"
            )

    # =================================================
    # WIDTH
    # =================================================
    st.subheader("Parámetro width")

    with st.expander("Control del ancho"):

        with st.echo():
            st.segmented_control(
                "Tamaño",
                ["Chico", "Mediano", "Grande"],
                width="stretch"
            )

def selectbox():
    pass

def select_slider():
    # =================================================
    # FIRMA DEL MÉTODO
    # =================================================
    st.code(
        'st.select_slider(label, options=(), value=None, '
        'format_func=special_internal_function, key=None, help=None, '
        'on_change=None, args=None, kwargs=None, *, '
        'disabled=False, label_visibility="visible", width="stretch")',
        language="python"
    )

    # =================================================
    # LABEL
    # =================================================
    st.subheader("Parámetro label")

    with st.expander("Label con Markdown"):

        with st.echo():
            st.select_slider(
                "**Seleccioná un nivel** 🎚️",
                options=["Bajo", "Medio", "Alto"]
            )

    # =================================================
    # OPTIONS
    # =================================================
    st.subheader("Parámetro options")

    with st.expander("Options como lista ordenada"):

        with st.echo():
            niveles = ["Junior", "Semi Senior", "Senior"]

            valor = st.select_slider(
                "Nivel de experiencia",
                options=niveles
            )

            st.write("Seleccionado:", valor)

    # =================================================
    # VALUE
    # =================================================
    st.subheader("Parámetro value")

    with st.expander("Valor por defecto"):

        with st.echo():
            st.select_slider(
                "Prioridad",
                options=[1, 2, 3, 4, 5],
                value=3
            )

    # =================================================
    # FORMAT_FUNC
    # =================================================
    st.subheader("Parámetro format_func")

    with st.expander("Formato visual del valor"):

        with st.echo():
            st.select_slider(
                "Gravedad del incidente",
                options=[1, 2, 3],
                format_func=lambda x: f"Nivel {x}"
            )

    # =================================================
    # KEY
    # =================================================
    st.subheader("Parámetro key")

    with st.expander("Acceso por session_state"):

        with st.echo():
            st.select_slider(
                "Modo de ejecución",
                options=["Manual", "Automático"],
                key="modo_slider"
            )

            st.write("Estado:", st.session_state.modo_slider)

    # =================================================
    # HELP
    # =================================================
    st.subheader("Parámetro help")

    with st.expander("Tooltip de ayuda"):

        with st.echo():
            st.select_slider(
                "Entorno",
                options=["Dev", "QA", "Prod"],
                help="Elegí el entorno donde se ejecuta la app"
            )

    # =================================================
    # ON_CHANGE + ARGS / KWARGS
    # =================================================
    st.subheader("Parámetros on_change, args y kwargs")

    with st.expander("Ejecutar acción al cambiar"):

        def notificar(mensaje):
            st.toast(mensaje)

        with st.echo():
            st.select_slider(
                "Estado del proceso",
                options=["Iniciado", "En curso", "Finalizado"],
                key="estado_proceso",
                on_change=notificar,
                args=("Estado actualizado",)
            )

    # =================================================
    # DISABLED
    # =================================================
    st.subheader("Parámetro disabled")

    with st.expander("Slider deshabilitado"):

        with st.echo():
            st.select_slider(
                "Plan",
                options=["Free", "Pro", "Enterprise"],
                disabled=True
            )

    # =================================================
    # LABEL_VISIBILITY
    # =================================================
    st.subheader("Parámetro label_visibility")

    with st.expander("Ocultar label"):

        with st.echo():
            st.select_slider(
                "Invisible",
                options=["A", "B", "C"],
                label_visibility="collapsed"
            )

    # =================================================
    # WIDTH
    # =================================================
    st.subheader("Parámetro width")

    with st.expander("Control del ancho"):

        with st.echo():
            st.select_slider(
                "Tamaño",
                options=["Chico", "Mediano", "Grande"],
                width="stretch"
            )

    # =================================================
    # CASOS DE USO REALES
    # =================================================
    st.subheader("Casos de uso prácticos")

    with st.expander("1️⃣ Filtro de rango temporal"):
        with st.echo():
            año = st.select_slider(
                "Año",
                options=list(range(2018, 2026)),
                value=2023
            )
            st.write("Filtrar datos del año:", año)

    with st.expander("2️⃣ Estados de un workflow"):
        with st.echo():
            estado = st.select_slider(
                "Estado del ticket",
                options=["Nuevo", "Asignado", "Resuelto", "Cerrado"]
            )
            st.write("Estado actual:", estado)

    with st.expander("3️⃣ Nivel de riesgo / severidad"):
        with st.echo():
            riesgo = st.select_slider(
                "Riesgo",
                options=[1, 2, 3, 4, 5],
                format_func=lambda x: "🔥" * x
            )
            st.write("Riesgo:", riesgo)

    with st.expander("4️⃣ Control de calidad"):
        with st.echo():
            calidad = st.select_slider(
                "Calidad del producto",
                options=["Deficiente", "Aceptable", "Buena", "Excelente"]
            )
            st.write("Calidad:", calidad)

def toggle():
    # =================================================
    # FIRMA DEL MÉTODO
    # =================================================
    st.code(
        'st.toggle(label, value=False, key=None, help=None, '
        'on_change=None, args=None, kwargs=None, *, '
        'disabled=False, label_visibility="visible", width="content")',
        language="python"
    )

    # =================================================
    # LABEL
    # =================================================
    st.subheader("Parámetro label")

    with st.expander("Label con Markdown"):

        with st.echo():
            estado = st.toggle("**Modo oscuro** 🌙")
            st.write("Estado:", estado)

    # =================================================
    # VALUE
    # =================================================
    st.subheader("Parámetro value")

    with st.expander("Valor inicial del toggle"):

        with st.echo():
            activo = st.toggle(
                "Notificaciones",
                value=True
            )
            st.write("Activo:", activo)

    # =================================================
    # KEY
    # =================================================
    st.subheader("Parámetro key")

    with st.expander("Acceso por session_state"):

        with st.echo():
            st.toggle(
                "Autoguardado",
                key="auto_save"
            )
            st.write("Estado:", st.session_state.auto_save)

    # =================================================
    # HELP
    # =================================================
    st.subheader("Parámetro help")

    with st.expander("Tooltip de ayuda"):

        with st.echo():
            st.toggle(
                "Modo seguro",
                help="Activa validaciones extra de seguridad"
            )

    # =================================================
    # ON_CHANGE + ARGS / KWARGS
    # =================================================
    st.subheader("Parámetros on_change, args y kwargs")

    with st.expander("Ejecutar acción al cambiar"):

        def aviso(mensaje):
            st.toast(mensaje)

        with st.echo():
            st.toggle(
                "Sistema activo",
                key="sistema",
                on_change=aviso,
                args=("Estado del sistema modificado",)
            )

    # =================================================
    # DISABLED
    # =================================================
    st.subheader("Parámetro disabled")

    with st.expander("Toggle deshabilitado"):

        with st.echo():
            st.toggle(
                "Cuenta verificada",
                value=True,
                disabled=True
            )

    # =================================================
    # LABEL_VISIBILITY
    # =================================================
    st.subheader("Parámetro label_visibility")

    with st.expander("Ocultar el label"):

        with st.echo():
            st.toggle(
                "Invisible",
                label_visibility="collapsed"
            )

    # =================================================
    # WIDTH
    # =================================================
    st.subheader("Parámetro width")

    with st.expander("Control del ancho"):

        with st.echo():
            st.toggle(
                "Pantalla completa",
                width="content"
            )

    # =================================================
    # QUÉ DEVUELVE
    # =================================================
    st.subheader("¿Qué devuelve st.toggle?")

    with st.expander("Valor retornado"):

        with st.echo():
            valor = st.toggle("Activar feature X")

            st.write(valor)
            st.write(type(valor))

    # =================================================
    # CASOS DE USO REALES
    # =================================================
    st.subheader("Casos de uso prácticos")

    with st.expander("1️⃣ Activar / desactivar funcionalidades"):
        with st.echo():
            debug = st.toggle("Modo debug")

            if debug:
                st.warning("Debug activado")
            else:
                st.info("Debug desactivado")


# =========================
# NUMERIC
# =========================


def number_input():

    # =================================================
    # FIRMA DEL MÉTODO
    # =================================================
    st.code(
        'st.number_input(label, min_value=None, max_value=None, value="min", '
        'step=None, format=None, key=None, help=None, '
        'on_change=None, args=None, kwargs=None, *, '
        'placeholder=None, disabled=False, label_visibility="visible", '
        'icon=None, width="stretch")',
        language="python"
    )

    # =================================================
    # LABEL
    # =================================================
    st.subheader("Parámetro label")

    with st.expander("Label con Markdown"):
        with st.echo():
            valor = st.number_input(
                "**Cantidad de usuarios** 👥",
                key="cantidad_usuarios"
            )
            st.write("Valor:", valor)

    # =================================================
    # MIN_VALUE / MAX_VALUE
    # =================================================
    st.subheader("Parámetros min_value y max_value")

    with st.expander("Rango permitido"):
        with st.echo():
            edad = st.number_input(
                "Edad",
                min_value=0,
                max_value=120,
                key="edad"
            )
            st.write("Edad:", edad)

    # =================================================
    # VALUE
    # =================================================
    st.subheader("Parámetro value")

    with st.expander("Valor inicial"):
        with st.echo():
            stock = st.number_input(
                "Stock inicial",
                min_value=0,
                value=10,
                key="stock"
            )
            st.write("Stock:", stock)

    # =================================================
    # STEP
    # =================================================
    st.subheader("Parámetro step")

    with st.expander("Incrementos controlados"):
        with st.echo():
            porcentaje = st.number_input(
                "Descuento (%)",
                min_value=0,
                max_value=100,
                step=5,
                key="descuento"
            )
            st.write("Descuento:", porcentaje)

    # =================================================
    # FORMAT
    # =================================================
    st.subheader("Parámetro format")

    with st.expander("Formato visual del número"):
        with st.echo():
            precio = st.number_input(
                "Precio",
                min_value=0.0,
                step=0.5,
                key="precio"
            )
            st.write("Precio real:", precio)

    # =================================================
    # KEY
    # =================================================
    st.subheader("Parámetro key")

    with st.expander("Acceso por session_state"):
        with st.echo():
            st.number_input(
                "Cantidad máxima",
                key="max_qty"
            )
            st.write("Estado:", st.session_state.max_qty)

    # =================================================
    # HELP
    # =================================================
    st.subheader("Parámetro help")

    with st.expander("Tooltip de ayuda"):
        with st.echo():
            st.number_input(
                "Timeout (segundos)",
                help="Tiempo máximo de espera antes de cancelar",
                key="timeout_help"
            )

    # =================================================
    # ON_CHANGE + ARGS / KWARGS
    # =================================================
    st.subheader("Parámetros on_change, args y kwargs")

    with st.expander("Ejecutar acción al cambiar"):

        def aviso(mensaje):
            st.toast(mensaje)

        with st.echo():
            st.number_input(
                "Reintentos",
                key="reintentos",
                on_change=aviso,
                args=("Cantidad modificada",)
            )

    # =================================================
    # PLACEHOLDER
    # =================================================
    st.subheader("Parámetro placeholder")

    with st.expander("Texto guía cuando no hay valor"):
        with st.echo():
            st.number_input(
                "Código interno",
                placeholder="Ej: 1001",
                key="codigo_interno"
            )

    # =================================================
    # DISABLED
    # =================================================
    st.subheader("Parámetro disabled")

    with st.expander("Input deshabilitado"):
        with st.echo():
            st.number_input(
                "ID del sistema",
                value=999,
                disabled=True,
                key="id_sistema"
            )

    # =================================================
    # LABEL_VISIBILITY
    # =================================================
    st.subheader("Parámetro label_visibility")

    with st.expander("Ocultar label"):
        with st.echo():
            st.number_input(
                "Invisible",
                label_visibility="collapsed",
                key="invisible"
            )

    # =================================================
    # ICON
    # =================================================
    st.subheader("Parámetro icon")

    with st.expander("Icono en el input"):
        with st.echo():
            st.number_input(
                "Monto",
                icon="💰",
                key="monto"
            )

    # =================================================
    # WIDTH
    # =================================================
    st.subheader("Parámetro width")

    with st.expander("Control del ancho"):
        with st.echo():
            st.number_input(
                "Ancho completo",
                width="stretch",
                key="ancho_completo"
            )

    # =================================================
    # CASOS DE USO REALES
    # =================================================

    st.subheader("Casos de uso prácticos")

    with st.expander("1️⃣ Parámetros de negocio"):
        with st.echo():
            tasa = st.number_input(
                "Tasa de interés (%)",
                min_value=0.0,
                max_value=100.0,
                step=0.25,
                key="tasa"
            )
            st.write("Tasa:", tasa)

    with st.expander("2️⃣ Filtros numéricos"):
        with st.echo():
            min_precio = st.number_input(
                "Precio mínimo",
                min_value=0,
                key="precio_min"
            )
            st.write("Filtrar desde:", min_precio)

    with st.expander("3️⃣ Configuración técnica"):
        with st.echo():
            timeout = st.number_input(
                "Timeout",
                min_value=1,
                max_value=300,
                key="timeout"
            )
            st.write("Timeout:", timeout)

    with st.expander("4️⃣ Cálculos dinámicos"):
        with st.echo():
            cantidad = st.number_input(
                "Cantidad",
                min_value=1,
                value=1,
                key="cantidad_calc"
            )

            precio_unitario = 1200
            total = cantidad * precio_unitario

            st.success(f"Total: ${total}")

def slider():
    # =================================================
    # FIRMA DEL MÉTODO
    # =================================================
    st.code(
        'st.slider(label, min_value=None, max_value=None, value=None, '
        'step=None, format=None, key=None, help=None, '
        'on_change=None, args=None, kwargs=None, *, '
        'disabled=False, label_visibility="visible", width="stretch")',
        language="python"
    )

    # =================================================
    # LABEL
    # =================================================
    st.subheader("Parámetro label")

    with st.expander("Label con Markdown"):
        with st.echo():
            valor = st.slider(
                "**Nivel de prioridad** 🚦",
                min_value=1,
                max_value=5,
                key="prioridad"
            )
            st.write("Valor:", valor)

    # =================================================
    # MIN_VALUE / MAX_VALUE
    # =================================================
    st.subheader("Parámetros min_value y max_value")

    with st.expander("Rango permitido"):
        with st.echo():
            edad = st.slider(
                "Edad",
                min_value=0,
                max_value=120,
                key="edad_slider"
            )
            st.write("Edad:", edad)

    # =================================================
    # VALUE
    # =================================================
    st.subheader("Parámetro value")

    with st.expander("Valor inicial"):
        with st.echo():
            volumen = st.slider(
                "Volumen",
                min_value=0,
                max_value=100,
                value=30,
                key="volumen"
            )
            st.write("Volumen:", volumen)

    # =================================================
    # STEP
    # =================================================
    st.subheader("Parámetro step")

    with st.expander("Incrementos controlados"):
        with st.echo():
            descuento = st.slider(
                "Descuento (%)",
                min_value=0,
                max_value=100,
                step=5,
                key="descuento_slider"
            )
            st.write("Descuento:", descuento)

    # =================================================
    # FORMAT
    # =================================================
    st.subheader("Parámetro format")

    with st.expander("Formato visual (solo números)"):
        with st.echo():
            temperatura = st.slider(
                "Temperatura",
                min_value=-10.0,
                max_value=50.0,
                step=0.5,
                format="%.1f °C",
                key="temperatura"
            )
            st.write("Temperatura real:", temperatura)

    # =================================================
    # KEY
    # =================================================
    st.subheader("Parámetro key")

    with st.expander("Acceso por session_state"):
        with st.echo():
            st.slider(
                "Zoom",
                min_value=1,
                max_value=10,
                key="zoom"
            )
            st.write("Estado:", st.session_state.zoom)

    # =================================================
    # HELP
    # =================================================
    st.subheader("Parámetro help")

    with st.expander("Tooltip de ayuda"):
        with st.echo():
            st.slider(
                "Sensibilidad",
                min_value=1,
                max_value=10,
                help="Ajusta qué tan sensible es el sistema",
                key="sensibilidad"
            )

    # =================================================
    # ON_CHANGE + ARGS / KWARGS
    # =================================================
    st.subheader("Parámetros on_change, args y kwargs")

    with st.expander("Ejecutar acción al cambiar"):

        def aviso(mensaje):
            st.toast(mensaje)

        with st.echo():
            st.slider(
                "Reintentos",
                min_value=0,
                max_value=10,
                key="reintentos_slider",
                on_change=aviso,
                args=("Valor del slider modificado",)
            )

    # =================================================
    # DISABLED
    # =================================================
    st.subheader("Parámetro disabled")

    with st.expander("Slider deshabilitado"):
        with st.echo():
            st.slider(
                "Modo bloqueado",
                min_value=0,
                max_value=10,
                value=5,
                disabled=True,
                key="bloqueado"
            )

    # =================================================
    # LABEL_VISIBILITY
    # =================================================
    st.subheader("Parámetro label_visibility")

    with st.expander("Ocultar label"):
        with st.echo():
            st.slider(
                "Invisible",
                min_value=0,
                max_value=10,
                label_visibility="collapsed",
                key="invisible_slider"
            )

    # =================================================
    # WIDTH
    # =================================================
    st.subheader("Parámetro width")

    with st.expander("Control del ancho"):
        with st.echo():
            st.slider(
                "Ancho completo",
                min_value=0,
                max_value=100,
                width="stretch",
                key="ancho_slider"
            )

    # =================================================
    # RANGO (VALUE COMO TUPLA)
    # =================================================
    st.subheader("Slider de rango (value como tupla)")

    with st.expander("Seleccionar un rango"):
        with st.echo():
            rango = st.slider(
                "Rango de precios",
                min_value=0,
                max_value=10000,
                value=(2000, 6000),
                step=500,
                key="rango_precios"
            )
            st.write("Rango seleccionado:", rango)

    # =================================================
    # QUÉ DEVUELVE
    # =================================================
    st.subheader("¿Qué devuelve st.slider?")

    with st.expander("Tipo de dato retornado"):
        with st.echo():
            valor = st.slider(
                "Valor",
                min_value=0,
                max_value=10,
                key="tipo_valor"
            )
            st.write(valor)
            st.write(type(valor))

            rango = st.slider(
                "Rango",
                min_value=0,
                max_value=10,
                value=(3, 7),
                key="tipo_rango"
            )
            st.write(rango)
            st.write(type(rango))

    # =================================================
    # CASOS DE USO REALES
    # =================================================
    st.subheader("Casos de uso prácticos")

    with st.expander("1️⃣ Filtros por rango"):
        with st.echo():
            precio_min, precio_max = st.slider(
                "Precio",
                min_value=0,
                max_value=5000,
                value=(1000, 3000),
                key="filtro_precio"
            )
            st.write("Filtrar entre:", precio_min, "y", precio_max)

    with st.expander("2️⃣ Ajustes en tiempo real"):
        with st.echo():
            brillo = st.slider(
                "Brillo",
                min_value=0,
                max_value=100,
                key="brillo"
            )
            st.write("Brillo:", brillo)

    with st.expander("3️⃣ Parámetros de simulación"):
        with st.echo():
            velocidad = st.slider(
                "Velocidad",
                min_value=0.0,
                max_value=1.0,
                step=0.05,
                key="velocidad"
            )
            st.write("Velocidad:", velocidad)

    with st.expander("4️⃣ Configuración UX"):
        with st.echo():
            tamaño_fuente = st.slider(
                "Tamaño de fuente",
                min_value=10,
                max_value=30,
                key="fuente"
            )
            st.write("Fuente:", tamaño_fuente)

# =========================
# DATE AND TIME
# =========================


def datetime_input():

    # =================================================
    # FIRMA DEL MÉTODO
    # =================================================
    st.code(
        'st.datetime_input(label, value=None, min_value=None, max_value=None, '
        'format="YYYY-MM-DD HH:mm:ss", key=None, help=None, '
        'on_change=None, args=None, kwargs=None, *, '
        'disabled=False, label_visibility="visible", width="content")',
        language="python"
    )

    # =================================================
    # LABEL
    # =================================================
    st.subheader("Parámetro label")

    with st.expander("Label con Markdown"):
        with st.echo():
            fecha_hora = st.datetime_input("📅⏰ **Fecha y hora del evento**")
            st.write("Valor:", fecha_hora)

    # =================================================
    # VALUE
    # =================================================
    st.subheader("Parámetro value")

    with st.expander("Fecha y hora inicial"):
        with st.echo():
            ahora = st.datetime_input(
                "Ahora",
                value=datetime(2025, 11, 19, 16, 45)
            )
            st.write("Ahora:", ahora)

    # =================================================
    # MIN_VALUE / MAX_VALUE
    # =================================================
    st.subheader("Parámetros min_value y max_value")

    with st.expander("Rango permitido"):
        with st.echo():
            fecha_hora = st.datetime_input(
                "Ventana válida",
                min_value=datetime(2024, 1, 1, 0, 0),
                max_value=datetime(2026, 12, 31, 23, 59)
            )
            st.write("Seleccionado:", fecha_hora)

    # =================================================
    # FORMAT
    # =================================================
    st.subheader("Parámetro format")

    with st.expander("Formato visual personalizado"):
        with st.echo():
            fecha_hora = st.datetime_input(
                "Formato DD/MM/YYYY",
                format="DD/MM/YYYY"
            )
            st.write("Valor real:", fecha_hora)

    # =================================================
    # KEY
    # =================================================
    st.subheader("Parámetro key")

    with st.expander("Acceso por session_state"):
        with st.echo():
            st.datetime_input(
                "Fecha guardada",
                key="fecha_hora_guardada"
            )
            st.write("Estado:", st.session_state.fecha_hora_guardada)

    # =================================================
    # HELP
    # =================================================
    st.subheader("Parámetro help")

    with st.expander("Tooltip informativo"):
        with st.echo():
            st.datetime_input(
                "Inicio del proceso",
                help="Seleccioná fecha y hora de inicio"
            )

   

    # =================================================
    # CASOS DE USO REALES
    # =================================================
    st.subheader("Casos de uso prácticos")

    with st.expander("1️⃣ Programación de tareas"):
        with st.echo():
            ejecucion = st.datetime_input(
                "Ejecutar tarea en",
                value=datetime.now() + timedelta(hours=1)
            )
            st.write("Programado para:", ejecucion)

    with st.expander("2️⃣ Logs / auditoría"):
        with st.echo():
            evento = st.datetime_input(
                "Fecha del evento",
                value=datetime.now()
            )
            st.success(f"Evento registrado: {evento}")

    with st.expander("3️⃣ Ventanas de mantenimiento"):
        with st.echo():
            inicio = st.datetime_input(
                "Inicio",
                value=datetime.now()
            )
            fin = st.datetime_input(
                "Fin",
                value=datetime.now() + timedelta(hours=2)
            )

            if fin > inicio:
                duracion = fin - inicio
                st.success(f"Duración: {duracion}")
            else:
                st.error("La fecha final debe ser posterior a la inicial")

    with st.expander("4️⃣ Filtros temporales"):
        with st.echo():
            desde = st.datetime_input(
                "Desde",
                value=datetime.now() - timedelta(days=1)
            )
            hasta = st.datetime_input(
                "Hasta",
                value=datetime.now()
            )

            st.write("Filtrar entre:")
            st.write(desde, "→", hasta)



def date_input():

    # =================================================
    # FIRMA DEL MÉTODO
    # =================================================
    st.code(
        'st.date_input(label, value=None, min_value=None, max_value=None, '
        'format="YYYY-MM-DD", key=None, help=None, '
        'on_change=None, args=None, kwargs=None, *, '
        'disabled=False, label_visibility="visible", width="content")',
        language="python"
    )

    # =================================================
    # LABEL
    # =================================================
    st.subheader("Parámetro label")

    with st.expander("Label con Markdown"):

        with st.echo():
            fecha = st.date_input("📅 **Fecha del evento**")
            st.write("Fecha:", fecha)

    # =================================================
    # VALUE
    # =================================================
    st.subheader("Parámetro value")

    with st.expander("Fecha inicial por defecto"):

        with st.echo():
            fecha = st.date_input(
                "Hoy por defecto",
                value=date.today()
            )
            st.write("Fecha:", fecha)

    # =================================================
    # VALUE COMO RANGO
    # =================================================
    st.subheader("Value como rango de fechas")

    with st.expander("Selector de rango"):

        with st.echo():
            rango = st.date_input(
                "Rango de fechas",
                value=(date(2024, 1, 1), date(2024, 1, 31))
            )
            st.write("Rango:", rango)

    # =================================================
    # MIN_VALUE / MAX_VALUE
    # =================================================
    st.subheader("Parámetros min_value y max_value")

    with st.expander("Limitar fechas válidas"):

        with st.echo():
            fecha = st.date_input(
                "Fecha permitida",
                min_value=date(2020, 1, 1),
                max_value=date(2030, 12, 31)
            )
            st.write("Fecha:", fecha)

    # =================================================
    # FORMAT
    # =================================================
    st.subheader("Parámetro format")

    with st.expander("Formato visual de fecha"):

        with st.echo():
            fecha = st.date_input(
                "Formato DD/MM/YYYY",
                format="DD/MM/YYYY"
            )
            st.write("Fecha:", fecha)

    # =================================================
    # KEY
    # =================================================
    st.subheader("Parámetro key")

    with st.expander("Acceso por session_state"):

        with st.echo():
            st.date_input(
                "Fecha guardada",
                key="fecha_guardada"
            )
            st.write("Estado:", st.session_state.fecha_guardada)

    # =================================================
    # HELP
    # =================================================
    st.subheader("Parámetro help")

    with st.expander("Tooltip informativo"):

        with st.echo():
            st.date_input(
                "Inicio del proyecto",
                help="Seleccioná la fecha de comienzo"
            )

    # =================================================
    # ON_CHANGE + ARGS / KWARGS
    # =================================================
    st.subheader("Parámetros on_change, args y kwargs")

    with st.expander("Acción al cambiar fecha"):

        def aviso(mensaje):
            st.toast(mensaje)

        with st.echo():
            st.date_input(
                "Fecha crítica",
                key="fecha_critica",
                on_change=aviso,
                args=("Fecha modificada",)
            )

    # =================================================
    # DISABLED
    # =================================================
    st.subheader("Parámetro disabled")

    with st.expander("Input deshabilitado"):

        with st.echo():
            st.date_input(
                "Fecha bloqueada",
                value=date.today(),
                disabled=True
            )

    # =================================================
    # LABEL_VISIBILITY
    # =================================================
    st.subheader("Parámetro label_visibility")

    with st.expander("Ocultar label"):

        with st.echo():
            st.date_input(
                "Label oculto",
                label_visibility="collapsed"
            )

    # =================================================
    # WIDTH
    # =================================================
    st.subheader("Parámetro width")

    with st.expander("Control del ancho"):

        with st.echo():
            st.date_input(
                "Ancho completo",
                width="stretch"
            )

    # =================================================
    # CASOS DE USO REALES
    # =================================================
    st.subheader("Casos de uso prácticos")

    with st.expander("1️⃣ Fecha de nacimiento"):
        with st.echo():
            nacimiento = st.date_input(
                "Fecha de nacimiento",
                min_value=date(1900, 1, 1),
                max_value=date.today()
            )
            st.write("Nacimiento:", nacimiento)

    with st.expander("2️⃣ Filtro por rango de fechas"):
        with st.echo():
            inicio, fin = st.date_input(
                "Período",
                value=(date(2024, 1, 1), date(2024, 12, 31))
            )
            st.write("Desde:", inicio)
            st.write("Hasta:", fin)

    with st.expander("3️⃣ Configuración de sistema"):
        with st.echo():
            vencimiento = st.date_input(
                "Fecha de vencimiento",
                min_value=date.today()
            )
            st.write("Vence el:", vencimiento)

    with st.expander("4️⃣ Cálculos con fechas"):
        with st.echo():
            inicio = st.date_input("Inicio", value=date.today())
            fin = st.date_input("Fin", value=date.today())

            if fin >= inicio:
                dias = (fin - inicio).days
                st.success(f"Días entre fechas: {dias}")
            else:
                st.error("La fecha final debe ser mayor o igual a la inicial")

def time_input():
    
    # =================================================
    # FIRMA DEL MÉTODO
    # =================================================
    st.code(
        'st.time_input(label, value=None, step=None, key=None, help=None, '
        'on_change=None, args=None, kwargs=None, *, '
        'disabled=False, label_visibility="visible", width="content")',
        language="python"
    )

    # =================================================
    # LABEL
    # =================================================
    st.subheader("Parámetro label")

    with st.expander("Label con Markdown"):

        with st.echo():
            hora = st.time_input("⏰ **Hora del evento**")
            st.write("Hora:", hora)

    # =================================================
    # VALUE
    # =================================================
    st.subheader("Parámetro value")

    with st.expander("Hora inicial por defecto"):

        with st.echo():
            hora = st.time_input(
                "Hora actual",
                value=time(9, 0)
            )
            st.write("Hora:", hora)

    # =================================================
    # STEP
    # =================================================
    st.subheader("Parámetro step")

    with st.expander("Intervalos de minutos"):

        with st.echo():
            hora = st.time_input(
                "Turnos cada 15 minutos",
                step=900  # 15 min = 900 segundos
            )
            st.write("Hora:", hora)

    # =================================================
    # KEY
    # =================================================
    st.subheader("Parámetro key")

    with st.expander("Acceso por session_state"):

        with st.echo():
            st.time_input(
                "Hora guardada",
                key="hora_guardada"
            )
            st.write("Estado:", st.session_state.hora_guardada)

    # =================================================
    # HELP
    # =================================================
    st.subheader("Parámetro help")

    with st.expander("Tooltip informativo"):

        with st.echo():
            st.time_input(
                "Hora límite",
                help="Hora máxima permitida para la operación"
            )

    # =================================================
    # ON_CHANGE + ARGS / KWARGS
    # =================================================
    st.subheader("Parámetros on_change, args y kwargs")

    with st.expander("Ejecutar acción al cambiar"):

        def aviso(mensaje):
            st.toast(mensaje)

        with st.echo():
            st.time_input(
                "Hora crítica",
                key="hora_critica",
                on_change=aviso,
                args=("Hora modificada",)
            )

    # =================================================
    # DISABLED
    # =================================================
    st.subheader("Parámetro disabled")

    with st.expander("Input deshabilitado"):

        with st.echo():
            st.time_input(
                "Hora bloqueada",
                value=time(12, 0),
                disabled=True
            )

    # =================================================
    # LABEL_VISIBILITY
    # =================================================
    st.subheader("Parámetro label_visibility")

    with st.expander("Ocultar label"):

        with st.echo():
            st.time_input(
                "Label oculto",
                label_visibility="collapsed"
            )

    # =================================================
    # WIDTH
    # =================================================
    st.subheader("Parámetro width")

    with st.expander("Control del ancho"):

        with st.echo():
            st.time_input(
                "Ancho completo",
                width="stretch"
            )

    # =================================================
    # QUÉ DEVUELVE
    # =================================================
    st.subheader("¿Qué devuelve st.time_input?")

    with st.expander("Tipo de dato retornado"):

        with st.echo():
            valor = st.time_input(
                "Hora seleccionada",
                value=time(8, 30)
            )

            st.write(valor)
            st.write(type(valor))

    # =================================================
    # CASOS DE USO REALES
    # =================================================
    st.subheader("Casos de uso prácticos")

    with st.expander("1️⃣ Horarios de trabajo"):
        with st.echo():
            inicio = st.time_input("Inicio", value=time(9, 0))
            fin = st.time_input("Fin", value=time(18, 0))
            st.write("Horario:", inicio, "-", fin)

    with st.expander("2️⃣ Turnos / reservas"):
        with st.echo():
            turno = st.time_input(
                "Turno disponible",
                step=1800  # 30 minutos
            )
            st.success(f"Turno asignado: {turno}")

    with st.expander("3️⃣ Configuración del sistema"):
        with st.echo():
            mantenimiento = st.time_input(
                "Hora de mantenimiento",
                value=time(2, 0)
            )
            st.write("Mantenimiento:", mantenimiento)

    with st.expander("4️⃣ Validación de horarios"):
        with st.echo():
            apertura = st.time_input("Apertura", value=time(8, 0))
            cierre = st.time_input("Cierre", value=time(17, 0))

            if cierre > apertura:
                st.success("Horario válido")
            else:
                st.error("La hora de cierre debe ser posterior a la apertura")


# =========================
# TEXT
# =========================

def chat_input():
    st.code(
        'st.chat_input(placeholder="Your message", *, key=None, '
        'max_chars=None, max_upload_size=None, accept_file=False, '
        'file_type=None, accept_audio=False, audio_sample_rate=16000, '
        'disabled=False, on_submit=None, args=None, kwargs=None, '
        'width="stretch")',
        language="python")

    # =================================================
    # PLACEHOLDER
    # =================================================
    st.subheader("Parámetro placeholder")

    with st.expander("Texto guía en el input"):

        with st.echo():
            mensaje = st.chat_input(
                placeholder="Escribí tu mensaje acá 💬"
            )
            if mensaje:
                st.write("Mensaje:", mensaje)

    # =================================================
    # KEY
    # =================================================
    st.subheader("Parámetro key")

    with st.expander("Acceso por session_state"):

        with st.echo():
            mensaje = st.chat_input(
                "Mensaje persistente",
                key="chat_msg"
            )

            if mensaje:
                st.write("Estado:", st.session_state.chat_msg)

    # =================================================
    # MAX_CHARS
    # =================================================
    st.subheader("Parámetro max_chars")

    with st.expander("Límite de caracteres"):

        with st.echo():
            mensaje = st.chat_input(
                "Mensaje corto",
                max_chars=50
            )
            if mensaje:
                st.write(f"{len(mensaje)} caracteres:", mensaje)

    # =================================================
    # ACCEPT_FILE
    # =================================================
    st.subheader("Parámetro accept_file")

    with st.expander("Aceptar archivos en el chat"):

        with st.echo():
            mensaje = st.chat_input(
                "Mensaje con archivo",
                accept_file=True,
                file_type=["png", "jpg", "pdf"]
            )

            if mensaje:
                st.write("Texto:", mensaje.text)
                st.write("Archivo:", mensaje.files)

    # =================================================
    # MAX_UPLOAD_SIZE
    # =================================================
    st.subheader("Parámetro max_upload_size")

    with st.expander("Limitar tamaño del archivo"):

        with st.echo():
            mensaje = st.chat_input(
                "Archivo chico",
                accept_file=True,
                max_upload_size=2 * 1024 * 1024  # 2 MB
            )

            if mensaje:
                st.write("Archivo recibido")

    # =================================================
    # ACCEPT_AUDIO
    # =================================================
    st.subheader("Parámetro accept_audio")

    with st.expander("Aceptar audio"):

        with st.echo():
            mensaje = st.chat_input(
                "Mensaje de voz",
                accept_audio=True
            )

            if mensaje:
                st.write("Audio recibido")

    # =================================================
    # AUDIO_SAMPLE_RATE
    # =================================================
    st.subheader("Parámetro audio_sample_rate")

    with st.expander("Frecuencia de muestreo"):

        with st.echo():
            mensaje = st.chat_input(
                "Audio 8kHz",
                accept_audio=True,
                audio_sample_rate=8000
            )

            if mensaje:
                st.write("Audio con sample rate 8kHz")

    # =================================================
    # DISABLED
    # =================================================
    st.subheader("Parámetro disabled")

    with st.expander("Chat deshabilitado"):

        with st.echo():
            st.chat_input(
                "No disponible",
                disabled=True
            )

    # =================================================
    # ON_SUBMIT + ARGS / KWARGS
    # =================================================
    st.subheader("Parámetros on_submit, args y kwargs")

    with st.expander("Ejecutar acción al enviar"):

        def procesar(mensaje):
            st.toast(f"Mensaje enviado: {mensaje}")

        with st.echo():
            st.chat_input(
                "Enviar con acción",
                on_submit=procesar,
                args=("Mensaje enviado",)
            )

    # =================================================
    # WIDTH
    # =================================================
    st.subheader("Parámetro width")

    with st.expander("Control del ancho"):

        with st.echo():
            st.chat_input(
                "Ancho completo",
                width="stretch"
            )

    # =================================================
    # QUÉ DEVUELVE
    # =================================================
    st.subheader("¿Qué devuelve st.chat_input?")

    with st.expander("Tipo de dato retornado"):

        with st.echo():
            mensaje = st.chat_input(
                "Escribí algo"
            )

            if mensaje:
                st.write(mensaje)
                st.write(type(mensaje))

    # =================================================
    # CASOS DE USO REALES
    # =================================================
    st.subheader("Casos de uso prácticos")

    with st.expander("1️⃣ Chat básico"):
        with st.echo():
            msg = st.chat_input("Decí hola")
            if msg:
                st.chat_message("user").write(msg)
                st.chat_message("assistant").write("¡Hola! 👋")

    with st.expander("2️⃣ Chat con historial"):
        with st.echo():
            if "historial" not in st.session_state:
                st.session_state.historial = []

            msg = st.chat_input("Mensaje con historial")
            if msg:
                st.session_state.historial.append(msg)

            for m in st.session_state.historial:
                st.chat_message("user").write(m)

    with st.expander("3️⃣ Soporte / feedback"):
        with st.echo():
            feedback = st.chat_input(
                "Dejanos tu feedback",
                max_chars=200
            )
            if feedback:
                st.success("Gracias por tu mensaje 🙌")

    with st.expander("4️⃣ Input multimodal"):
        with st.echo():
            msg = st.chat_input(
                "Texto + archivo + audio",
                accept_file=True,
                accept_audio=True
            )

            if msg:
                st.write("Texto:", msg.text)
                st.write("Archivos:", msg.files)
                st.write("Audio:", msg.audio)

def text_area():
    
    # =================================================
    # TÍTULO
    # =================================================
    st.title("st.text_area usando st.echo()")
    st.divider()

    # =================================================
    # FIRMA DEL MÉTODO
    # =================================================
    st.subheader("Código del método")

    st.code(
        """st.text_area(
        label,
        value="",
        height=None,
        max_chars=None,
        key=None,
        help=None,
        on_change=None,
        args=None,
        kwargs=None,
        *,
        placeholder=None,
        disabled=False,
        label_visibility="visible",
        width="stretch"
    )""",
        language="python"
    )

    # =================================================
    # PARÁMETRO label
    # =================================================
    with st.expander("Parámetro label"):
        with st.echo():
            st.text_area("📝 Escribí un comentario")

    # =================================================
    # PARÁMETRO value
    # =================================================
    with st.expander("Parámetro value"):
        with st.echo():
            st.text_area(
                "Texto inicial",
                value="Este texto aparece al renderizar el componente"
            )

    # =================================================
    # PARÁMETRO height
    # =================================================
    with st.expander("Parámetro height"):
        with st.echo():
            st.text_area(
                "Height por defecto (3 líneas)",
                key="height_default"
            )

        with st.echo():
            st.text_area(
                "Height = 'content'",
                height="content",
                value="La altura se ajusta al contenido",
                key="height_content"
            )

        with st.echo():
            st.text_area(
                "Height fijo (150px)",
                height=150,
                value="Si el contenido supera la altura, aparece scroll",
                key="height_fixed"
            )

    # =================================================
    # PARÁMETRO max_chars
    # =================================================
    with st.expander("Parámetro max_chars"):
        with st.echo():
            st.text_area(
                "Máximo 50 caracteres",
                max_chars=50,
                placeholder="No podés escribir más de 50 caracteres"
            )

    # =================================================
    # PARÁMETRO key
    # =================================================
    with st.expander("Parámetro key"):
        with st.echo():
            texto = st.text_area(
                "Text area con key",
                key="textarea_key"
            )

        st.write("Valor actual:", texto)

    # =================================================
    # PARÁMETRO help
    # =================================================
    with st.expander("Parámetro help"):
        with st.echo():
            st.text_area(
                "Campo con ayuda",
                help="Este texto explica qué debe ingresar el usuario"
            )

    # =================================================
    # PARÁMETRO on_change
    # =================================================
    with st.expander("Parámetro on_change"):

        def mostrar_mensaje(nombre):
            st.success(f"Texto modificado por {nombre}")

        with st.echo():
            st.text_area(
                "Dispara callback al cambiar",
                on_change=mostrar_mensaje,
                args=("Pablo",),
                key="textarea_callback1"
            )

    # =================================================
    # PARÁMETRO placeholder
    # =================================================
    with st.expander("Parámetro placeholder"):
        with st.echo():
            st.text_area(
                "Campo vacío",
                placeholder="Escribí acá tu mensaje..."
            )

    # =================================================
    # PARÁMETRO width
    # =================================================
    with st.expander("Parámetro width"):
        with st.echo():
            st.text_area(
                "Width stretch (default)",
                width="stretch",
                key="width_stretch"
            )

        with st.echo():
            st.text_area(
                "Width fijo 300px",
                width=300,
                key="width_fixed"
            )

   


    # =================================================
    # CASOS DE USO
    # =================================================
    st.divider()
    st.title("📘 st.text_area — Casos de uso reales")

    # -------------------------------------------------
    # CASO 1
    # -------------------------------------------------
    with st.expander("1️⃣ Comentarios / Feedback"):
        with st.echo():
            st.text_area(
                "Dejanos tu comentario",
                placeholder="Escribí tu opinión acá..."
            )

    # -------------------------------------------------
    # CASO 2
    # -------------------------------------------------
    with st.expander("2️⃣ Formularios con texto largo"):
        with st.echo():
            st.text_area(
                "Descripción del problema",
                height=150,
                help="Explicá el problema con el mayor detalle posible"
            )

    # -------------------------------------------------
    # CASO 3
    # -------------------------------------------------
    with st.expander("3️⃣ Ingreso de código (SQL / Python)"):
        with st.echo():
            codigo = st.text_area(
                "Pegá tu código o consulta SQL",
                height=150,
                placeholder="SELECT * FROM usuarios;"
            )

            if codigo:
                st.code(codigo, language="sql")

    # -------------------------------------------------
    # CASO 4
    # -------------------------------------------------
    with st.expander("4️⃣ Edición de texto existente"):
        with st.echo():
            st.text_area(
                "Editar contenido",
                value="Este texto fue cargado desde una base de datos o archivo."
            )

    # -------------------------------------------------
    # CASO 5
    # -------------------------------------------------
    with st.expander("5️⃣ Logs / solo lectura"):
        with st.echo():
            st.text_area(
                "Logs del sistema",
                value=(
                    "Proceso iniciado...\n"
                    "Cargando datos...\n"
                    "Proceso finalizado correctamente."
                ),
                height=180,
                disabled=True
            )

    # -------------------------------------------------
    # CASO 6
    # -------------------------------------------------
    with st.expander("6️⃣ Texto con límite de caracteres"):
        with st.echo():
            st.text_area(
                "Resumen (máx. 200 caracteres)",
                max_chars=200,
                placeholder="Escribí un resumen corto..."
            )

    # -------------------------------------------------
    # CASO 7
    # -------------------------------------------------
    with st.expander("7️⃣ Callback con on_change"):
        with st.echo():
            def aviso():
                st.warning("⚠️ El texto fue modificado")

            st.text_area(
                "Texto monitoreado",
                key="textarea_callback",
                on_change=aviso
            )

    # -------------------------------------------------
    # CASO 8
    # -------------------------------------------------
    with st.expander("8️⃣ UI limpia (label oculto)"):
        with st.echo():
            st.text_area(
                "Mensaje",
                label_visibility="collapsed",
                placeholder="Escribí tu mensaje..."
            )

    # -------------------------------------------------
    # CASO 9
    # -------------------------------------------------
    with st.expander("9️⃣ Control de altura"):
        with st.echo():
            st.text_area(
                "Altura fija (120px)",
                height=120,
                value="Si el contenido supera la altura, aparece scroll."
            )

    # -------------------------------------------------
    # CASO 10
    # -------------------------------------------------
    with st.expander("🔟 Control de ancho (usando columnas)"):
        with st.echo():
            col1, col2 = st.columns([1, 2])

            with col1:
                st.text_area("Columna angosta")

            with col2:
                st.text_area("Columna ancha")

def text_input():
    st.divider()
    st.title("📘 st.text_input() — Explicación de parámetros")

    # =================================================
    # PARÁMETRO: label
    # =================================================
    with st.expander("label (obligatorio)"):
        with st.echo():
            st.text_input(
                label="Nombre de usuario"
            )

    # =================================================
    # PARÁMETRO: value
    # =================================================
    with st.expander("value (valor inicial)"):
        with st.echo():
            st.text_input(
                label="Usuario",
                value="admin"
            )

    # =================================================
    # PARÁMETRO: max_chars
    # =================================================
    with st.expander("max_chars (límite de caracteres)"):
        with st.echo():
            st.text_input(
                label="Código",
                max_chars=6,
                placeholder="ABC123"
            )

    # =================================================
    # PARÁMETRO: key
    # =================================================
    with st.expander("key (identificador único)"):
        with st.echo():
            st.text_input(
                label="Campo con key",
                key="input_unico"
            )

    # =================================================
    # PARÁMETRO: type
    # =================================================
    with st.expander('type ("default" | "password")'):
        with st.echo():
            st.text_input(
                label="Contraseña",
                type="password"
            )

    # =================================================
    # PARÁMETRO: help
    # =================================================
    with st.expander("help (texto de ayuda)"):
        with st.echo():
            st.text_input(
                label="Email",
                help="Usá un correo válido"
            )

    # =================================================
    # PARÁMETRO: autocomplete
    # =================================================
    with st.expander("autocomplete (autocompletado del navegador)"):
        with st.echo():
            st.text_input(
                label="País",
                autocomplete="country-name"
            )

    # =================================================
    # PARÁMETRO: on_change
    # =================================================
    with st.expander("on_change (callback al modificar)"):
        with st.echo():
            def aviso():
                st.warning("⚠️ El valor fue modificado")

            st.text_input(
                label="Texto monitoreado",
                key="callback_input",
                on_change=aviso
            )

    # =================================================
    # PARÁMETRO: args / kwargs
    # =================================================
    with st.expander("args / kwargs (argumentos para callback)"):
        with st.echo():
            def mostrar(valor):
                st.info(f"Valor recibido: {valor}")

            st.text_input(
                label="Campo con argumentos",
                key="input_args",
                on_change=mostrar,
                args=("Hola desde args",)
            )

    # =================================================
    # PARÁMETRO: placeholder
    # =================================================
    with st.expander("placeholder (texto de ejemplo)"):
        with st.echo():
            st.text_input(
                label="Buscar",
                placeholder="Escribí para buscar..."
            )

    # =================================================
    # PARÁMETRO: disabled
    # =================================================
    with st.expander("disabled (campo deshabilitado)"):
        with st.echo():
            st.text_input(
                label="ID",
                value="USR-001",
                disabled=True
            )

    # =================================================
    # PARÁMETRO: label_visibility
    # =================================================
    with st.expander('label_visibility ("visible" | "hidden" | "collapsed")'):
        with st.echo():
            st.text_input(
                label="Mensaje",
                label_visibility="collapsed",
                placeholder="Campo sin label visible"
            )

    # =================================================
    # PARÁMETRO: icon
    # =================================================
    with st.expander("icon (ícono decorativo)"):
        with st.echo():
            st.text_input(
                label="Buscar",
                icon="🔍",
                placeholder="Buscar..."
            )

    # =================================================
    # PARÁMETRO: width
    # =================================================
    with st.expander('width ("stretch" | número)'):
        with st.echo():
            st.text_input(
                label="Ancho automático",
                width="stretch"
            )

            st.text_input(
                label="Ancho fijo",
                width=300
            )


# =========================
# MEDIA AND FILES
# =========================

def audio_input():
    st.title("🎤 Apunte completo: st.audio_input")

# =================================================
# FIRMA DEL MÉTODO
# =================================================
    st.subheader("📌 Firma del método")

    st.code(
        'st.audio_input(label, *, sample_rate=16000, key=None, help=None, '
        'on_change=None, args=None, kwargs=None, disabled=False, '
        'label_visibility="visible", width="stretch")',
        language="python"
    )

    # =================================================
    # LABEL
    # =================================================
    with st.expander("📝 Parámetro: label"):
        with st.echo():
            st.audio_input("Grabá tu audio")

    # =================================================
    # SAMPLE_RATE
    # =================================================
    with st.expander("🎚️ Parámetro: sample_rate"):
        with st.echo():
            st.audio_input(
                "Audio con sample rate 44100",
                sample_rate=44100
            )

    # =================================================
    # KEY
    # =================================================
    with st.expander("🔑 Parámetro: key"):
        with st.echo():
            st.audio_input(
                "Audio con key",
                key="audio_unico"
            )

    # =================================================
    # HELP
    # =================================================
    with st.expander("❓ Parámetro: help"):
        with st.echo():
            st.audio_input(
                "Audio con ayuda",
                help="Presioná grabar y hablá cerca del micrófono"
            )

    # =================================================
    # ON_CHANGE
    # =================================================
    with st.expander("🔁 Parámetro: on_change"):
        with st.echo():
            def aviso_audio():
                st.success("Audio grabado correctamente 🎉")

            st.audio_input(
                "Audio con evento",
                on_change=aviso_audio
            )

    # =================================================
    # ARGS
    # =================================================
    with st.expander("📦 Parámetro: args"):
        with st.echo():
            def mostrar_nombre(nombre):
                st.info(f"Audio grabado por {nombre}")

            st.audio_input(
                "Audio con args",
                on_change=mostrar_nombre,
                args=("Pablo",)
            )

    # =================================================
    # DISABLED
    # =================================================
    with st.expander("🚫 Parámetro: disabled"):
        with st.echo():
            st.audio_input(
                "Audio deshabilitado",
                disabled=True
            )

    # =================================================
    # LABEL_VISIBILITY
    # =================================================
    with st.expander("👁️ Parámetro: label_visibility"):
        with st.echo():
            st.audio_input(
                "Audio sin label",
                label_visibility="collapsed"
            )


def camera_input():
    st.title("📸 Apunte completo: st.camera_input")

    # =================================================
    # FIRMA DEL MÉTODO
    # =================================================
    st.subheader("📌 Firma del método")

    st.code(
        'st.camera_input(label, *, key=None, help=None, '
        'on_change=None, args=None, kwargs=None, '
        'disabled=False, label_visibility="visible", width="stretch")',
        language="python"
    )

    # =================================================
    # LABEL
    # =================================================
    with st.expander("📝 Parámetro: label"):
        with st.echo():
            st.camera_input("Tomar una foto")

    # =================================================
    # KEY
    # =================================================
    with st.expander("🔑 Parámetro: key"):
        with st.echo():
            st.camera_input(
                "Foto con key",
                key="camera_unica"
            )

    # =================================================
    # HELP
    # =================================================
    with st.expander("❓ Parámetro: help"):
        with st.echo():
            st.camera_input(
                "Foto con ayuda",
                help="Asegurate de tener buena iluminación"
            )

    # =================================================
    # ON_CHANGE
    # =================================================
    with st.expander("🔁 Parámetro: on_change"):
        with st.echo():
            def aviso_foto():
                st.success("Foto capturada 📸")

            st.camera_input(
                "Foto con evento",
                on_change=aviso_foto
            )

    # =================================================
    # ARGS
    # =================================================
    with st.expander("📦 Parámetro: args"):
        with st.echo():
            def mostrar_usuario(nombre):
                st.info(f"Foto tomada por {nombre}")

            st.camera_input(
                "Foto con args",
                on_change=mostrar_usuario,
                args=("Pablo",)
            )

    # =================================================
    # DISABLED
    # =================================================
    with st.expander("🚫 Parámetro: disabled"):
        with st.echo():
            st.camera_input(
                "Cámara deshabilitada",
                disabled=True
            )

    # =================================================
    # LABEL_VISIBILITY
    # =================================================
    with st.expander("👁️ Parámetro: label_visibility"):
        with st.echo():
            st.camera_input(
                "Foto sin label",
                label_visibility="collapsed"
            )





# =========================
# FILES
# =========================

def file_uploader():
    st.title("📁 Apunte completo: st.file_uploader")

    st.code(
        'st.file_uploader(label, type=None, accept_multiple_files=False, '
        'key=None, help=None, on_change=None, args=None, kwargs=None, *, '
        'max_upload_size=None, disabled=False, '
        'label_visibility="visible", width="stretch")',
        language="python"
    )

    # =================================================
    # LABEL
    # =================================================
    with st.expander("📝 Parámetro: label"):
        with st.echo():
            st.file_uploader("Subí un archivo")

    # =================================================
    # TYPE (string)
    # =================================================
    with st.expander("🧾 Parámetro: type (string)"):
        with st.echo():
            archivo = st.file_uploader(
                "Solo archivos CSV",
                type="csv"
            )

            if archivo:
                st.success("CSV cargado correctamente")

    # =================================================
    # TYPE (lista)
    # =================================================
    with st.expander("🧾 Parámetro: type (lista de extensiones)"):
        with st.echo():
            imagen = st.file_uploader(
                "Imágenes JPG / PNG",
                type=["jpg", "jpeg", "png"]
            )

            if imagen:
                st.image(imagen)

    # =================================================
    # ACCEPT_MULTIPLE_FILES = False
    # =================================================
    with st.expander("📄 Parámetro: accept_multiple_files=False"):
        with st.echo():
            archivo = st.file_uploader(
                "Un solo archivo",
                accept_multiple_files=False
            )

            if archivo:
                st.write("Archivo:", archivo.name)

    # =================================================
    # ACCEPT_MULTIPLE_FILES = True
    # =================================================
    with st.expander("📚 Parámetro: accept_multiple_files=True"):
        with st.echo():
            archivos = st.file_uploader(
                "Múltiples archivos",
                accept_multiple_files=True
            )

            if archivos:
                for a in archivos:
                    st.write(a.name)

    # =================================================
    # ACCEPT_MULTIPLE_FILES = 'directory'
    # =================================================
    with st.expander("📂 Parámetro: accept_multiple_files='directory'"):
        with st.echo():
            carpeta = st.file_uploader(
                "Subir carpeta completa",
                accept_multiple_files="directory"
            )

            if carpeta:
                st.write("Archivos en la carpeta:")
                for a in carpeta:
                    st.write("-", a.name)

    # =================================================
    # KEY
    # =================================================
    with st.expander("🔑 Parámetro: key"):
        with st.echo():
            st.file_uploader(
                "Uploader con key",
                key="uploader_unico"
            )

    # =================================================
    # HELP
    # =================================================
    with st.expander("❓ Parámetro: help"):
        with st.echo():
            st.file_uploader(
                "Archivo con ayuda",
                help="Formatos permitidos según la consigna"
            )

    # =================================================
    # ON_CHANGE
    # =================================================
    with st.expander("🔁 Parámetro: on_change"):
        with st.echo():
            def aviso():
                st.success("Archivo subido 📥")

            st.file_uploader(
                "Uploader con evento",
                on_change=aviso
            )

    # =================================================
    # ARGS
    # =================================================
    with st.expander("📦 Parámetro: args"):
        with st.echo():
            def mostrar_usuario(nombre):
                st.info(f"Archivo subido por {nombre}")

            st.file_uploader(
                "Uploader con args",
                on_change=mostrar_usuario,
                args=("Pablo",)
            )

    # =================================================
    # KWARGS
    # =================================================
    with st.expander("🧩 Parámetro: kwargs"):
        with st.echo():
            def mostrar_info(nombre=None):
                st.warning(f"Usuario: {nombre}")

            st.file_uploader(
                "Uploader con kwargs",
                on_change=mostrar_info,
                kwargs={"nombre": "Pablo"}
            )

    # =================================================
    # MAX_UPLOAD_SIZE
    # =================================================
    with st.expander("📏 Parámetro: max_upload_size"):
        with st.echo():
            st.file_uploader(
                "Máximo 1 MB",
                max_upload_size=1
            )

    # =================================================
    # DISABLED
    # =================================================
    with st.expander("🚫 Parámetro: disabled"):
        with st.echo():
            st.file_uploader(
                "Uploader deshabilitado",
                disabled=True
            )

    # =================================================
    # LABEL_VISIBILITY
    # =================================================
    with st.expander("👁️ Parámetro: label_visibility"):
        with st.echo():
            st.file_uploader(
                "Uploader sin label",
                label_visibility="collapsed"
            )

    # =================================================
    # WIDTH
    # =================================================
    with st.expander("📐 Parámetro: width"):
        with st.echo():
            st.file_uploader(
                "Uploader ancho fijo (300px)",
                width=300
            )

    # =================================================
    # VALOR DEVUELTO
    # =================================================
    with st.expander("📦 Valor devuelto (UploadedFile)"):
        with st.echo():
            archivo = st.file_uploader("Inspeccionar archivo")

            if archivo:
                st.write("Nombre:", archivo.name)
                st.write("Tipo MIME:", archivo.type)
                st.write("Tamaño (bytes):", archivo.size)

    # =================================================
    # CASOS DE USO
    # =================================================
    st.subheader("🧠 Casos de uso comunes")

    # -------------------------------------------------
    # Caso 1: Leer CSV
    # -------------------------------------------------
    with st.expander("📊 Caso de uso: Cargar y leer un CSV"):
        with st.echo():
            import pandas as pd

            csv = st.file_uploader("Subí un CSV", type="csv")

            if csv:
                df = pd.read_csv(csv)
                st.dataframe(df)

    # -------------------------------------------------
    # Caso 2: Subir imágenes
    # -------------------------------------------------
    with st.expander("🖼️ Caso de uso: Subir imágenes"):
        with st.echo():
            imagen = st.file_uploader(
                "Imagen",
                type=["jpg", "jpeg", "png"]
            )

            if imagen:
                st.image(imagen)

    # -------------------------------------------------
    # Caso 3: Subir varios archivos
    # -------------------------------------------------
    with st.expander("📚 Caso de uso: Subir múltiples archivos"):
        with st.echo():
            archivos = st.file_uploader(
                "Varios archivos",
                accept_multiple_files=True
            )

            if archivos:
                st.write("Cantidad:", len(archivos))

    # -------------------------------------------------
    # Caso 4: Validar tamaño
    # -------------------------------------------------
    with st.expander("⚠️ Caso de uso: Limitar tamaño"):
        with st.echo():
            archivo = st.file_uploader(
                "Máx 2 MB",
                max_upload_size=2
            )

            if archivo:
                st.success("Archivo aceptado")

    # -------------------------------------------------
    # Caso 5: Desactivar según lógica
    # -------------------------------------------------
    with st.expander("🔒 Caso de uso: Desactivar uploader"):
        with st.echo():
            habilitar = st.checkbox("Habilitar carga")

            st.file_uploader(
                "Uploader controlado",
                disabled=not habilitar
            )

