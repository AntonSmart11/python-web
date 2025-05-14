import reflex as rx
import link_bio.styles.styles as st

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        style=st.title_style,
        size='7',
    )