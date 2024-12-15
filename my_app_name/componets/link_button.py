import reflex as rx
import my_app_name.styles.styles as styles
from my_app_name.styles.styles import Size as Size

def link_button(title: str, body: str, imagen: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=imagen,
                    alt=title,
                    width=Size.BIG.value,
                    height=Size.BIG.value,
                    margin=Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing="2",
                    align_items="start",
                    margin="0px !important",
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                ),
            ), 
        ),
        href=url,
        is_external=True,
        width="100%"
    )