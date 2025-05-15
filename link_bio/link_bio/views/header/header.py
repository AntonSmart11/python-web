import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback='AO', size='7', radius='full'),
            rx.vstack(
                rx.heading(
                    'Antonio Ovando',
                    size='7'
                ),
                rx.text(
                    'antonsmart',
                    color=TextColor.BODY.value,
                ),
                rx.hstack(
                    link_icon("https://antonsmart11.github.io/cv-portfolio/"),
                    link_icon("https://www.linkedin.com/in/antoniooc11/"),
                    link_icon("https://github.com/AntonSmart11"),
                ),
                align='start',
                spacing='0'
            ),
            align='center',
            spacing='4'
        ),
        rx.flex(
            rx.spacer(),
            info_text('✓', 'FrontEnd'),
            rx.spacer(),
            info_text('✓', 'BackEnd'),
            rx.spacer(),
            info_text('✓', 'Bases de Datos'), 
            rx.spacer(),
            width='100%'
        ),
        rx.text(
            'Soy un apasionado de la industria tecnológica, especializado en varios lenguajes de programación y frameworks, me gusta crear aplicaciones web o páginas web que brinden una experiencia buena para el usuario. ¡BIENVENID@ A MÍ PÁGINA DE ENLACES!',
            color=TextColor.BODY.value,
        ),
        spacing='6',
        align='start',
    )