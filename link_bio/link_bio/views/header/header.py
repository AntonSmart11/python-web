import reflex as rx

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
                    'antonsmart'
                ),
                align='start',
                spacing='0'
            ),
            align='center'
        ),
        rx.text('Soy un apasionado de la industria tecnológica, me gusta crear aplicaciones web o páginas web que brinden una experiencia buena para el usuario. ¡BIENVENID@!'),
        align='start'
    )