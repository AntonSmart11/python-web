import reflex as rx
from link_bio import constants as const
from link_bio.components.link_button import link_button
from link_bio.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title('Mis redes'),
        link_button(
            'Portafolio Web', 
            'Ve mi perfil profesional junto con mis proyectos.',
            'icons/portfolio.svg',
            const.PORTFOLIO_WEB_URL
        ),
        link_button(
            'LinkedIn', 
            'Mi LinkedIn dónde encontrarás todas mis habilidades.',
            'icons/linkedin.svg',
            const.LINKEDIN_URL
        ),
        link_button(
            'GitHub', 
            'Descube mi GitHub dónde están todos mis códigos.',
            'icons/github.svg',
            const.GITHUB_URL
        ),

        title('Contacto'),
        link_button(
            'Email', 
            const.EMAIL,
            'icons/email.svg',
            f'mailto:{const.EMAIL}'
        ),
        width='100%',
        align='center',
        spacing='4'
    )