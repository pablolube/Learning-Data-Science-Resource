import streamlit as st
import numpy as np
from io import BytesIO
from datetime import timedelta
from PIL import Image
from pathlib import Path
def audio():
    st.title("🔊 Apunte completo: st.audio")

    # =================================================
    # FIRMA DEL MÉTODO
    # =================================================
    st.subheader("📌 Firma del método")

    st.code(
        'st.audio(data, format="audio/wav", start_time=0, *, '
        'sample_rate=None, end_time=None, loop=False, '
        'autoplay=False, width="stretch")',
        language="python"
    )

    
    # =================================================
    # DATA (ruta local)
    # =================================================
    with st.expander("📂 Parámetro: data (ruta local)"):
        with st.echo():
            st.audio("Streamlit/apunte_streamlit/archivos/audio_ejemplo.wav")
    # =================================================
    # DATA (bytes / BytesIO)
    # =================================================
    with st.expander("📦 Parámetro: data (BytesIO)"):
        st.info(''' BytesIO es una clase del módulo io que crea un archivo en memoria.

👉 Se comporta como un archivo, pero:

❌ no está en el disco

✅ vive en RAM

✅ trabaja con bytes (b"...")

En otras palabras:

BytesIO = “un archivo falso, pero real para Python” ''')
        with st.echo():
            audio_bytes = BytesIO(open("Streamlit/apunte_streamlit/archivos/audio_ejemplo.wav", "rb").read())
            st.audio(audio_bytes)

    # =================================================
    # DATA (URL)
    # =================================================
    with st.expander("🌐 Parámetro: data (URL)"):
        with st.echo():
            st.audio(
                "https://www2.cs.uic.edu/~i101/SoundFiles/StarWars60.wav"
            )

    # =================================================
    # DATA (NumPy array)
    # =================================================
    with st.expander("📊 Parámetro: data (NumPy array)"):
        with st.echo():
            sr = 16000
            t = np.linspace(0, 1, sr)
            audio = 0.5 * np.sin(2 * np.pi * 440 * t)

            st.audio(audio, sample_rate=sr)

    # =================================================
    # START_TIME
    # =================================================
    with st.expander("⏱️ Parámetro: start_time"):
        with st.echo():
            st.audio(
                "Streamlit/apunte_streamlit/archivos/audio_ejemplo.wav",
                start_time=5
            )

    # =================================================
    # START_TIME (string / timedelta)
    # =================================================
    with st.expander("⏱️ start_time (string / timedelta)"):
        with st.echo():
            st.audio(
                "Streamlit/apunte_streamlit/archivos/audio_ejemplo.wav",
                start_time="10s"
            )

    # =================================================
    # SAMPLE_RATE
    # =================================================
    with st.expander("🎚️ Parámetro: sample_rate"):
        with st.echo():
            sr = 22050
            t = np.linspace(0, 1, sr)
            audio = np.sin(2 * np.pi * 220 * t)

            st.audio(audio, sample_rate=sr)

    # =================================================
    # END_TIME
    # =================================================
    with st.expander("⏹️ Parámetro: end_time"):
        with st.echo():
            st.audio(
                "Streamlit/apunte_streamlit/archivos/audio_ejemplo.wav",
                end_time=10
            )

    # =================================================
    # LOOP
    # =================================================
    with st.expander("🔁 Parámetro: loop"):
        with st.echo():
            st.audio(
                "Streamlit/apunte_streamlit/archivos/audio_ejemplo.wav",
                loop=True
            )

    # =================================================
    # AUTOPLAY
    # =================================================
    with st.expander("▶️ Parámetro: autoplay"):
        with st.echo():
            st.audio(
                "Streamlit/apunte_streamlit/archivos/audio_ejemplo.wav",
                autoplay=True
            )

    # =================================================
    # WIDTH
    # =================================================
    with st.expander("📐 Parámetro: width"):
        with st.echo():
            st.audio(
                "Streamlit/apunte_streamlit/archivos/audio_ejemplo.wav",
                width=300
            )


    # =================================================
    # CASOS DE USO
    # =================================================
    st.subheader("🧠 Casos de uso comunes")

    # -------------------------------------------------
    # Caso 1: Reproducir audio subido
    # -------------------------------------------------
    with st.expander("📁 Caso de uso: Reproducir audio cargado por el usuario"):
        with st.echo():
            archivo = st.file_uploader(
                "Subí un audio",
                type=["wav", "mp3"]
            )

            if archivo:
                st.audio(archivo)

    # -------------------------------------------------
    # Caso 2: Preview de grabación
    # -------------------------------------------------
    with st.expander("🎤 Caso de uso: Preview de st.audio_input"):
        with st.echo():
            audio = st.audio_input("Grabá tu voz")

            if audio:
                st.audio(audio)

    # -------------------------------------------------
    # Caso 3: Cortar un fragmento
    # -------------------------------------------------



    with st.expander("✂️ Caso de uso: Reproducir un fragmento de audio"):
        with st.echo():

            # Inputs
            start = st.number_input(
                "⏱ Desde (segundos)",
                min_value=0.0,
                value=0.0,
                step=0.5
            )

            end = st.number_input(
                "⏱ Hasta (segundos)",
                min_value=0.0,
                value=5.0,
                step=0.5
            )

            # Validación
            if start >= end:
                st.warning("⚠️ El tiempo inicial debe ser menor al tiempo final")
            else:
                st.audio(
                    "Streamlit/apunte_streamlit/archivos/audio_ejemplo.wav",
                    start_time=start,
                    end_time=end
                )

    # -------------------------------------------------
    # Caso 4: Audio en loop
    # -------------------------------------------------
    with st.expander("🔁 Caso de uso: Música de fondo"):
        with st.echo():
            st.audio(
                "Streamlit/apunte_streamlit/archivos/audio_ejemplo.wav",
                loop=True
            )

    # -------------------------------------------------
    # Caso 5: Señal generada por código
    # -------------------------------------------------
    with st.expander("🧪 Caso de uso: Audio generado por NumPy"):
        with st.echo():
            sr = 16000
            t = np.linspace(0, 2, sr * 2)
            audio = np.sin(2 * np.pi * 330 * t)

            st.audio(audio, sample_rate=sr)

