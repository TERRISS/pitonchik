from fastapi import FastAPI
from app.service import get_current_cours

app = FastAPI()

@app.get("/currency_rates")
def currency_rates_endpoint() -> dict:
    get_current_cours()
    # result = get_current_cours()
    # return result
    return {"message": "sdasdas"}
