import reflex as rx
from reflexapp.styles.colors import TextColor as TextColor
from reflexapp.styles.colors import Colors as Colors
from reflexapp.styles.styles import Size as Size
import reflexapp.routes.routes as router


def header(details: True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.link(
                rx.avatar(
                    fallback="PM",
                    size="6",
                    src="/avatar.jpg",
                    style={
                        "border-radius": "50%",
                        "padding": "2px",
                        "border": "3px solid " + Colors.PRIMARY.value
                    }
                ),
                href=router.Route.INDEX.value
            ),

            rx.vstack(
                rx.heading("Pablo Javier Montícoli", size="6",
                           color=TextColor.WHITE.value),
                rx.text("@PJMonticoli", color=TextColor.WHITE.value)
            ),
            spacing="6",
            align_items="start"
        ),
        rx.cond(
            details,
            rx.box(
                rx.text.strong("About me", color=TextColor.BODY.value),
                rx.text("I'm a Full-Stack Programmer, graduated from the National Technological University with experience in:",
                        color=TextColor.BODY.value,
                        font_size=Size.MEDIUM.value),
                rx.unordered_list(
                    rx.list_item("Front-End: HTML, CSS, JavaScript, TypeScript, Angular and Reflex.",
                                 color=TextColor.BODY.value, font_size=Size.MEDIUM.value),
                    rx.list_item("Back-End: .NET, C#, Java, Python, NodeJs(ExpressJs), Supabase and Reflex.",
                                 color=TextColor.BODY.value, font_size=Size.MEDIUM.value),
                    rx.list_item("Database Management: SQLServer, MySQL, PostgreSQL and MongoDB.",
                                 color=TextColor.BODY.value, font_size=Size.MEDIUM.value),
                    rx.list_item("Scrum Methodology (Jira Software).",
                                 color=TextColor.BODY.value, font_size=Size.MEDIUM.value),
                )
            )
        ),
        align_items="start",
        width="100%"
    )
