import flet as ft

class TimePage(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
        
        self.input_value = ft.TextField(label="enter value" , on_change=self.convert_time)
        self.from_unit = ft.Dropdown(
            label="from",
            options=[
                ft.dropdown.Option("Microsecond"),
                ft.dropdown.Option("Miliseconds"),
                ft.dropdown.Option("Second"),
                ft.dropdown.Option("Minute"),
                ft.dropdown.Option("Hours"),
                ft.dropdown.Option("Days"),
                ft.dropdown.Option("Week"),
                ft.dropdown.Option("Years"),
            ],
            on_change=self.convert_time
        )
        
        self.to_unit = ft.Dropdown(
            label="to",
            options=[
                ft.dropdown.Option("Microsecond"),
                ft.dropdown.Option("Miliseconds"),
                ft.dropdown.Option("Second"),
                ft.dropdown.Option("Minute"),
                ft.dropdown.Option("Hours"),
                ft.dropdown.Option("Days"),
                ft.dropdown.Option("Week"),
                ft.dropdown.Option("Years"),
            ],
            on_change=self.convert_time
        )
        self.result = ft.Text(size=20,color=ft.colors.WHITE)
        
    def build(self):
        return ft.Column(
            controls=[
                ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.go_back),
                ft.Text("Time Unit Conversion" , size=30 , color=ft.colors.WHITE),
                self.input_value,
                self.from_unit,
                self.to_unit,
                self.result,
            ],
            spacing=20
        )
    
    def go_back(self,_):
        self.page.go("/")
    
    def convert_time(self,_):
        try:
            if self.input_value.value and self.from_unit.value and self.to_unit.value:
                value = float(self.input_value.value)
                from_unit = self.from_unit.value
                to_unit = self.to_unit.value
                
                # ! convet ke detik dahulu
                
                seconds = self.to_seconds(value,from_unit)
                
                # ! convert ke unit lainya
                
                result = self.from_seconds(seconds,to_unit)
                
                self.result.value = f"{value} {from_unit} = {result:.6g} {to_unit}"
                
            else:
                self.result.value = "please enter a valid number and select units to convert"
        except ValueError:
            self.result = "Please enter a valid value"
        self.update()
    
    def to_seconds(self,value,unit):
        conversions = {
            "Microsecond": 1e-6,
            "Milliseconds": 0.001,
            "Second": 1,
            "Minute": 60,
            "Hours": 3600,
            "Days": 86400,
            "Week": 604800,
            "Years": 31536000,  #
        }
        return value * conversions[unit]
    
    def from_seconds(self, seconds, unit):
        conversions = {
            "Microsecond": 1e6,
            "Milliseconds": 1000,
            "Second": 1,
            "Minute": 1/60,
            "Hours": 1/3600,
            "Days": 1/86400,
            "Week": 1/604800,
            "Years": 1/31536000,  # Assuming 365 days in a year
        }
        return seconds * conversions[unit]
