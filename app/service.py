from datetime import datetime, timedelta
from typing import List

import requests

from app.core.database import db_session
from app.core.models import Currency

import xml.etree.ElementTree as ET

def fetch_data(date) -> str:
    url = f'https://cbr.ru/scripts/XML_daily.asp?date_req={date.strftime("%d/%m/%Y")}'
    response = requests.get(url)
    response.encoding = 'windows-1251'

    return response.text


def parse_data(xml_text: str):
    root = ET.fromstring(xml_text)
    valutes = []

    for valute in root.findall('Valute'):
        valutes.append({
            'num_code': valute.find('NumCode').text,
            'char_code': valute.find('CharCode').text,
            'nominal': valute.find('Nominal').text,
            'name': valute.find('Name').text,
            'value': valute.find('Value').text
        })

    return valutes


def save_rates(data: List, currency_date: datetime) -> None:
    for dict_data in data:
        #TODO: взять каждый элемент словаря
        num_code = dict_data['num_code']
        char_code = dict_data['char_code']
        nominal = dict_data['nominal']
        name = dict_data['name']
        value = dict_data['value'] #взял
        #TODO: сделать проверку на currency_date, что бы не было повторяющихся данных
        existing_rate = db_session.query(Currency).filter_by(date=currency_date, NumCode=num_code).first() #Если existing_rate = None, то подобных данных ещё нету
        if existing_rate is None:
            db_session.add(
                Currency(
                    date = currency_date,
                    NumCode = num_code,
                    CharCode = char_code,
                    Nominal = nominal,
                    Name = name,
                    Value = value
                )
            )
    db_session.commit()

def get_current_cours():
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    data = fetch_data(yesterday)
    parsed_data = parse_data(data)
    #TODO: научить из списка преображать в сохранение в бд
    save_rates(data=parsed_data,currency_date=yesterday)

    return parsed_data

def get_all_rates():
    return db_session.query(Currency).all()