import flet as ft
import requests


def main(page: ft.Page):
    page.title = "CryptoPriceTracker"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label='Введите название криптовалютной пары (пример: BTCUSDT)', width=400)
    crypto_price = ft.Text('')

    def get_info(e):
        if len(user_data.value) < 2:
            return

        symbol = user_data.value.upper()
        url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'

        try:
            response = requests.get(url).json()
            price = float(response['price'])
            crypto_price.value = f'Цена на {symbol} равна ' + str(price)
        except (KeyError, ValueError):
            crypto_price.value = f'Не удалось получить информацию о цене для {symbol}'

        page.update()

    def change_theme(e):
        if page.theme_mode == 'light':
            page.theme_mode = 'dark'
        else:
            page.theme_mode = 'light'
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
                ft.Text('Узнать цену на криптовалюту')
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([crypto_price], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.FilledTonalButton('Узнать', on_click=get_info)], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)
