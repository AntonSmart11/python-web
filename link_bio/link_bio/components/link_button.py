import reflex as rx
import link_bio.styles.styles as st

def link_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    'calendar',
                    width=st.Size.BIG.value,
                    height=st.Size.BIG.value,
                ),
                rx.vstack(
                    rx.text(title, style=st.button_title_style),
                    rx.text(body, style=st.button_body_style)
                ),
                align='center'
            )
        ),
        href=url,
        is_external=True,
        width='100%'
    )