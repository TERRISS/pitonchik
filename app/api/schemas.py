from typing import List

from pydantic import BaseModel, Field


class ValuteSchema(BaseModel):
    num_code: str = Field(..., description="Цифровой код валюты (NumCode)")
    char_code: str = Field(..., description="Буквенный код валюты (CharCode)")
    nominal: str = Field(..., description="Номинал")
    name: str = Field(..., description="Наименование валюты")
    value: str = Field(..., description="Курс валюты (в строке, с запятой)")


class CurrencyRatesResponseSchame(BaseModel):
    valutes: List[ValuteSchema]