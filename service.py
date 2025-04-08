import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from database import session, Currency


def get_currency_rates(date):
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


def main():
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    get_currency_rates(yesterday)


if __name__ == '__main__':
    main()
