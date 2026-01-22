import streamlit as st
import Header_and_body as hb
import Formated_text as ft

st.set_page_config(
    page_title="Ejemplos st.header",
    layout="wide"
)

tematicas = ("Headings and body", "Formated Text")
sidebar = st.sidebar.selectbox("Barra Lateral", tematicas)

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
            ft.help()

        with st.expander("HTML"):
            ft.html()