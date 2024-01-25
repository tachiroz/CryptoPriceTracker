import flet as ft
import requests

# Словарь для использования котировок без USDT
symbol_mapping = {
    'BTC': 'BTCUSDT',
    'ETH': 'ETHUSDT',
    'BNB': 'BNBUSDT',
    'XRP': 'XRPUSDT',
    'ADA': 'ADAUSDT',
    'AVAX': 'AVAXUSDT',
    'APT': 'APTUSDT',
    'ARB': 'ARBUSDT'
}

history = []  # Список для хранения истории запросов


def main(page: ft.Page):
    page.title = "CryptoPriceTracker"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label='Введите название котировки криптовалюты (пример: BTC)', width=400)
    crypto_price = ft.Text('')
    history_text = ft.Text('История запросов: ')

    def get_info(e):
        if len(user_data.value) < 2:
            return

        symbol = user_data.value.upper()  # Преобразование введеных символов в верхний регистр

        if symbol in symbol_mapping:
            symbol = symbol_mapping[symbol]

        url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'

        try:
            response = requests.get(url).json()
            price = float(response['price'])
            crypto_price.value = f'Цена на {symbol} равна ' + str(price)
        except (KeyError, ValueError):
            crypto_price.value = f'Не удалось получить информацию о цене для {symbol}'

        history.append(f'Монета: {symbol}, цена: {price}')
        update_history_text()

        page.update()

    def update_history_text():
        # Обновление текстового виджета с историей запросов
        history_text.value = '\n'.join(history)


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
        ft.Row([ft.FilledButton('Узнать', on_click=get_info)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.Text('История запросов: ')], alignment=ft.MainAxisAlignment.START),
        ft.Row([history_text], alignment=ft.MainAxisAlignment.START)
    )


ft.app(target=main)
