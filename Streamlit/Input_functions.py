import streamlit as st
import pandas as pd
from pathlib import Path


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
    pass

def selectbox():
    pass

def select_slider():
    pass

def toggle():
    pass


# =========================
# NUMERIC
# =========================

def number_input():
    pass

def slider():
    pass


# =========================
# DATE AND TIME
# =========================

def date_input():
    pass

def datetime_input():
    pass

def time_input():
    pass


# =========================
# TEXT
# =========================

def chat_input():
    pass

def link():
    pass

def text_area():
    pass

def text_input():
    pass


# =========================
# MEDIA AND FILES
# =========================

def audio_input():
    pass

def camera_input():
    pass

def data_editor():
    pass


# =========================
# FILES
# =========================

def file_uploader():
    pass

