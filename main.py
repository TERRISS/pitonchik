from fastapi import FastAPI

from app.api.schemas import CurrencyRatesResponseSchame
from app.service import get_current_cours

app = FastAPI()

@app.get("/currency_rates", response_model=CurrencyRatesResponseSchame)
def currency_rates_endpoint() -> dict:
    current_cours = get_current_cours()
    # result = get_current_cours()
    # return result
    print(current_cours)

    result = CurrencyRatesResponseSchame(
        valutes = current_cours,
    )

    return result
