from datetime import datetime, timedelta

from bs4 import BeautifulSoup
from fastapi import requests

from app.core.database import session
from app.core.models import Currency

def get_currency_rates(date) -> None:
    url = f'https://cbr.ru/scripts/XML_daily.asp?date_req={date.strftime("%d/%m/%Y")}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'xml')

    records = soup.find_all('Record')
    for record in records:
        currency_id = record.get('Id')
        currency_value = record.find('Value').text
        currency_date = datetime.strptime(record.get('Date'), "%d.%m.%Y").date()
        session.add(Currency(date=currency_date, currency=currency_id, value=currency_value))

    session.commit()


#TODO: нейминг main сменить
def main():
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    #TODO: перегруженный метод разделить на два
    # 1. получает данные из ЦБ
    # 2. сохраняет в БД
    get_currency_rates(yesterday)