def image():
 

    st.title("🖼️ Apunte completo — st.image")

    # Imagen base (PIL)
    pil_img = Image.open(
        "Streamlit/apunte_streamlit/archivos/imagen_ejemplo.jpg"
    )


    # =================================================
    # image
    # =================================================
    with st.expander("📌 Parámetro: image"):
        with st.echo():
            st.image(pil_img)

    # =================================================
    # caption
    # =================================================
    with st.expander("📌 Parámetro: caption"):
        with st.echo():
            st.image(
                pil_img,
                caption="Esta es una imagen con caption"
            )

    # =================================================
    # width
    # =================================================
    with st.expander("📌 Parámetro: width"):
        with st.echo():
            st.image(
                pil_img,
                width=300
            )

    # =================================================
    # use_column_width (deprecated)
    # =================================================
    with st.expander("📌 Parámetro: use_column_width (deprecated)"):
        with st.echo():
            st.image(
                pil_img,
                use_column_width=True
            )

    # =================================================
    # use_container_width
    # =================================================
    with st.expander("📌 Parámetro: use_container_width"):
        with st.echo():
            st.image(
                pil_img,
                use_container_width=True
            )

    # =================================================
    # clamp
    # =================================================
    with st.expander("📌 Parámetro: clamp"):
        st.info('''Si se deben restringir los valores de píxeles de la imagen a un rango válido (0-255 por canal). Esto solo se utiliza para imágenes de matriz de bytes; el parámetro se ignora para URL y archivos de imágenes. Si se establece en Falso (predeterminado) y una imagen tiene un valor fuera de rango, se generará un RuntimeError . ''')
        with st.echo():
            
            ruido = np.random.randint(
                -50, 300, (200, 200, 3)
            )

            st.image(
                ruido,
                clamp=True
            )


    # =================================================
    # output_format
    # =================================================
    with st.expander("📌 Parámetro: output_format"):
        with st.echo():
            st.image(
                pil_img,
                output_format="PNG",
                caption="Renderizada como PNG"
            )

def logo():
    pass
