import flet as ft
# ! weight mass page start

class WeightMassPage(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
        self.input_value = ft.TextField(label="Enter Value" , on_change=self.convert)
        self.from_unit = ft.Dropdown(
            label = "from",
            options=[
                ft.dropdown.Option("mg"),
                ft.dropdown.Option("g"),
                ft.dropdown.Option("kg"),
                ft.dropdown.Option("t"),
                ft.dropdown.Option("oz"),
                ft.dropdown.Option("lb"),
                ft.dropdown.Option("st")
            ],
            on_change=self.convert
        )
        self.to_unit = ft.Dropdown(
            label = "to",
             options=[
                ft.dropdown.Option("mg"),
                ft.dropdown.Option("g"),
                ft.dropdown.Option("kg"),
                ft.dropdown.Option("t"),
                ft.dropdown.Option("oz"),
                ft.dropdown.Option("lb"),
                ft.dropdown.Option("st")
            ],
            on_change=self.convert
        )
        self.result = ft.Text(size=20,color=ft.colors.WHITE)
    
    def build(self):
        return ft.Column(
            controls=[
                ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.go_back),
                ft.Text("Weight and mass conversion" , size=30,color=ft.colors.WHITE),
                self.input_value,
                self.from_unit,
                self.to_unit,
                self.result,
            ],
            spacing=20
        )
    
    def go_back(self,_):
        self.page.go("/")
    
    def convert(self,_):
        try:
            if self.input_value.value and self.from_unit.value and self.to_unit.value:
                value = float(self.input_value.value)
                from_unit = self.from_unit.value
                to_unit = self.to_unit.value
                
                # ! conversi ke gram
                
                grams = self.to_grams(value,from_unit)
                
                # ! lalu conversi dari gram ke unit lainya
                
                result = self.from_grams(grams,to_unit)
                
                self.result.value = f"{value} {from_unit} = {result:.4f} {to_unit}"
            else:
                self.result.value = "please enter a value and select units"
        except ValueError:
            self.result.value = "Please enter a valid number"
        self.update()
        
    def to_grams(self,value,unit):
        conversions = {
            "mg": 0.001,
            "g": 1,
            "kg": 1000,
            "t": 1000000,
            "oz": 28.34952,
            "lb": 453.59237,
            "st": 6350.29318
        }
        return value * conversions[unit]
    
    def from_grams(self,value,unit):
        conversions = {
           "mg": 1000,
            "g": 1,
            "kg": 0.001,
            "t": 0.000001,
            "oz": 0.03527396,
            "lb": 0.00220462,
            "st": 0.000157473
        }
        return value * conversions[unit]
    
# ! weight mass page end
