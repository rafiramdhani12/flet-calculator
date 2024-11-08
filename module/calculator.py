import flet as ft
import math

# ! calculator start

class Calculator(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.result = ft.Text(value="0", color=ft.colors.WHITE, size=20)

    def build(self):
        return ft.Container(
            width=500,
            height=500,
            bgcolor=ft.colors.BLACK,
            border_radius=ft.border_radius.all(20),
            padding=35,
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.IconButton(icon=ft.icons.MENU, on_click=self.show_menu),
                            self.result,
                        ],
                        alignment="spaceBetween",
                    ),
                    ft.Row(controls=[
                        ExtraActionButton(text="1/x", button_clicked=self.button_clicked),
                        ExtraActionButton(text="√x", button_clicked=self.button_clicked),
                        ExtraActionButton(text="x²", button_clicked=self.button_clicked),
                        ExtraActionButton(text="<=", button_clicked=self.button_clicked)
                        ]),
                    ft.Row(
                        controls=[
                            ExtraActionButton(text="AC", button_clicked=self.button_clicked),
                            ExtraActionButton(text="+/-", button_clicked=self.button_clicked),
                            ExtraActionButton(text="%", button_clicked=self.button_clicked),
                            ActionButton(text="/", button_clicked=self.button_clicked),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="7", button_clicked=self.button_clicked),
                            DigitButton(text="8", button_clicked=self.button_clicked),
                            DigitButton(text="9", button_clicked=self.button_clicked),
                            ActionButton(text="*", button_clicked=self.button_clicked),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="4", button_clicked=self.button_clicked),
                            DigitButton(text="5", button_clicked=self.button_clicked),
                            DigitButton(text="6", button_clicked=self.button_clicked),
                            ActionButton(text="-", button_clicked=self.button_clicked),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="1", button_clicked=self.button_clicked),
                            DigitButton(text="2", button_clicked=self.button_clicked),
                            DigitButton(text="3", button_clicked=self.button_clicked),
                            ActionButton(text="+", button_clicked=self.button_clicked),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="0", button_clicked=self.button_clicked, expand=2),
                            DigitButton(text=".", button_clicked=self.button_clicked),
                            ActionButton(text="=", button_clicked=self.button_clicked),
                        ]
                    ),
                ]
            ),
        )

    def button_clicked(self, e):
        if e.control.data == "AC":
            self.result.value = "0"
        elif e.control.data == "<=":
            self.result.value = self.result.value[:-1] if len(self.result.value) > 1 else "0"
        elif e.control.data == "+/-":
            self.result.value = str(-float(self.result.value))
        elif e.control.data == "%":
            try:
                self.result.value = str(float(self.result.value) * 0.01)
            except ValueError:
                self.result.value = "Error"
        elif e.control.data == "=":
            try:
                self.result.value = str(eval(self.result.value))
            except:
                self.result.value = "Error"
        elif e.control.data == "1/x":
            try:
                self.result.value = str(1/float(self.result.value))
            except(ValueError,ZeroDivisionError):
                self.result.value = "Error"
        elif e.control.data == "√x":
            try:
                value = float(self.result.value)
                if value >= 0:
                    self.result.value = str(round(math.sqrt(value),8))
                else:
                    self.result.value = "Error"
            except ValueError:
                self.result.value
        elif e.control.data == "x²":
            try:
                self.result.value = str(float(self.result.value) ** 2)
            except ValueError:
                self.result.value = "Error"
        else:
            self.result.value = e.control.data if self.result.value == "0" else self.result.value + e.control.data
        self.result.update()

    def show_menu(self, _):
        self.page.bottom_sheet.open = True
        self.page.update()

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked, expand=1):
        super().__init__(text=text, expand=expand, on_click=button_clicked, data=text)

class DigitButton(CalcButton):
    def __init__(self, text, button_clicked, expand=1):
        super().__init__(text, button_clicked, expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE

class ActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        super().__init__(text, button_clicked)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE

class ExtraActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        super().__init__(text, button_clicked)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK

# ! calculator end
