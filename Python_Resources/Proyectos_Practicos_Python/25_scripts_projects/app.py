import streamlit as st
from st_on_hover_tabs import on_hover_tabs
from translate import Translator

st.checkbox()

if  option[0]:
    from modules.a_voice_sales_bot import ejecutar_busqueda_amazon

    st.set_page_config(page_title="Buscador por Voz", page_icon="🎤")

    st.title("🎤 Buscador por Voz")
    st.write("Probá decir algo y buscarlo directamente en Amazon.")

    def manejar_busqueda():
        texto, url = ejecutar_busqueda_amazon()
        if texto:
            st.success(f"✅ Has dicho: {texto}")
            st.markdown(f"[🔗 Abrir búsqueda en Amazon]({url})", unsafe_allow_html=True)
        else:
            st.error("❌ No se pudo reconocer tu voz.")

    if st.button("🎧 Hablar y Buscar"):
        st.info("🎙️ Escuchando...")
        texto, url = ejecutar_busqueda_amazon()
        if texto:
            st.success(f"✅ Has dicho: {texto}")
            st.markdown(f"[🔗 Abrir búsqueda en Amazon]({url})", unsafe_allow_html=True)
        else:
            st.error("❌ No se pudo reconocer tu voz.")