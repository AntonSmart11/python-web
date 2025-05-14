import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src='favicon.ico'),
        rx.text(f'© 2023 - {datetime.date.today().year} Antonio Ovando. Desarrollador FullStack'),
        align='center'
    )