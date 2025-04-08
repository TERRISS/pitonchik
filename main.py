from typing import Dict, List, Any

from fastapi import FastAPI
from app.service import main

app = FastAPI()

@app.get("/currency_rates")
def get_currency_rates() -> dict:
    main()
    # TODO return dict {
    #
    #  }

    prarm = 23432
    return {"message": prarm}

# TODO: start uvicorn uvicorn main:app --reload --host 0.0.0.0 --port 8000
# TODO: install uvicorn

# TODO: install black and isort
# что бы исправить код black app
# что бы исрпавить иморты isort app