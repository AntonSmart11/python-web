import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font
from .fonts import FontWeight as FontWeight

# Constants
MAX_WIDTH = '600px'

# Fonts
STYLESHEETS =[
    'https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap',
    'https://fonts.googleapis.com/css2?family=Audiowide&display=swap'
]

# Sizes
class Size(Enum):
    ZERO='0px !important'
    SMALL='0.5em'
    MEDIUM='0.8em'
    DEFAULT='1em'
    LARGE='1.5em'
    BIG='2em'
    VERY_BIG='4em'

# Styles

BASE_STYLE = {
    'font_family': Font.DEFAULT.value,
    'font_weight': FontWeight.LIGHT.value,
    'background_color': Color.BACKGROUND.value,
    rx.heading: {
        "color": TextColor.HEADER.value,
        'font_family': Font.DEFAULT.value,
    },
    rx.button: {
        "width": "100%",
        "height": "100%",   
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "cursor": "pointer",
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start", 
        "_hover": {
            "background_color": Color.SECONDARY.value,
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_size=Size.LARGE.value,
)

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
)

button_title_style = dict(
    font_size = Size.DEFAULT.value,
    font_family=Font.TITLE.value,
    font_weight='Bold',
    color = TextColor.HEADER.value,
)

button_body_style = dict(
    font_size = Size.MEDIUM.value,
    color = TextColor.FOOTER.value,
)