'''

    # =================================================
    # TÍTULO
    # =================================================
    st.title("📘 Documentación práctica — st.logo()")

    # =================================================
    # FIRMA DEL MÉTODO
    # =================================================
    st.code(
        'st.logo(image, *, size="medium", link=None, icon_image=None)',
        language="python"
    )

    # =================================================
    # PARÁMETRO: image
    # =================================================
    with st.expander("🔹 Parámetro: image — Imagen del logotipo"):
        st.markdown("""
        Imagen que se muestra en:
        - Esquina superior izquierda
        - Barra lateral

        Acepta cualquier formato compatible con `st.image()`  
        ❌ Excepto listas
        """)

        with st.echo():
            st.logo(
                image="Streamlit/apunte_streamlit/archivos/logo.png"
            )

    # =================================================
    # PARÁMETRO: size
    # =================================================
    with st.expander("🔹 Parámetro: size — Tamaño del logotipo"):
        st.markdown("""
        Controla la altura máxima del logo:

        - `"small"` → 20 px  
        - `"medium"` → 24 px (default)  
        - `"large"` → 32 px
        """)

        with st.echo():
            st.logo(
                image="Streamlit/apunte_streamlit/archivos/logo.png",
                size="large"
            )

    # =================================================
    # PARÁMETRO: link
    # =================================================
    with st.expander("🔹 Parámetro: link — Enlace al hacer clic"):
        st.markdown("""
        URL externa que se abre al hacer clic en el logotipo.

        ⚠️ Debe comenzar con:
        - `http://`
        - `https://`
        """)

        with st.echo():
            st.logo(
                image="Streamlit/apunte_streamlit/archivos/logo.png",
                link="https://streamlit.io"
            )

    # =================================================
    # PARÁMETRO: icon_image
    # =================================================
    with st.expander("🔹 Parámetro: icon_image — Ícono con sidebar cerrado"):
        st.markdown("""
        Imagen alternativa que se muestra cuando la barra lateral está cerrada.

        📌 Recomendación:
        - `image` → logo horizontal  
        - `icon_image` → imagen cuadrada
        """)

        with st.echo():
            st.logo(
                image="Streamlit/apunte_streamlit/archivos/logo.png",
                icon_image="assets/logo_icon.png"
            )

    # =================================================
    # CASOS DE USO
    # =================================================
    st.divider()
    st.subheader("🧪 Casos de uso")

    # -------------------------------------------------
    # CASO 1
    # -------------------------------------------------
    with st.expander("✅ Caso 1 — Logo simple (default)"):
        with st.echo():
            st.logo("assets/logo_horizontal.png")

    # -------------------------------------------------
    # CASO 2
    # -------------------------------------------------
    with st.expander("✅ Caso 2 — Logo clickeable"):
        with st.echo():
            st.logo(
                image="assets/logo_horizontal.png",
                link="https://www.miempresa.com"
            )

    # -------------------------------------------------
    # CASO 3
    # -------------------------------------------------
    with st.expander("✅ Caso 3 — Logo adaptable al sidebar ⭐"):
        with st.echo():
            st.logo(
                image="assets/logo_horizontal.png",
                icon_image="assets/logo_icon.png",
                size="medium"
            )

    # -------------------------------------------------
    # CASO 4
    # -------------------------------------------------
    with st.expander("✅ Caso 4 — App corporativa (tema fijo)"):
        st.markdown("""
        Útil cuando el logo **no se ve bien en modo claro y oscuro**.
        """)

        st.code(
            """
    # .streamlit/config.toml

    [theme]
    base = "light"

    [client]
    toolbarMode = "minimal"
            """,
            language="toml"
        )

    # =================================================
    # DETALLES IMPORTANTES
    # =================================================
    with st.expander("⚠️ Detalles importantes"):
        st.markdown("""
        - Llamar `st.logo()` **al inicio del script**
        - Si se llama varias veces → **solo se muestra la última**
        - Evitar imágenes con márgenes transparentes
        - `icon_image` mejora mucho la UX
        """)

    # =================================================
    # CONTENIDO DE EJEMPLO
    # =================================================
    st.sidebar.write("📌 Barra lateral")
    st.write("Contenido principal de la aplicación")

'''

def video():
    pass
