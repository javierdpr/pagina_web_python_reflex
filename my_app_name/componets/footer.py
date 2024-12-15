import reflex as rx
import datetime
from my_app_name.styles.styles import Size as Size
from my_app_name.styles.colors import TextColor as TextColor
from my_app_name.styles.colors import Color as Color

def footer() -> rx.Component:
        return rx.vstack(
        rx.link(f"2022-{datetime.date.today().year} javierdev by javier de prados",
                href="https://portfoliojavierdev.netlify.app/",
                is_external=True,
                font_size=Size.MEDIUM.value
                ),
        rx.text("desarrollando web desde la mancha",
                font_size=Size.MEDIUM.value,
                margin_top="0px !important"
                ),
        padding_bottom=Size.BIG.value,
        align="center",
        color=TextColor.FOOTER.value
        )