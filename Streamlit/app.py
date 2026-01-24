import streamlit as st
import Header_and_body as hb
import Formated_text as ft
import data_elements as de

st.set_page_config(
    page_title="Apunte Steamlit",
    layout="wide"
)

tematicas = ("Headings and body", "Formated Text","Data Elements")
sidebar = st.sidebar.radio("Barra Lateral", tematicas)

st.title("APUNTE DE STREAMLIT")
st.divider()
match sidebar:
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

    case "Formated Text":
        st.header("Formated Text")

        with st.expander("Badge"):
            ft.badge()

        with st.expander("Caption"):
            ft.caption()

        with st.expander("Code"):
            ft.code()

        with st.expander("Divider"):
            ft.divider()

        with st.expander("Echo"):
            ft.echo()

        with st.expander("LaTeX"):
            ft.latex()

        with st.expander("Text"):
            ft.text()

        with st.expander("Help"):
            ft.pagina_help()

        with st.expander("HTML"):
            ft.html()
    case "Data Elements":

        with st.expander("📊 DataFrame"):
            de.mostrar_dataframe()

        with st.expander("✏️ Data Editor"):
            de.editor_dataframe()

        with st.expander("⚙️ Column Config"):
            de.configurar_columnas()

        with st.expander("📋 Table"):
            de.mostrar_tabla()

        with st.expander("📈 Metric"):
            de.mostrar_metrica()

        with st.expander("🧾 JSON"):
            de.mostrar_json()
