import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from database import session, Currency

def get_currency_rates(date):
    url = f'https://cbr.ru/scripts/XML_daily.asp?date_req={date.strftime("%d/%m/%Y")}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'xml')
    currencies = soup.find_all('Valute')
    for currency in currencies:
        currency_code = currency.find('CharCode').text
        currency_value = currency.find('Value').text
        session.add(Currency(date=date, currency=currency_code, value=currency_value))
    session.commit()

def main():
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    get_currency_rates(yesterday)

if __name__ == '__main__':
    main()