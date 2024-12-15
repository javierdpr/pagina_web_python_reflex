import reflex as rx
from my_app_name.componets.link_icon import link_icon
from my_app_name.styles.styles import Size as Size
from my_app_name.styles.colors import TextColor as TextColor
from my_app_name.styles.colors import Color as Color

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="JD", 
                        size="8",
                        color=TextColor.BODY.value,
                        bg=Color.CONTENT.value),
            rx.vstack(
                rx.heading(
                    "Javier De Prados Ruedas",
                    size="lg"
                ),
                rx.text(
                    "@javierdev",
                    margin_top="0px !important",
                    color=TextColor.BODY.value
                    ),
                    rx.hstack(
                        link_icon("https://github.com/javierdpr", "/icons/github-dark.svg"),
                        rx.spacer(),
                        link_icon("https://www.linkedin.com/in/javier-de-prados-ruedas-6850b1291/", "/icons/linkedin.svg"),
                        rx.spacer(),
                        link_icon("https://portfoliojavierdev.netlify.app/", "/icons/portfolio.svg")
                    ),
                    align_items="start",
                ),
                spacing="4"
            ),
            rx.text("soy desarrollador web llevo dos años de experiencia en el desarrollo web y aplicaciones web aqui tienes algunos de los enlaces que me han ayudado a mi espero que tambien te ayuden a ti",
                    color=TextColor.BODY.value
                    ),
            spacing="6",
            align_items="start",
        )
