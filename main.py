from flet import *

def main(page: Page):
    page.title = 'Ghallab flashlight'
    page.scroll = 'auto'
    page.window.top = 1
    page.window.left = 960
    page.window.width = 390
    page.window.height = 740
    page.bgcolor = 'white'
    page.theme_mode = ThemeMode.LIGHT

    flashlight = Flashlight()
    page.overlay.append(flashlight)

    page.add(
        AppBar(
            title=Text('Ghallab flash light'),
            color='white',
            bgcolor='#e3113e',
        ),
        Row([
            Text('\n\nFlash light App', size=31, color="black")
        ], alignment=MainAxisAlignment.CENTER),

        Row([
            Image(src='Flash.png', width=360)
        ], alignment=MainAxisAlignment.CENTER),

        Row([
            ElevatedButton(
                'ON',
                width=100,
                icon=icons.PLAY_ARROW,
                style=ButtonStyle(
                    bgcolor='#e3113e',
                    color='white',
                    padding=15,
                    shape=ContinuousRectangleBorder(radius=100)
                ),
                on_click=lambda _: flashlight.turn_on()
            ),

            ElevatedButton(
                'OFF',
                width=100,
                icon=icons.PLAY_DISABLED_SHARP,
                style=ButtonStyle(
                    bgcolor='#e3113e',
                    color='white',
                    padding=15,
                    shape=ContinuousRectangleBorder(radius=100)
                ),
                on_click=lambda _: flashlight.turn_off()
            )
        ], alignment=MainAxisAlignment.CENTER),

        Row([
            Text('\n\n\n\n\n Ghallab Flash light App © 2025', size=14, color="black")
        ], alignment=MainAxisAlignment.CENTER),
    )

    page.update()

app(main)
