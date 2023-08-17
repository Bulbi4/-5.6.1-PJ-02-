import json
import requests
from config import keys


class ConvertExeption(Exception):
    pass

class ConvertMoney:
    @staticmethod
    def getprice(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertExeption(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertExeption(f'Не обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertExeption(f'Не обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertExeption(f'Не обработать количество {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * float(amount)

        return total_base



