import reflex as rx
import link_bio.styles.styles as st

def link_icon(url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            'link'
        ),
        href=url,
        is_external=True
    )