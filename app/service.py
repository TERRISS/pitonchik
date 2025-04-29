from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
from sqlalchemy import values

from app.core.database import db_session
from app.core.models import Currency

def fetch_data(date) -> str:
    url = f'https://cbr.ru/scripts/XML_daily.asp?date_req={date.strftime("%d/%m/%Y")}'
    response = requests.get(url)
    response.encoding = 'utf-8' # Что бы не срало ISO-8859-1, решил попробовать utf-8
    return response.text

def save_rates(data: str) -> None:
    soup = BeautifulSoup(data, "xml")
    valutes = soup.find_all("Valute")
    currency_date = soup.ValCurs["Date"]
    for valute in valutes:
        try:
            num_code = valute.NumCode.text
            char_code = valute.CharCode.text
            nominal = valute.Nominal.text
            name = valute.Name.text
            print(f"Saving: {num_code}, {char_code}, {nominal}, {name}")  # Логированием решил почекать чё оно выдаёт по символам
        except Exception as e:
            print(f"Error processing valute: {e}")

        db_session.add(
            Currency(
                date=currency_date,
                NumCode = num_code,
                CharCode = char_code,
                Nominal = nominal,
                Name = name,
                Value = value
            )
        )

    db_session.commit()


def build_result_object(data):
    soup = BeautifulSoup(data, "xml")
    valutes = soup.find_all("Valute")
    currency_date = soup.ValCurs["Date"]
    result = []
    for valute in valutes:
        try:
            valute_objetc = {
                "num_code": valute.NumCode.text,
                "char_code": valute.CharCode.text,
                "nominal": valute.Nominal.text,
                "name": valute.Name.text,
                "value": valute.Value.text,
            }

            result.append(valute_objetc)
        except Exception as e:
            print(e)

    return result

def get_current_cours():
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    data = fetch_data(yesterday)
    save_rates(data)
    current_cours = build_result_object(data)

    return current_cours

def get_all_rates():
    return db_session.query(Currency).all()