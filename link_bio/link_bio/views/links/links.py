import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title('Mis redes'),
        link_button(
            'Portafolio Web', 
            'Ve mi perfil profesional junto con mis proyectos.', 
            'https://antonsmart11.github.io/cv-portfolio/'
        ),
        link_button(
            'LinkedIn', 
            'Mi LinkedIn dónde encontrarás todas mis habilidades.', 
            'https://www.linkedin.com/in/antoniooc11/'
        ),
        link_button(
            'GitHub', 
            'Descube mi GitHub dónde están todos mis códigos.', 
            'https://github.com/AntonSmart11'
        ),
        title('Mis redes'),
        link_button(
            'Portafolio Web', 
            'Ve mi perfil profesional junto con mis proyectos.', 
            'https://antonsmart11.github.io/cv-portfolio/'
        ),
        link_button(
            'LinkedIn', 
            'Mi LinkedIn dónde encontrarás todas mis habilidades.', 
            'https://www.linkedin.com/in/antoniooc11/'
        ),
        link_button(
            'GitHub', 
            'Descube mi GitHub dónde están todos mis códigos.', 
            'https://github.com/AntonSmart11'
        ),
        width='100%',
        align='center'
    )