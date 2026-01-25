import streamlit as st

# =========================
# BUTTONS
# =========================

def button():
    st.code('st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", icon=None, icon_position="left", disabled=False, use_container_width=None, width="content", shortcut=None)')        
    import streamlit as st


def button():

    st.subheader("Playground st.button()")

    with st.echo():

        # =========================
        # INPUTS DE PARÁMETROS
        # =========================

        label = st.text_input(
            "Label",
            value="Click me"
        )

        key = st.text_input(
            "Key (optional)",
            value=""
        ) or None

        help_text = st.text_input(
            "Help tooltip",
            value="This is a help message"
        )

        button_type = st.selectbox(
            "Type",
            ["primary", "secondary", "tertiary"]
        )

        icon = st.text_input(
            "Icon (emoji or :material/name:)",
            value="🔥"
        ) or None

        icon_position = st.radio(
            "Icon position",
            ["left", "right"],
            horizontal=True
        )

        disabled = st.checkbox("Disabled", value=False)

        width = st.selectbox(
            "Width",
            ["content", "stretch", 150, 300]
        )

        shortcut = st.text_input(
            "Shortcut (ex: Ctrl+K)",
            value=""
        ) or None


        # =========================
        # CALLBACK
        # =========================

        def on_click_action(msg):
            st.success(f"Button clicked! Message: {msg}")


        # =========================
        # RENDER BUTTON
        # =========================

        clicked = st.button(
            label=label,
            key=key,
            help=help_text,
            on_click=on_click_action,
            args=("Hola Streamlit",),
            type=button_type,
            icon=icon,
            icon_position=icon_position,
            disabled=disabled,
            width=width,
            shortcut=shortcut,
        )

        st.write("Return value:", clicked)


def download_button():
    pass

def form_submit_button():
    pass


# =========================
# LINKS
# =========================

def link_button():
    pass

def page_link():
    pass


# =========================
# SELECTIONS
# =========================

def checkbox():
    pass

def color_picker():
    pass

def feedback():
    pass

def multiselect():
    pass

def pills():
    pass

def radio():
    pass

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
