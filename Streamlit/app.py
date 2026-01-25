import streamlit as st
import Header_and_body as hb
import Formated_text as ft
import data_elements as de
import Input_functions as inp


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Apunte Streamlit",
    layout="wide"
)


# =========================
# SIDEBAR
# =========================

tematicas = (
    "Headings and body",
    "Formated Text",
    "Data Elements",
    "Input Elements",
)

sidebar = st.sidebar.radio("Barra lateral", tematicas)


# =========================
# TITLE
# =========================

st.title("APUNTE DE STREAMLIT")
st.divider()


# =========================
# MAIN ROUTER
# =========================

match sidebar:

    # -------------------------------------------------
    case "Headings and body":

        st.header("Headings and body")

        hb.header_body()

        with st.expander("Title"):
            hb.title()

        with st.expander("Headers"):
            hb.headers()

        with st.expander("Subheader"):
            hb.subheader()

        hb.observaciones_formato()

        with st.expander("Markdown"):
            hb.markdown()


    # -------------------------------------------------
    case "Formated Text":

        st.header("Formated Text")

        for label, func in [
            ("Badge", ft.badge),
            ("Caption", ft.caption),
            ("Code", ft.code),
            ("Divider", ft.divider),
            ("Echo", ft.echo),
            ("LaTeX", ft.latex),
            ("Text", ft.text),
            ("Help", ft.pagina_help),
            ("HTML", ft.html),
        ]:
            with st.expander(label):
                func()


    # -------------------------------------------------
    case "Data Elements":

        for label, func in [
            ("📊 DataFrame", de.mostrar_dataframe),
            ("✏️ Data Editor", de.editor_dataframe),
            ("⚙️ Column Config", de.configurar_columnas),
            ("📋 Table", de.mostrar_tabla),
            ("📈 Metric", de.mostrar_metrica),
            ("🧾 JSON", de.mostrar_json),
        ]:
            with st.expander(label):
                func()


    # -------------------------------------------------
    case "Input Elements":

        tab_names = [
            "🔘 Buttons",
            "🔗 Links",
            "☑️ Selections",
            "🔢 Numerics",
            "📅 Date and Time",
            "✏️ Text",
            "🎥 Media and Editors",
            "📁 Files"
        ]

        (
            buttons_tab,
            links_tab,
            selections_tab,
            numerics_tab,
            datetime_tab,
            text_tab,
            media_tab,
            files_tab
        ) = st.tabs(tab_names)


        # ---------- Helper layout ----------

        def render_section(items, columns=2):
            cols = st.columns(columns)

            for i, (label, func) in enumerate(items):
                with cols[i % columns]:
                    with st.expander(label):
                        func()


        # =========================
        # BUTTONS
        # =========================
        with buttons_tab:
            st.subheader("Buttons")
            st.caption("Interactive action elements")
            st.divider()

            render_section([
                ("st.button", inp.button),
                ("st.download_button", inp.download_button),
                ("st.form_submit_button", inp.form_submit_button),
            ])


        # =========================
        # LINKS
        # =========================
        with links_tab:
            st.subheader("Links")
            st.caption("Navigation and external links")
            st.divider()

            render_section([
                ("st.link_button", inp.link_button),
                ("st.page_link", inp.page_link),
            ], columns=1)


        # =========================
        # SELECTIONS
        # =========================
        with selections_tab:
            st.subheader("Selections")
            st.caption("Choose values")
            st.divider()

            render_section([
                ("st.checkbox", inp.checkbox),
                ("st.color_picker", inp.color_picker),
                ("st.feedback", inp.feedback),
                ("st.multiselect", inp.multiselect),
                ("st.pills", inp.pills),
                ("st.radio", inp.radio),
                ("st.segmented_control", inp.segmented_control),
                ("st.selectbox", inp.selectbox),
                ("st.select_slider", inp.select_slider),
                ("st.toggle", inp.toggle),
            ])


        # =========================
        # NUMERIC
        # =========================
        with numerics_tab:
            st.subheader("Numeric Inputs")
            st.caption("Numbers & ranges")
            st.divider()

            render_section([
                ("st.number_input", inp.number_input),
                ("st.slider", inp.slider),
            ])


        # =========================
        # DATE & TIME
        # =========================
        with datetime_tab:
            st.subheader("Date and Time")
            st.caption("Temporal inputs")
            st.divider()

            render_section([
                ("st.date_input", inp.date_input),
                ("st.datetime_input", inp.datetime_input),
                ("st.time_input", inp.time_input),
            ])


        # =========================
        # TEXT
        # =========================
        with text_tab:
            st.subheader("Text Inputs")
            st.caption("User written data")
            st.divider()

            render_section([
                ("st.chat_input", inp.chat_input),
                ("st.link", inp.link),
                ("st.text_area", inp.text_area),
                ("st.text_input", inp.text_input),
            ])


        # =========================
        # MEDIA
        # =========================
        with media_tab:
            st.subheader("Media & Editors")
            st.caption("Audio, camera & tables")
            st.divider()

            render_section([
                ("st.audio_input", inp.audio_input),
                ("st.camera_input", inp.camera_input),
                ("st.data_editor", inp.data_editor),
            ])


        # =========================
        # FILES
        # =========================
        with files_tab:
            st.subheader("File Uploads")
            st.caption("External files")
            st.divider()

            with st.expander("st.file_uploader"):
                inp.file_uploader()
