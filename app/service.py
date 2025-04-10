from datetime import datetime, timedelta

from bs4 import BeautifulSoup
from fastapi import requests

from app.core.database import session
from app.core.models import Currency

def fetch_data(date) -> str:
    url = f'https://cbr.ru/scripts/XML_daily.asp?date_req={date.strftime("%d/%m/%Y")}'
    response = requests.get(url)
    return response.text

def save_rates(data: str) -> None:
    soup = BeautifulSoup(data, 'xml')
    records = soup.find_all('Record')
    for record in records:
        currency_id = record.get('Id')
        currency_value = record.find('Value').text
        currency_date = datetime.strptime(record.get('Date'), "%d.%m.%Y").date()
        session.add(Currency(date=currency_date, currency=currency_id, value=currency_value))

    session.commit()

def oooGore():
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    data = fetch_currency_data(yesterday)
    save_currency_rates(data)
