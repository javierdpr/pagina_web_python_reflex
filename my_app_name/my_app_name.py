import reflex as rx
from my_app_name.componets.navabar import navbar
from my_app_name.views.header.header import header
from my_app_name.views.links.links import links
from my_app_name.componets.footer import footer
import my_app_name.styles.styles as styles
from my_app_name.styles.styles import Size as Size


#class State(rx.State):
    #pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            ),
        ),
        footer()
    )



app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS
)
app.add_page(
    index,
    title="JavierDev",
    description="pagina web de enlaces hecha en reflex con python"
    )
app._compile()
