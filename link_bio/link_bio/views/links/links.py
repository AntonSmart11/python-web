import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button('Portafolio Web', 'https://antonsmart11.github.io/cv-portfolio/'),
        link_button('LinkedIn', 'https://www.linkedin.com/in/antoniooc11/'),
        link_button('GitHub', 'https://github.com/AntonSmart11'),
        align='center'
    )