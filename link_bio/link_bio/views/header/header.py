import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback='AO', size='7', radius='full'),
        rx.text('AntonSmart11'),
        rx.text('HOLA 👋🏻 MI NOMBRE ES ANTONIO OVANDO'),
        rx.text('Soy un apasionado de la industria tecnológica, me gusta crear aplicaciones web o páginas web que brinden una experiencia buena para el usuario. !BIENVENID@!'),
        align='center'
    )