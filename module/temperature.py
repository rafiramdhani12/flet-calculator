import flet as ft

# ! temperature page start

class TempPage(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.celsius_input = ft.TextField(label="Celsius", on_change=self.celsius_changed)
        self.kelvin_input = ft.TextField(label="Kelvin", on_change=self.kelvin_changed)
        self.reaumur_input = ft.TextField(label="Réaumur", on_change=self.reaumur_changed)

    def build(self):
        return ft.Column(
            controls=[
                ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.go_back),
                ft.Text("Temperature Conversion", size=30, color=ft.colors.WHITE),
                self.celsius_input,
                self.kelvin_input,
                self.reaumur_input,
            ],
            spacing=20
        )

    def go_back(self, _):
        self.page.go("/")

    def celsius_changed(self, e):
        try:
            c = float(self.celsius_input.value)
            self.kelvin_input.value = str(round(c + 273.15, 2))
            self.reaumur_input.value = str(round(c * 0.8, 2))
        except ValueError:
            self.kelvin_input.value = ""
            self.reaumur_input.value = ""
        self.update()

    def kelvin_changed(self):
        try:
            k = float(self.kelvin_input.value)
            self.celsius_input.value = str(round(k - 273.15, 2))
            self.reaumur_input.value = str(round((k - 273.15) * 0.8, 2))
        except ValueError:
            self.celsius_input.value = ""
            self.reaumur_input.value = ""
        self.update()

    def reaumur_changed(self):
        try:
            r = float(self.reaumur_input.value)
            self.celsius_input.value = str(round(r / 0.8, 2))
            self.kelvin_input.value = str(round((r / 0.8) + 273.15, 2))
        except ValueError:
            self.celsius_input.value = ""
            self.kelvin_input.value = ""
        self.update()

# ! temperature page end
