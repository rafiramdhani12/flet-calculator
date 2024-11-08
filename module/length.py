import flet as ft

# ! length page start
class LengthCalculatorPage(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.input_value = ft.TextField(label="Enter value", on_change=self.convert)
        self.from_unit = ft.Dropdown(
            label="From",
            options=[
                ft.dropdown.Option("mm"),
                ft.dropdown.Option("cm"),
                ft.dropdown.Option("m"),
                ft.dropdown.Option("km"),
                ft.dropdown.Option("in"),
                ft.dropdown.Option("ft"),
                ft.dropdown.Option("yd"),
                ft.dropdown.Option("mi")
            ],
            on_change=self.convert
        )
        self.to_unit = ft.Dropdown(
            label="To",
            options=[
                ft.dropdown.Option("mm"),
                ft.dropdown.Option("cm"),
                ft.dropdown.Option("m"),
                ft.dropdown.Option("km"),
                ft.dropdown.Option("in"),
                ft.dropdown.Option("ft"),
                ft.dropdown.Option("yd"),
                ft.dropdown.Option("mi")
            ],
            on_change=self.convert
        )
        self.result = ft.Text(size=20, color=ft.colors.WHITE)

    def build(self):
        return ft.Column(
            controls=[
                ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.go_back),
                ft.Text("Length Conversion", size=30, color=ft.colors.WHITE),
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
            if self.input_value.value and self.from_unit.value and self.to_unit.value:
                value = float(self.input_value.value)
                from_unit = self.from_unit.value
                to_unit = self.to_unit.value
                
                # Convert to meters first
                meters = self.to_meters(value, from_unit)
                
                # Then convert from meters to desired unit
                result = self.from_meters(meters, to_unit)
                
                self.result.value = f"{value} {from_unit} = {result:.4f} {to_unit}"
            else:
                self.result.value = "Please enter a value and select units"
        except ValueError:
            self.result.value = "Please enter a valid number"
        self.update()

    def to_meters(self, value, unit):
        conversions = {
            "mm": 0.001,
            "cm": 0.01,
            "m": 1,
            "km": 1000,
            "in": 0.0254,
            "ft": 0.3048,
            "yd": 0.9144,
            "mi": 1609.344
        }
        return value * conversions[unit]

    def from_meters(self, meters, unit):
        conversions = {
            "mm": 1000,
            "cm": 100,
            "m": 1,
            "km": 0.001,
            "in": 39.3701,
            "ft": 3.28084,
            "yd": 1.09361,
            "mi": 0.000621371
        }
        return meters * conversions[unit]

# ! length page end
