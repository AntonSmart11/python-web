import reflex as rx
from link_bio import constants as const
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback='AO', 
                size='7',
                src='avatar.webp',
                radius='full',
                color_scheme='gray',
                high_contrast=False,
                variant='solid',
                border='4px solid',
                border_color=Color.PRIMARY.value
            ),
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
                    link_icon(
                        'icons/portfolio.svg',
                        const.PORTFOLIO_WEB_URL,
                        'Portafolio Web',
                    ),
                    link_icon(
                        'icons/linkedin.svg',
                        const.LINKEDIN_URL,
                        'LinkedIn',
                    ),
                    link_icon(
                        'icons/github.svg',
                        const.GITHUB_URL,
                        'GitHub',
                    ),
                    spacing='5'
                ),
                align='start',
                spacing='1'
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