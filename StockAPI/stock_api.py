from fastapi import FastAPI, HTTPException, status
import requests
import json

app = FastAPI()

@app.get("/stock/{ticker}")
async def root(ticker):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "apikey": "MXTEXXHKBY4S1F4U"
    }

    response = requests.get(url = "https://www.alphavantage.co/query", params = params)
    json_data = response.json()

    if "Time Series (Daily)" not in json_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid stock ticker"
    )
    
    days = list(json_data["Time Series (Daily)"].keys())
    price = json_data["Time Series (Daily)"][days[0]]["4. close"]
    return {"price": price}