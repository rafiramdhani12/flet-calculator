import flet as ft
from module.speed import SpeedPage
from module.temperature import TempPage
from module.weight_mass import WeightMassPage
from module.length import LengthCalculatorPage
from module.date import DateCalculatorPage
from module.currency import CurrencyPage
from module.calculator import Calculator
from module.time import TimePage

# ! route start
def route_change(page: ft.Page ,route_event : ft.RouteChangeEvent):
    page.views.clear()
    if page.route == "/":
        page.views.append(
            ft.View(
                "/",
                [Calculator(page)],
            )
        )
    elif page.route == "/temperature":
        page.views.append(
            ft.View(
                "/temperature",
                [TempPage(page)],
            )
        )
    elif page.route == "/currency":
        page.views.append(
            ft.View(
                "/currency",
                [CurrencyPage(page)],
            )
        )
    elif page.route == "/date":
        page.views.append(
            ft.View(
                "/date",
                [DateCalculatorPage(page)],
            )
        )
    elif page.route == "/length":
        page.views.append(
            ft.View(
                "/length",
                [LengthCalculatorPage(page)],
            )
        )
    elif page.route == "/weight_mass":
        page.views.append(
            ft.View(
                "/weight_mass",
                [WeightMassPage(page)],
            )
        )
    elif page.route == "/speed":
        page.views.append(
            ft.View(
                "/speed",
                [SpeedPage(page)],
            )
        )
    elif page.route == "/time":
        page.views.append(
            ft.View(
                "/time",
                [TimePage(page)],
            )
        )
    page.update()

# ! route end
