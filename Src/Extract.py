import yfinance as yf
from sqlalchemy import text
from sqlalchemy.orm import Session
from datetime import timedelta

def extract_data(engine, tickers):
    session = Session(engine)
    maxDate = session.execute(text("SELECT max(date) from portfolio_ohlc_data")).scalar()
    session.close()

    if maxDate is None:
        data = yf.download(tickers, start="2022-01-01")
        return data
    else:
        startDate = maxDate + timedelta(days=1)
        data = yf.download(tickers, start= startDate)
        return data

