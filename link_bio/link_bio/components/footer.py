import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src='favicon.ico'),
        rx.text(
            f'© 2023 - {datetime.date.today().year} Antonio Ovando - Página de Enlaces',
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            'Desarrollador FullStack',
        ),
        align='center',
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value,
        spacing='0',
    )