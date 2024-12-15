import reflex as rx
from my_app_name.styles.styles import Size
from my_app_name.styles.colors import TextColor as TextColor
from my_app_name.styles.colors import Color as Color
import my_app_name.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "JavierDev",
            color=Color.PRIMARY.value,
            style=styles.navbar_title_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )