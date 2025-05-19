import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as st
from link_bio.styles.styles import Size as Size

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                align='center',
                max_width=st.MAX_WIDTH,
                width='100%',
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
            ),
        ),
        footer(),
    )

app = rx.App(
    stylesheets=st.STYLESHEETS,
    style=st.BASE_STYLE,
)
app.add_page(
    index,
    title='AntonSmart',
    description='Soy un apasionado de la industria tecnológica, especializado en varios lenguajes de programación y frameworks.',
)
app._compile()