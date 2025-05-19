import reflex as rx
import link_bio.styles.styles as st
from link_bio.styles.styles import Size as Size

def link_button(title: str, body: str, image:str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.BIG.value,
                    height=Size.BIG.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(title, style=st.button_title_style),
                    rx.text(body, style=st.button_body_style),
                    spacing='1',
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                ),
                align='center',
                width='100%',
            )
        ),
        href=url,
        is_external=True,
        width='100%'
    )