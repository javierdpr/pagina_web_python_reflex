import reflex as rx
import my_app_name.styles.styles as styles


def link_icon(url: str, image: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width="2em",
        ), 
        href=url,
        is_external=True
    )
