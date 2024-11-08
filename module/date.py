import flet as ft
from datetime import datetime , timedelta

# ! date page start

class DateCalculatorPage(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.start_date_input = ft.TextField(label="Start Date (YYYY-MM-DD)", on_change=self.calculate_difference)
        self.end_date_input = ft.TextField(label="End Date (YYYY-MM-DD)", on_change=self.calculate_difference)
        self.result = ft.Text(size=20, color=ft.colors.WHITE)
        self.add_days_result = ft.Text(color=ft.colors.WHITE)
        
    def build(self):
        return ft.Column(
            controls=[
                ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.go_back),
                ft.Text("Date Calculation", size=30, color=ft.colors.WHITE),
                ft.Text("Calculate difference between two dates:", size=16, color=ft.colors.WHITE),
                self.start_date_input,
                self.end_date_input,
                self.result,
            ],
            spacing=20
        )

    def go_back(self, _):
        self.page.go("/")

    def calculate_difference(self, _):
        try:
            start = datetime.strptime(self.start_date_input.value, "%Y-%m-%d")
            end = datetime.strptime(self.end_date_input.value, "%Y-%m-%d")
            difference = end - start
            self.result.value = f"Difference: {difference.days} days"
        except ValueError:
            self.result.value = "Please enter valid dates in YYYY-MM-DD format"
        self.update()
        