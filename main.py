from fastapi import FastAPI
from service import main

app = FastAPI()

@app.get("/currency_rates")
def get_currency_rates():
    main()
    return {"message": "Currency rates updated"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)