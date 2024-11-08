import flet as ft

# ! speed page start

class SpeedPage(ft.UserControl):
    def __init__(self, page):
        super().__init__()  # Hapus 'page' dari sini
        self.page = page
        self.input_value = ft.TextField(label="Enter speed", on_change=self.convert)
        self.from_unit = ft.Dropdown(
            label="From",
            options=[
                ft.dropdown.Option("m/s"),
                ft.dropdown.Option("km/h"),
                ft.dropdown.Option("mph"),
                ft.dropdown.Option("ft/s"),
                ft.dropdown.Option("knot")
            ],
            on_change=self.convert
        )
        self.to_unit = ft.Dropdown(
            label="To",
            options=[
                ft.dropdown.Option("m/s"),
                ft.dropdown.Option("km/h"),
                ft.dropdown.Option("mph"),
                ft.dropdown.Option("ft/s"),
                ft.dropdown.Option("knot")
            ],
            on_change=self.convert
        )
        self.result = ft.Text(size=20, color=ft.colors.WHITE)  # Tambahkan ini

    def build(self):
        return ft.Column(
            controls=[
                ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.go_back),
                ft.Text("Speed Conversion", size=30, color=ft.colors.WHITE),
                self.input_value,
                self.from_unit,
                self.to_unit,
                self.result,
            ],
            spacing=20
        )

    def go_back(self, _):
        self.page.go("/")

    def convert(self, _):
        try:
            if self.input_value.value and self.from_unit.value and self.to_unit.value:  # Perbaiki 'form_unit' menjadi 'from_unit'
                value = float(self.input_value.value)
                from_unit = self.from_unit.value
                to_unit = self.to_unit.value

                # Convert to m/s first
                m_s = self.to_m_s(value, from_unit)

                # Then convert from m/s to desired unit
                result = self.from_m_s(m_s, to_unit)

                self.result.value = f"{value} {from_unit} = {result:.4f} {to_unit}"
            else:
                self.result.value = "Please enter a value and select units"
        except ValueError:
            self.result.value = "Please enter a valid number"
        self.update()

    def to_m_s(self, value, unit):
        conversions = {
            "m/s": 1,
            "km/h": 1/3.6,
            "mph": 0.44704,
            "ft/s": 0.3048,
            "knot": 0.514444
        }
        return value * conversions[unit]

    def from_m_s(self, value, unit):
        conversions = {
            "m/s": 1,
            "km/h": 3.6,
            "mph": 2.23694,
            "ft/s": 3.28084,
            "knot": 1.94384
        }
        return value * conversions[unit] 

# ! speed page end
