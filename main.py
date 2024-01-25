import flet as ft
import requests


def main(page: ft.Page):
    page.title = "CryptoPriceTracker"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label='Введите название криптовалюты', width=400)
    crypto_price = ft.Text('')

    def get_info(e):
        if len(user_data.value) < 2:
            return

        url = 'https://api.binance.com/api/v3/ticker/price'
        response = requests.get(url).json()
        temp = response['price']
        crypto_price.value = f'Цена на токен равна ' + str({temp})
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
        ft.Row([ft.ElevatedButton('Узнать', on_click=get_info)], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)
