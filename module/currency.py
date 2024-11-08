import flet as ft


# ! currency page start

class CurrencyPage(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.amount_input = ft.TextField(label="Amount", on_change=self.convert_currency)
        self.from_currency = ft.Dropdown(
            label="From",
            options=[
                ft.dropdown.Option("USD"),
                ft.dropdown.Option("EUR"),
                ft.dropdown.Option("GBP"),
                ft.dropdown.Option("JPY"),
                ft.dropdown.Option("AUD"),
                ft.dropdown.Option("IDR"),
            ],
            on_change=self.convert_currency
        )
        self.to_currency = ft.Dropdown(
            label="To",
            options=[
                ft.dropdown.Option("USD"),
                ft.dropdown.Option("EUR"),
                ft.dropdown.Option("GBP"),
                ft.dropdown.Option("JPY"),
                ft.dropdown.Option("AUD"),
                ft.dropdown.Option("IDR"),
            ],
            on_change=self.convert_currency
        )
        self.result = ft.Text(size=20, color=ft.colors.WHITE)

    def build(self):
        return ft.Column(
            controls=[
                ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.go_back),
                ft.Text("Currency Conversion", size=30, color=ft.colors.WHITE),
                self.amount_input,
                self.from_currency,
                self.to_currency,
                self.result,
            ],
            spacing=20
        )

    def go_back(self, _):
        self.page.go("/")

    def convert_currency(self, _):
        try:
            amount = float(self.amount_input.value)
            from_curr = self.from_currency.value
            to_curr = self.to_currency.value
            
            # Simplified conversion rates (not real-time)
            rates = {
                "USD": 1.0,
                "EUR": 0.85,
                "GBP": 0.73,
                "JPY": 110.0,
                "AUD": 1.35,
                "IDR": 14500.0  # Approximate rate, 1 USD = 14500 IDR
            }
            
            if from_curr and to_curr:
                result = amount * (rates[to_curr] / rates[from_curr])
                self.result.value = f"{amount} {from_curr} = {result:.2f} {to_curr}"
            else:
                self.result.value = "Please select both currencies"
        except ValueError:
            self.result.value = "Please enter a valid amount"
        self.update()
        
# ! currency page end
