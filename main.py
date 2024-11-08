import flet as ft
from module.route import route_change


def main(page: ft.Page):
    page.title = "Calculator"
    page.window.width = 450
    page.window.height = 500
    page.window.resizable = False
    page.bgcolor = ft.colors.BLACK
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        
        # ! memanggil method change route dengan anonim function
    page.on_route_change = lambda e : route_change(page,e)
    page.on_view_pop = view_pop
    
    page.bottom_sheet = ft.BottomSheet(
        content=ft.Container(
            ft.Column(
                [
                    ft.ListTile(
                        leading= ft.Icon(name=ft.icons.CURRENCY_EXCHANGE,color="white",size=30),
                        title=ft.Text("Currency"),
                        on_click=lambda _: page.go("/currency")
                    ),
                    ft.ListTile(
                        leading= ft.Icon(name=ft.icons.DEVICE_THERMOSTAT,color="white",size=30),
                        title=ft.Text("Temperature"),
                        on_click=lambda _: page.go("/temperature")
                    ),
                    ft.ListTile(
                        leading= ft.Icon(name=ft.icons.DATE_RANGE,color="white",size=30),
                        title=ft.Text("Date calculation"),
                        on_click=lambda _: page.go("/date")
                    ),
                    ft.ListTile(
                        leading= ft.Icon(name=ft.icons.STRAIGHTEN,color="white",size=30),
                        title=ft.Text("Length"),
                        on_click=lambda _: page.go("/length")
                    ),
                    ft.ListTile(
                        leading= ft.Icon(name=ft.icons.FITNESS_CENTER,color="white",size=30),
                        title=ft.Text("Weigth and mass"),
                        on_click=lambda _: page.go("/weight_mass")
                    ),
                    ft.ListTile(
                        leading= ft.Icon(name=ft.icons.SPEED,color="white",size=30),
                        title=ft.Text("Speed"),
                        on_click=lambda _: page.go("/speed")
                    ),
                    ft.ListTile(
                        leading= ft.Icon(name=ft.icons.ACCESS_TIME,color="white",size=30),
                        title=ft.Text("Time"),
                        on_click=lambda _: page.go("/time")
                    ),
                ],
                scroll=ft.ScrollMode.AUTO
            ),
            padding=10,
        ),
        open=False,
    )

    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)
    
